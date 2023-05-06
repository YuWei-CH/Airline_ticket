# Import Flask Library
from flask import Flask, render_template, request, session, url_for, redirect
import pymysql.cursors
import datetime
import calendar
import hashlib
import decimal


# Initialize the app from Flask
app = Flask(__name__)


# Configure MySQL
conn = pymysql.connect(host='localhost',
                       port=8889,
                       user='root',
                       password='root',
                       db='Test-flight',
                       charset='utf8mb4',
                       cursorclass=pymysql.cursors.DictCursor)
'''
# Configure MySQL
conn = pymysql.connect(host='localhost',
                       user='root',
                       password='',
                       db='air_ticket_system',
                       charset='utf8mb4',
                       cursorclass=pymysql.cursors.DictCursor)
'''

# Define a route to hello function


@app.route('/')
def hello():
    return render_template('index.html')

# Define logout


@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')


# Define route for login


@app.route('/User/user-login.html')
def userlogin():
    return render_template('User/user-login.html')

# Define route for register


@app.route('/User/user-register.html')
def userregister():
    return render_template('User/user-register.html')

# search and book for specific flight by user


@app.route('/User/user-flight-booking.html')
def booking():
    return render_template('User/user-flight-booking.html')

# query future flight


@app.route('/search_flights', methods=['POST'])
def search_flights():
    # get data from form
    airline_name = request.form['airline_name']
    flight_number = request.form['flight_number']
    departure_date_and_time = request.form['departure_date_and_time']
    arrival_date_and_time = request.form['arrival_date_and_time']
    arrival_airport_code = request.form['arrival_airport_code']
    departure_airport_code = request.form['departure_airport_code']

    # cursor used to send queries
    cursor = conn.cursor()
    # build the query string based on user input
    query = "SELECT * FROM Flight WHERE 1=1"
    params = []
    if airline_name:
        query += " AND airline_name=%s"
        params.append(airline_name)
    if flight_number:
        query += " AND flight_number=%s"
        params.append(flight_number)
    if departure_date_and_time:
        query += " AND departure_date_and_time=%s"
        params.append(departure_date_and_time)
    if arrival_date_and_time:
        query += " AND arrival_date_and_time=%s"
        params.append(arrival_date_and_time)
    if arrival_airport_code:
        query += " AND arrival_airport_code=%s"
        params.append(arrival_airport_code)
    if departure_airport_code:
        query += " AND departure_airport_code=%s"
        params.append(departure_airport_code)
    cursor.execute(query, tuple(params))

    # stores the results in a variable
    flights = cursor.fetchall()
    # use fetchall() if you are expecting more than 1 data row
    cursor.close()
    if len(flights) == 0:
        # no flights
        error = 'No flights found for the selected criteria.'
        return render_template('index.html', error=error)

    # Return result
    return render_template('index.html', flights=flights)

# Authenticates the login


@app.route('/loginAuth', methods=['GET', 'POST'])
def userloginAuth():
    # grabs information from the forms
    email = request.form['email']
    password = request.form['password']

    # get hashed password
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    # cursor used to send queries
    cursor = conn.cursor()
    # executes query
    query = 'SELECT * FROM Customer WHERE email_address = %s and c_password = %s'
    cursor.execute(query, (email, hashed_password))
    # stores the results in a variable
    data = cursor.fetchone()
    # use fetchall() if you are expecting more than 1 data row
    # search name
    name_query = 'SELECT first_name FROM Customer WHERE email_address = %s and c_password = %s'
    cursor.execute(name_query, (email, hashed_password))
    # stores the results in a variable
    name = cursor.fetchone()
    cursor.close()
    error = None
    if (data):
        # creates a session for the the user
        # session is a built in
        session['username'] = name
        session['email'] = email
        session['type'] = "customer"
        return redirect(url_for('user_main'))
    else:
        # returns an error message to the html page
        error = 'Invalid login or email'
        return render_template('User/user-login.html', error=error)


# Authenticates the register
@app.route('/registerAuth', methods=['GET', 'POST'])
def userregisterAuth():
    if request.method == 'POST':
        # grabs information from the forms
        email = request.form['email']
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        password = request.form['password']
        building_number = request.form['building_number']
        street_name = request.form['street_name']
        apartment_number = request.form['apartment_number']
        city = request.form['city']
        state = request.form['state']
        zip_code = request.form['zip_code']
        phone_number = request.form['phone_number']
        passport_number = request.form['passport_number']
        passport_expiration = request.form['passport_expiration']
        passport_country = request.form['passport_country']
        date_of_birth = request.form['date_of_birth']

    #  hash the password
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    # cursor used to send queries
    cursor = conn.cursor()
    # executes query
    query = 'SELECT * FROM Customer WHERE email_address = %s'
    cursor.execute(query, (email))
    # stores the results in a variable
    data = cursor.fetchone()
    # use fetchall() if you are expecting more than 1 data row
    error = None
    if (data):
        # If the previous query returns data, then user exists
        error = "This user already exists"
        return render_template('User/user-register.html', error=error)
    else:
        ins = "INSERT INTO Customer (email_address,first_name, last_name, c_password, building_number, street_name, apartment_number, city, state, zip_code, passport_number, passport_expiration, passport_country, date_of_birth) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s,%s, %s, %s, %s)"
        cursor.execute(ins, (email, first_name, last_name, hashed_password, building_number, street_name, apartment_number, city,
                             state, zip_code, passport_number, passport_expiration, passport_country, date_of_birth))
        conn.commit()
        phone_list = phone_number.split(";")
        # insert phone number
        for i in phone_list:
            phone_ins = "INSERT INTO Customer_Phone_Number (email_address, phone_number) VALUES (%s,%s)"
            cursor.execute(phone_ins, (email, i))
            conn.commit()
        # conn.commit()
        cursor.close()
        return render_template('index.html')


@app.route('/user-main', methods=['GET', 'POST'])
def user_main(error=None):

    username = session['username']
    email = session['email']
    # cursor used to send queries
    cursor = conn.cursor()
    # executes query
    query = "SELECT * FROM (SELECT t.calculated_price_of_ticket, f.airline_name, f.departure_date_and_time, f.arrival_date_and_time, f.arrival_airport_code, f.departure_airport_code, f.flight_number FROM Ticket t JOIN Flight f ON f.flight_number=t.flight_number WHERE email_address= %s) AS derived_table_alias WHERE (derived_table_alias.departure_date_and_time > NOW()  AND derived_table_alias.arrival_date_and_time > NOW());"
    cursor.execute(query, (email))
    # stores the results in a variable
    flights = cursor.fetchall()
    cursor.close()
    return render_template('User/user-main.html', username=username, flights=flights, error=error)


@app.route('/purchase-form/<flight_number>', methods=['GET', 'POST'])
def purchase_form(flight_number):
    return render_template('User/user-payment.html', flight_number=flight_number)


@app.route('/purchase_result')
def purchase_result():
    return render_template('User/user-purchase-result.html')

# For purchase-form, I have to ignore CSS 404. If not, it will jump to error


@app.route('/CSS/<path:path>')
def serve_css(path):
    """Serve CSS files"""
    return "", 404 if not path.endswith('.css') else 200

# render rate flight


@app.route('/user-track', methods=['GET', 'POST'])
def user_track():
    email = session['email']
    # cursor used to send queries
    cursor = conn.cursor()
    # executes query
    query = "SELECT DISTINCT * FROM (SELECT f.airline_name, f.departure_date_and_time, f.arrival_date_and_time, f.arrival_airport_code, f.departure_airport_code, f.flight_number FROM Ticket t JOIN Flight f ON f.flight_number=t.flight_number WHERE email_address= %s) AS derived_table_alias WHERE arrival_date_and_time < NOW();"
    cursor.execute(query, (email))
    # stores the results in a variable
    flights = cursor.fetchall()
    print(flights)
    cursor.close()
    return render_template('User/user-track.html', flights=flights)

# display result of rating


@app.route('/rate-result', methods=['GET', 'POST'])
def rate_result():
    return render_template('User/user-rate-result.html')


# dispaly 1 year and 6 month spending
@app.route("/user-spend")
def track_spending():

    # get current month and year
    now = datetime.datetime.now()
    # current_month = now.month
    # current_year = now.year

    email = session['email']
    # cursor used to send queries
    cursor = conn.cursor()

    # query past 1 year
    query = "SELECT SUM(t.calculated_price_of_ticket) FROM Ticket t JOIN Purchase p ON t.ticket_ID = p.ticket_ID WHERE t.email_address = %s AND p.purchase_date_and_time >= DATE_SUB(NOW(), INTERVAL 1 YEAR);"
    cursor.execute(query, (email))
    total_spending = cursor.fetchone()['SUM(t.calculated_price_of_ticket)']

    # data store in `spending_data`
    # key of spending_data month, value is spending

    # get past 6 month
    now = datetime.datetime.now()
    date_ranges = []
    for i in range(6):
        year = now.year
        month = now.month - i
        if month <= 0:
            month += 12
            year -= 1
        end_of_month = calendar.monthrange(year, month)[1]
        end_date = now.replace(year=year, month=month, day=end_of_month)
        start_date = end_date.replace(day=1)
        date_ranges.append((start_date, end_date))
    monthly_spending = {}
    for date_range in date_ranges:
        start_date = date_range[0].strftime('%Y-%m-%d 00:00:00')
        end_date = date_range[1].strftime('%Y-%m-%d 23:59:59')
        query = "SELECT SUM(t.calculated_price_of_ticket) FROM Ticket t JOIN Purchase p ON t.ticket_ID = p.ticket_ID WHERE t.email_address = %s AND p.purchase_date_and_time BETWEEN %s AND %s;"
        cursor.execute(query, (email, start_date, end_date))
        monthly_spend = cursor.fetchone()['SUM(t.calculated_price_of_ticket)']
        if monthly_spend is None:
            monthly_spend = 0  # if no spending, set it to 0
        month_year = date_range[0].strftime('%B %Y')
        monthly_spending[month_year] = monthly_spend
    if 'specific_monthly_spending' in session:
        specific_monthly_spending = session['specific_monthly_spending']
    else:
        specific_monthly_spending = None
    print(specific_monthly_spending)
    cursor.close()
    # send data back
    return render_template("User/user-spend.html",
                           total_spending=total_spending,
                           monthly_spending=monthly_spending, specific_monthly_spending=specific_monthly_spending)


"""
#########################
"""

# user-main future search


@app.route('/search_user_flights', methods=['POST'])
def search_user_flights():
    email = session['email']
    username = session['username']
    # get data from form
    flight_number = request.form['flight_number']
    departure_date_and_time = request.form['departure_date_and_time']
    arrival_date_and_time = request.form['arrival_date_and_time']
    arrival_airport_code = request.form['arrival_airport_code']
    departure_airport_code = request.form['departure_airport_code']

    # cursor used to send queries
    cursor = conn.cursor()

    # list of conditions to include in the query
    conditions = []
    values = [email]

    # check if flight number is provided
    if flight_number:
        conditions.append("flight_number = %s")
        values.append(flight_number)

    # check if departure date and time is provided
    if departure_date_and_time:
        conditions.append("departure_date_and_time = %s")
        values.append(departure_date_and_time)

    # check if arrival date and time is provided
    if arrival_date_and_time:
        conditions.append("arrival_date_and_time = %s")
        values.append(arrival_date_and_time)

    # check if arrival airport code is provided
    if arrival_airport_code:
        conditions.append("arrival_airport_code = %s")
        values.append(arrival_airport_code)

    # check if departure airport code is provided
    if departure_airport_code:
        conditions.append("departure_airport_code = %s")
        values.append(departure_airport_code)

    # combine conditions into SQL query
    query = "SELECT * FROM (SELECT f.airline_name, f.departure_date_and_time, f.arrival_date_and_time, f.arrival_airport_code, f.departure_airport_code, f.flight_number FROM Ticket t JOIN Flight f ON f.flight_number = t.flight_number WHERE email_address = %s) AS derived_table_alias"
    if conditions:
        query += " WHERE " + " AND ".join(conditions)

    values = tuple(values)
    # execute query
    cursor.execute(query, values)

    # stores the results in a variable
    flights = cursor.fetchall()

    if len(flights) == 0:
        # no flights
        error = 'No flights found for the selected criteria.'
        return render_template('User/user-main.html', error=error, username=username)

    # Return result
    return render_template('User/user-main.html', flights=flights, username=username)

# user book


@app.route('/search_and_book_flight', methods=['GET', 'POST'])
def search_and_book_flight():
    # get data from form
    cursor = conn.cursor()
    airline_name = request.form['airline_name']
    flight_number = request.form['flight_number']
    departure_date_and_time = request.form['departure_date_and_time']
    arrival_date_and_time = request.form['arrival_date_and_time']
    arrival_airport_code = request.form['arrival_airport_code']
    departure_airport_code = request.form['departure_airport_code']

    query = "SELECT * FROM Flight WHERE (departure_date_and_time>NOW() AND arrival_date_and_time>NOW())"

    conditions = []
    params = []

    if airline_name:
        conditions.append("airline_name = %s")
        params.append(airline_name)

    if flight_number:
        conditions.append("flight_number = %s")
        params.append(flight_number)

    if departure_date_and_time:
        conditions.append("departure_date_and_time = %s")
        params.append(departure_date_and_time)

    if arrival_date_and_time:
        conditions.append("arrival_date_and_time = %s")
        params.append(arrival_date_and_time)

    if arrival_airport_code:
        conditions.append("arrival_airport_code = %s")
        params.append(arrival_airport_code)

    if departure_airport_code:
        conditions.append("departure_airport_code = %s")
        params.append(departure_airport_code)

    if conditions:
        query += " AND " + " AND ".join(conditions)

    cursor.execute(query, tuple(params))
    flights = cursor.fetchall()
    # use fetchall() if you are expecting more than 1 data row
    cursor.close()
    if len(flights) == 0:
        # no flights
        error = 'No flights found for the selected criteria.'
        return render_template('User/user-flight-booking.html', error=error)

        # Return result
    return render_template('User/user-flight-booking.html', flights=flights)
# Purchase flight


@app.route('/purchase_flight/<flight_number>', methods=['GET', 'POST'])
def purchase_flight(flight_number):
    flight_number = flight_number
    email = session['email']
    card_number = request.form['card_number']
    card_type = request.form['card_type']
    name = request.form['card_name']
    expiration_date = request.form['expiration_date']

    # cursor used to send queries
    cursor = conn.cursor()

    # add card information
    query = "INSERT IGNORE INTO Payment_Information (card_number, card_type, name_on_card, expiration_date) VALUES (%s, %s, %s, %s);"
    cursor.execute(query, (card_number, card_type, name, expiration_date))

    # purcharse here

    # find ticket ratio
    """
    1. find identification_number by flight_number in Fly table
    2. use identification_number find number_of_seats in Airplane table and save as t_seats
    3. find how many record of this flight_number in Ticket table as t_tickets
    4. get purchase_ratio by t_tickets/t_seats
    """
    query = "SELECT COUNT(DISTINCT t.ticket_id) / a.number_of_seats AS purchase_ratio FROM Fly AS f JOIN Ticket AS t ON f.flight_number = t.flight_number JOIN Airplane AS a ON f.identification_number = a.identification_number WHERE f.flight_number = %s GROUP BY f.flight_number, a.number_of_seats;"
    cursor.execute(query, (flight_number))
    result = cursor.fetchone()
    if result is not None:
        purchase_ratio = result['purchase_ratio']
    else:
        purchase_ratio = 0

    # insert ticket information
    """
    1. get email by session['email']
    2. find first_name, last_name, date_of_birth in Customer table by email
    3. get base_price_of_ticket by flight_number in Flight
    4. calculate price of ticket 
    5. find airline_name, flight_number, departure_date_time in Flight table by flight_number
    6. extract data and Insert
    """
    query = "SELECT first_name, last_name, date_of_birth FROM Customer WHERE email_address = %s;"
    cursor.execute(query, (email))
    result = cursor.fetchone()
    print(result)
    first_name = result['first_name']
    last_name = result['last_name']
    date_of_birth = result['date_of_birth']

    query = "SELECT base_price_of_ticket FROM Flight WHERE flight_number = %s ;"
    cursor.execute(query, (flight_number))
    result = cursor.fetchone()
    base_price = result['base_price_of_ticket']
    if purchase_ratio >= 0.8:
        calculated_price_of_ticket = decimal.Decimal(
            base_price) * decimal.Decimal('1.25')
    else:
        calculated_price_of_ticket = base_price

    query = "SELECT airline_name, departure_date_and_time FROM Flight WHERE flight_number = %s ;"
    cursor.execute(query, (flight_number))
    result = cursor.fetchone()
    airline_name = result['airline_name']
    departure_date_and_time = result['departure_date_and_time']

    query = "INSERT INTO `Ticket` (`ticket_ID`, `first_name`, `last_name`, `date_of_birth`, `calculated_price_of_ticket`, `airline_name`, `flight_number`, `departure_date_and_time`, `email_address`) VALUES (NULL, %s, %s, %s, %s, %s, %s, %s,%s);"
    cursor.execute(query, (first_name, last_name, date_of_birth, calculated_price_of_ticket,
                   airline_name, flight_number, departure_date_and_time, email))
    ticket_ID = cursor.lastrowid
    # insert ticket_ID, card_number and current date to Purcahse table
    # get ticket ID

    query = "INSERT INTO Purchase (ticket_ID,card_number, purchase_date_and_time) VALUES (%s,%s, NOW());"
    cursor.execute(query, (ticket_ID, card_number))
    conn.commit()
    cursor.close()
    return redirect(url_for('purchase_result'))

# search and rate and comment


@app.route('/search_and_rate', methods=['POST'])
def search_and_rate():
    email = session['email']
    # get data from form
    airline_name = request.form['airline_name']
    flight_number = request.form['flight_number']
    departure_date_and_time = request.form['departure_date_and_time']
    cursor = conn.cursor()

    query = "SELECT DISTINCT * FROM (SELECT f.airline_name, f.departure_date_and_time, f.arrival_date_and_time, f.arrival_airport_code, f.departure_airport_code, f.flight_number FROM Ticket t JOIN Flight f ON f.flight_number=t.flight_number WHERE email_address= %s) AS derived_table_alias WHERE arrival_date_and_time < NOW();"
    cursor.execute(query, (email))
    # stores the results in a variable
    flights = cursor.fetchall()
    if len(flights) > 0:
        rate = request.form['rating']
        comment = request.form['comment']

        # cursor used to send queries
        # executes query
        # print(email)
        query = "SELECT DISTINCT * FROM Evaluation WHERE email_address = %s AND airline_name = %s AND flight_number = %s AND departure_date_and_time = %s;"
        cursor.execute(query, (email, airline_name,
                       flight_number, departure_date_and_time))
        result = cursor.fetchone()

        if result is not None:
            # Update existing record
            text = "Sorry, you already rate and comment for this flight"
        else:
            # Insert new record
            insert_query = "INSERT INTO Evaluation (email_address,airline_name,flight_number,departure_date_and_time,rate,comment) VALUES (%s,%s,%s,%s,%s,%s);"
            cursor.execute(insert_query, (email, airline_name,
                           flight_number, departure_date_and_time, rate, comment))
            text = "Thanks, you are successfully submit your rate and comment"
            # commit changes
            conn.commit()
        # close cursor and connection
        cursor.close()
        return render_template('User/user-rate-result.html', text=text)
    else:
        cursor.close()
        return render_template('User/user-track.html', flights=flights)


# track user spend specifically


@app.route('/track-specific-spend', methods=['POST'])
def track_specific_spend():
    cursor = conn.cursor()
    email = session['email']
    start_date = datetime.datetime.strptime(
        request.form['start-date'], '%Y-%m-%d').strftime('%Y-%m-%d')
    end_date = datetime.datetime.strptime(
        request.form['end-date'], '%Y-%m-%d').strftime('%Y-%m-%d')
    query = "SELECT SUM(t.calculated_price_of_ticket) FROM Ticket t JOIN Purchase p ON t.ticket_ID = p.ticket_ID WHERE t.email_address = %s AND p.purchase_date_and_time BETWEEN %s AND %s;"
    cursor.execute(query, (email, start_date, end_date))
    total_monthly_spend = cursor.fetchone(
    )['SUM(t.calculated_price_of_ticket)']

    # get monthly spending
    start_year, start_month, start_day = start_date.split('-')
    end_year, end_month, end_day = end_date.split('-')
    start_month = int(start_month)
    end_month = int(end_month)
    year_diff = int(end_year) - int(start_year)
    month_diff = end_month - start_month + 1 + year_diff * 12
    specific_monthly_spending = {}
    for i in range(month_diff):
        year = start_year
        month = start_month + i
        if month > 12:
            year = str(int(year) + 1)
            month -= 12
        if i == 0:
            start_day = int(start_day)
        else:
            start_day = 1
        if i == month_diff - 1:
            end_day = int(end_day)
        else:
            end_day = calendar.monthrange(int(year), month)[1]
        start_time = "00:00:00"
        end_time = "23:59:59"
        date_range = (f"{year}-{month:02}-{start_day} {start_time}",
                      f"{year}-{month:02}-{end_day} {end_time}")
        query = "SELECT SUM(t.calculated_price_of_ticket) FROM Ticket t JOIN Purchase p ON t.ticket_ID = p.ticket_ID WHERE t.email_address = %s AND p.purchase_date_and_time BETWEEN %s AND %s;"
        cursor.execute(query, (email, date_range[0], date_range[1]))
        monthly_spend = cursor.fetchone(
        )['SUM(t.calculated_price_of_ticket)']
        if monthly_spend is None:
            monthly_spend = 0
        month_year = f"{calendar.month_name[month]} {year}"
        specific_monthly_spending[month_year] = monthly_spend
    session['specific_monthly_spending'] = (
        total_monthly_spend, specific_monthly_spending)
    cursor.close()

    # send data back
    return redirect(url_for('track_spending'))


@app.route('/cancel', methods=['POST'])
def cancel():
    flight_number = request.form['flight_number']
    departure_date_and_time = request.form['departure_date_and_time']
    cursor = conn.cursor()
    email = session['email']

    # how long

    now = datetime.datetime.now()
    departure_time_str = departure_date_and_time
    departure_time = datetime.datetime.strptime(
        departure_time_str, "%Y-%m-%d %H:%M:%S")
    time_difference = departure_time - now

    error = None
    # if > 24 h
    if time_difference > datetime.timedelta(hours=24):
        # Delete
        query = "DELETE FROM Ticket WHERE email_address = %s AND flight_number = %s AND departure_date_and_time = %s;"
        cursor.execute(query, (email, flight_number, departure_date_and_time))
    else:
        error = "Sorry, you can't delete it. Less than 24 hours left."
    conn.commit()
    return redirect(url_for('user_main', error=error))  # back


"""

STAFF CODE


"""


@app.route('/Staff/staff-login.html')
def stafflogin():
    return render_template('Staff/staff-login.html')

# Define route for register


@app.route('/Staff/staff-register.html')
def staffregister():
    return render_template('Staff/staff-register.html')

# Authenticates the login


@app.route('/staffLoginAuth', methods=['GET', 'POST'])
def staffLoginAuth():
    # grabs information from the forms
    username = request.form['username']
    password = request.form['password']

    # get hashed password
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    # cursor used to send queries
    cursor = conn.cursor()
    # executes query
    query = 'SELECT * FROM Airline_Staff WHERE username = %s and s_password = %s'
    cursor.execute(query, (username, hashed_password))
    # stores the results in a variable
    data = cursor.fetchone()
    # use fetchall() if you are expecting more than 1 data row
    # search name
    name_query = 'SELECT first_name FROM Airline_Staff WHERE username = %s and s_password = %s'
    cursor.execute(name_query, (username, hashed_password))
    # stores the results in a variable
    name = cursor.fetchone()
    cursor.close()
    error = None
    if (data):
        # creates a session for the the user
        # session is a built in
        session['username'] = username
        session['name'] = name
        session['type'] = "staff"
        return redirect(url_for('staff_main'))
    else:
        # returns an error message to the html page
        error = 'Invalid username or password!'
        return render_template('Staff/staff-login.html', error=error)


# Authenticates the register
@app.route('/staffRegisterAuth', methods=['GET', 'POST'])
def staffRegisterAuth():
    if request.method == 'POST':
        # grabs information from the forms
        username = request.form['username']
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        password = request.form['password']
        email = request.form['email']
        phone_number = request.form['phone_number']
        date_of_birth = request.form['date_of_birth']
        airline_name = request.form['airline_name']

    #  hash the password
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    # cursor used to send queries
    cursor = conn.cursor()
    # executes query
    query = 'SELECT * FROM Airline_Staff WHERE username = %s'
    cursor.execute(query, (username))
    # stores the results in a variable
    data = cursor.fetchone()
    # use fetchall() if you are expecting more than 1 data row

    # Check if the airline exist
    query = "SELECT * FROM Airline WHERE name = %s"
    cursor.execute(query, (airline_name))
    airline_exist = cursor.fetchone()

    error = None
    if (data):
        # If the previous query returns data, then user exists
        error = "This user already exists!"
        return render_template('Staff/staff-register.html', error=error)
    elif (not airline_exist):
        error = "The airline you are working for does not exist!"
        return render_template('Staff/staff-register.html', error=error)
    else:
        ins = "INSERT INTO Airline_Staff (username, s_password, first_name, last_name, date_of_birth, airline_name) VALUES (%s, %s, %s, %s, %s, %s)"
        cursor.execute(ins, (username, hashed_password, first_name,
                       last_name, date_of_birth, airline_name))
        conn.commit()

        email_list = email.split(";")
        # insert email
        for i in email_list:
            email_ins = "INSERT INTO Staff_Email (username, email_address) VALUES (%s, %s)"
            cursor.execute(email_ins, (username, i))
            conn.commit()

        phone_list = phone_number.split(";")
        # insert phone number
        for i in phone_list:
            phone_ins = "INSERT INTO Staff_Phone_Number (username, phone_number) VALUES (%s, %s)"
            cursor.execute(phone_ins, (username, i))
            conn.commit()
        cursor.close()
        return render_template('index.html')


@app.route('/staff-main', methods=['GET', 'POST'])
def staff_main():
    username = session['username']
    name = session['name']
    # cursor used to send queries
    cursor = conn.cursor()
    # Get the airline name
    airline_query = "SELECT airline_name FROM Airline_Staff WHERE username = %s"
    cursor.execute(airline_query, (username))
    airline_name = cursor.fetchone()["airline_name"]
    session['airline_name'] = airline_name
    # executes query
    search_query = "SELECT * FROM Flight WHERE airline_name = %s AND departure_date_and_time BETWEEN NOW() AND DATE_ADD(NOW(), INTERVAL 30 DAY)"
    cursor.execute(search_query, (airline_name))
    # stores the results in a variable
    flights = cursor.fetchall()
    cursor.close()
    # If len(flights) == 0, show an optional message.
    error = None
    if len(flights) == 0:
        # no flights
        error = "No flight found for the next 30 days. "
        return render_template('Staff/staff-main.html', name=name, error=error)
    return render_template('Staff/staff-main.html', name=name, flights=flights, error=error)


@app.route('/view-flights', methods=['GET', 'POST'])
def view_flights():
    error = " "
    return render_template('Staff/view-flights.html', error=error)


@app.route('/search_airline_flights', methods=['POST'])
def search_airline_flights():
    # get data from form
    from_date = request.form['from-date']
    to_date = request.form['to-date']
    source_airport = request.form['source-airport']
    destination_airport = request.form['destination-airport']

    # cursor used to send queries
    cursor = conn.cursor()
    # Get airline_name
    airline_name = session['airline_name']

    # executes query
    query = "SELECT * FROM Flight WHERE airline_name = %s"
    argument_list = [airline_name]
    if from_date:
        query += " AND departure_date_and_time >= %s"
        argument_list.append(from_date)
    if to_date:
        query += " AND departure_date_and_time <= %s"
        argument_list.append(to_date)
    if source_airport:
        query += " AND departure_airport_code = %s"
        argument_list.append(source_airport)
    if destination_airport:
        query += " AND arrival_airport_code = %s"
        argument_list.append(destination_airport)
    argument = tuple(argument_list)
    cursor.execute(query, argument)
    # stores the results in a variable
    flights = cursor.fetchall()
    # use fetchall() if you are expecting more than 1 data row
    cursor.close()
    error = None
    if len(flights) == 0:
        # no flights
        error = 'No flights found for the selected criteria.'
        return render_template('Staff/view-flights.html', error=error)
    # Return result
    return render_template('Staff/view-flights.html', error=error, flights=flights)


@app.route('/view_customers', methods=['POST'])
def view_customers():
    flight_number = request.form['flight_number']
    cursor = conn.cursor()
    query = "SELECT DISTINCT Customer.email_address, Customer.first_name, Customer.last_name, Customer.date_of_birth, Customer.passport_number, (SELECT Customer_Phone_Number.phone_number FROM Customer_Phone_Number WHERE Customer_Phone_Number.email_address = Customer.email_address LIMIT 1) as phone_number FROM Customer, Ticket WHERE Customer.email_address = Ticket.email_address and Ticket.flight_number = %s"
    cursor.execute(query, (flight_number))
    customers = cursor.fetchall()
    cursor.close()
    error = None
    if len(customers) == 0:
        error = "There are no customer for this flight. "
        return render_template('Staff/view-customers.html', error=error)
    return render_template('Staff/view-customers.html', error=error, customers=customers)


@app.route('/create-new-flight', methods=['GET', 'POST'])
def create_new_flight():
    return render_template('Staff/new-flight.html')


@app.route('/insertNewFlight', methods=['GET', 'POST'])
def insertNewFlight():
    # verify if the user is actually a airline staff
    verification = session['type']
    if verification != "staff":
        session.clear()
        action = "create a new flight"
        return render_template('no_permission.html', action=action)

    # grabs information from the forms
    flight_number = request.form['flight-number']
    departure_date_and_time = request.form['departure-date-and-time']
    arrival_date_and_time = request.form['arrival-date-and-time']
    base_price_of_ticket = request.form['base-price']
    departure_airport = request.form['departure-airport']
    arrival_airport = request.form['arrival-airport']
    airline_name = session['airline_name']
    identification_number = request.form['identification-number']

    cursor = conn.cursor()

    # check if the flight already exists
    query = "SELECT * FROM Flight WHERE flight_number = %s AND departure_date_and_time = %s AND airline_name = %s"
    cursor.execute(
        query, (flight_number, departure_date_and_time, airline_name))
    flight_exist = cursor.fetchone()

    # check if the airport exists
    query = "SELECT * FROM Airport WHERE code = %s"
    cursor.execute(query, (arrival_airport))
    arrival_airport_exist = cursor.fetchone()
    cursor.execute(query, (departure_airport))
    departure_airport_exist = cursor.fetchone()

    # check if the airplane exists
    query = "SELECT * FROM Airplane WHERE airline_name = %s AND identification_number = %s"
    cursor.execute(query, (airline_name, identification_number))
    airplane_exist = cursor.fetchone()

    error = None
    if (flight_exist):
        error = "This flight already exists!"
        return render_template('Staff/new-flight.html', error=error)
    elif (not (arrival_airport_exist and departure_airport_exist)):
        error = "One or both of the airport doesn't exist!"
        return render_template('Staff/new-flight.html', error=error)
    elif (not airplane_exist):
        error = "The airplane does not exist! "
        return render_template('Staff/new-flight.html', error=error)
    else:
        # insert into both Flight and Fly
        insFlight = "INSERT INTO Flight (airline_name, flight_number, departure_date_and_time, arrival_date_and_time, base_price_of_ticket, arrival_airport_code, departure_airport_code) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        cursor.execute(insFlight, (airline_name, flight_number, departure_date_and_time,
                                   arrival_date_and_time, base_price_of_ticket, arrival_airport, departure_airport))
        conn.commit()
        flight_status = "on time"
        insFly = "INSERT INTO Fly (airline_name, flight_number, departure_date_and_time, identification_number, flight_status) VALUES (%s, %s, %s, %s, %s)"
        cursor.execute(insFly, (airline_name, flight_number,
                       departure_date_and_time, identification_number, flight_status))
        conn.commit()
        cursor.close()
        return redirect(url_for('success'))


@app.route('/success')
def success():
    return render_template('Staff/success.html')


@app.route('/change-status', methods=['GET', 'POST'])
def change_status():
    return render_template('Staff/change-status.html')


@app.route('/toggleStatus', methods=['GET', 'POST'])
def toggleStatus():
    verification = session['type']
    if verification != "staff":
        session.clear()
        action = "change the flight status"
        return render_template('no_permission.html', action=action)

    # grabs information from the forms
    flight_number = request.form['flight-number']
    departure_date_and_time = request.form['departure-date-and-time']
    airline_name = session['airline_name']
    flight_status = request.form['status']
    identification_number = request.form['identification-number']

    cursor = conn.cursor()

    # check if the flight exists
    query = "SELECT * FROM Fly WHERE flight_number = %s AND departure_date_and_time = %s AND airline_name = %s AND identification_number = %s"
    cursor.execute(
        query, (flight_number, departure_date_and_time, airline_name, identification_number))
    flight_exist = cursor.fetchone()

    error = None
    if (not flight_exist):
        error = "This flight does not exist! "
        return render_template('Staff/change-status.html', error=error)
    else:
        # change flight status
        updateQuery = "UPDATE Fly SET flight_status = %s WHERE airline_name = %s AND flight_number = %s AND departure_date_and_time = %s AND identification_number = %s"
        cursor.execute(updateQuery, (flight_status, airline_name,
                                     flight_number, departure_date_and_time, identification_number))
        conn.commit()
        cursor.close()
        return redirect(url_for('success'))


@app.route('/add-airplane', methods=['GET', 'POST'])
def addAirplane():
    return render_template('Staff/add-airplane.html')


@app.route('/insertAirplane', methods=['GET', 'POST'])
def insertAirplane():
    verification = session['type']
    if verification != "staff":
        session.clear()
        action = "add new airplane"
        return render_template('no_permission.html', action=action)

    # grabs information from the forms
    airline_name = session['airline_name']
    identification_number = request.form['identification-number']
    number_of_seats = request.form['number-of-seats']
    manufacturing_company = request.form['manufacturing-company']
    manufacture_date = request.form['manufacture-date']

    cursor = conn.cursor()

    # check if the airplane already exists
    query = "SELECT * FROM Airplane WHERE airline_name = %s AND identification_number = %s"
    cursor.execute(query, (airline_name, identification_number))
    airplane_exist = cursor.fetchone()

    error = None
    if (airplane_exist):
        error = "This airplane already exists!"
        return render_template('Staff/add-airplane.html', error=error)
    else:
        insAirplane = "INSERT INTO Airplane (airline_name, identification_number, number_of_seats, manufacturing_company, manufacturing) VALUES (%s, %s, %s, %s, %s)"
        cursor.execute(insAirplane, (airline_name, identification_number,
                       number_of_seats, manufacturing_company, manufacture_date))
        conn.commit()
        cursor.close()
        return redirect(url_for('displayAirplane'))


@app.route('/displayAirplane')
def displayAirplane():
    airline_name = session['airline_name']
    cursor = conn.cursor()
    # executes query
    search_query = "SELECT * FROM Airplane WHERE airline_name = %s"
    cursor.execute(search_query, (airline_name))
    # stores the results in a variable
    airplanes = cursor.fetchall()
    cursor.close()
    return render_template('Staff/display-all-airplane.html', airline_name=airline_name, airplanes=airplanes)


@app.route('/add-airport', methods=['GET', 'POST'])
def addAirport():
    return render_template('Staff/add-airport.html')


@app.route('/insertAirport', methods=['GET', 'POST'])
def insertAirport():
    verification = session['type']
    if verification != "staff":
        session.clear()
        action = "add new airport"
        return render_template('no_permission.html', action=action)

    # grabs information from the forms
    airport_code = request.form['code']
    airport_name = request.form['name']
    airport_city = request.form['city']
    airport_country = request.form['country']
    airport_type = request.form['type']

    cursor = conn.cursor()

    # check if the airport already exists
    query = "SELECT * FROM Airport WHERE code = %s"
    cursor.execute(query, (airport_code))
    airport_exist = cursor.fetchone()

    error = None
    if (airport_exist):
        error = "This airport already exists!"
        return render_template('Staff/add-airport.html', error=error)
    else:
        insAirport = "INSERT INTO Airport (code, name, city, country, airport_type) VALUES (%s, %s, %s, %s, %s)"
        cursor.execute(insAirport, (airport_code, airport_name,
                       airport_city, airport_country, airport_type))
        conn.commit()
        cursor.close()
        return redirect(url_for('success'))


@app.route('/view-ratings', methods=['GET', 'POST'])
def viewRatings():
    error = " "
    return render_template('Staff/view-ratings.html', error=error)


@app.route('/displayRatings', methods=['POST'])
def displayRatings():
    # get data from form
    airline_name = session['airline_name']
    flight_number = request.form['flight-number']
    departure_date_and_time = request.form['departure-date-and-time']
    datetime_obj = datetime.datetime.fromisoformat(departure_date_and_time)

    cursor = conn.cursor()
    error = None

    # check if the flight already exists
    query = "SELECT * FROM Flight WHERE flight_number = %s AND departure_date_and_time = %s AND airline_name = %s"
    cursor.execute(
        query, (flight_number, departure_date_and_time, airline_name))
    flight_exist = cursor.fetchone()

    if (not flight_exist):
        error = "This flight does not exists!"
        return render_template('Staff/view-ratings.html', error=error)
    if datetime_obj >= datetime.datetime.today():
        error = "This is a future flight, it does not have ratings yet. "
        return render_template('Staff/view-ratings.html', error=error)

    # executes query, the flight shoud be past flight
    query = "SELECT Evaluation.email_address, Evaluation.rate, Evaluation.comment FROM Evaluation WHERE airline_name = %s AND flight_number = %s AND departure_date_and_time = %s"
    cursor.execute(
        query, (airline_name, flight_number, departure_date_and_time))
    # stores the results in a variable
    customers = cursor.fetchall()

    # calculate average rating
    averageQuery = "SELECT AVG(rate) as avg_rating FROM Evaluation WHERE airline_name = %s AND flight_number = %s AND departure_date_and_time = %s"
    cursor.execute(averageQuery, (airline_name,
                   flight_number, departure_date_and_time))
    average_rating = cursor.fetchone()

    cursor.close()
    if len(customers) == 0:
        # no ratings
        error = "This flight does not have any ratings. "
        return render_template('Staff/view-ratings.html', error=error)
    # Return result
    return render_template('Staff/view-ratings.html', customers=customers, average_rating=average_rating, error=error)


@app.route('/view-report', methods=['GET', 'POST'])
def view_report():
    cursor = conn.cursor()
    airline_name = session['airline_name']
    # get total_amount if it exist, else set to 0
    total_amount = request.args.get(
        'total_amount') if request.args.get('total_amount') else 0
    # Get the total number of tickets sold last month
    today = datetime.date.today()
    first_day_of_month = today.replace(day=1)
    last_day_of_previous_month = first_day_of_month - \
        datetime.timedelta(days=1)
    query = "SELECT COUNT(*) as num FROM Ticket JOIN Purchase ON Ticket.ticket_ID = Purchase.ticket_ID WHERE airline_name = %s AND Purchase.purchase_date_and_time BETWEEN %s AND %s"
    cursor.execute(query, (airline_name,
                   last_day_of_previous_month.replace(day=1), last_day_of_previous_month))
    last_month_tickets_sold = cursor.fetchone()['num']

    # Get the total number of tickets sold last year
    query = "SELECT COUNT(*) as num FROM Ticket JOIN Purchase ON Ticket.ticket_ID = Purchase.ticket_ID WHERE airline_name = %s AND YEAR(Purchase.purchase_date_and_time) = YEAR(CURRENT_DATE - INTERVAL 1 YEAR)"
    cursor.execute(query, (airline_name))
    last_year_tickets_sold = cursor.fetchone()['num']

    monthly_tickets_sold = [{'month': month, 'num': 0}
                            for month in range(1, 13)]
    # Get the number of tickets sold each month, retuen by a dict: month, num
    query = "SELECT MONTH(Purchase.purchase_date_and_time) as month, COUNT(*) as num FROM Ticket JOIN Purchase ON Ticket.ticket_ID = Purchase.ticket_ID WHERE airline_name = %s GROUP BY MONTH(Purchase.purchase_date_and_time)"
    cursor.execute(query, (airline_name))
    result = cursor.fetchall()

    for i in monthly_tickets_sold:
        for j in result:
            if j['month'] == i['month']:
                i['num'] = j['num']
                break

    # Get the most frequent customer in the last year,
    query = "SELECT email_address, COUNT(*) as num FROM Ticket JOIN Purchase ON Ticket.ticket_ID = Purchase.ticket_ID WHERE airline_name = %s AND Purchase.purchase_date_and_time BETWEEN DATE_SUB(NOW(), INTERVAL 2 YEAR) AND DATE_SUB(NOW(),INTERVAL 1 YEAR) GROUP BY email_address ORDER BY num DESC LIMIT 1"
    cursor.execute(query, (airline_name))
    most_frequent_customer = cursor.fetchone()

    # Get the total revenue last month
    query = "SELECT SUM(calculated_price_of_ticket) FROM Ticket JOIN Purchase ON Ticket.ticket_ID = Purchase.ticket_ID WHERE airline_name = %s AND Purchase.purchase_date_and_time BETWEEN %s AND %s"
    cursor.execute(query, (airline_name, last_day_of_previous_month.replace(
        day=1), last_day_of_previous_month))
    last_month_revenue = cursor.fetchone()['SUM(calculated_price_of_ticket)']
    if not last_month_revenue:
        last_month_revenue = 0

    # Get the total revenue last year
    query = "SELECT SUM(calculated_price_of_ticket) FROM Ticket JOIN Purchase ON Ticket.ticket_ID = Purchase.ticket_ID WHERE airline_name = %s AND YEAR(Purchase.purchase_date_and_time) = YEAR(CURRENT_DATE - INTERVAL 1 YEAR)"
    cursor.execute(query, (airline_name))
    last_year_revenue = cursor.fetchone()['SUM(calculated_price_of_ticket)']
    if not last_year_revenue:
        last_year_revenue = 0
    cursor.close()

    return render_template('Staff/view-report.html', total_amount=total_amount, last_month_tickets_sold=last_month_tickets_sold, last_year_tickets_sold=last_year_tickets_sold, monthly_tickets_sold=monthly_tickets_sold, most_frequent_customer=most_frequent_customer, last_month_revenue=last_month_revenue, last_year_revenue=last_year_revenue)


@app.route('/ticketReport', methods=['POST'])
def ticket_report():
    cursor = conn.cursor()
    airline_name = session['airline_name']
    # Get the total amount of ticket sales between the specified dates
    start_date = request.form['start-date']
    end_date = request.form['end-date']
    query = "SELECT COUNT(*) AS total FROM Ticket JOIN Purchase ON Ticket.ticket_ID = Purchase.ticket_ID WHERE airline_name=%s AND Purchase.purchase_date_and_time BETWEEN %s AND %s"
    cursor.execute(query, (airline_name, start_date, end_date))
    result = cursor.fetchone()
    total_amount = result['total'] if result['total'] else 0
    return redirect(url_for('view_report', total_amount=total_amount))


@app.route('/view-customer-flight-page', methods=['GET', 'POST'])
def view_customer_flight_page():
    return render_template('Staff/view-customer-flight.html')


@app.route('/viewCustomerFlight', methods=['POST'])
def viewCustomerFlight():
    cursor = conn.cursor()

    customer_email = request.form['email']
    airline_name = session['airline_name']

    # Get all flights taken by the customer on this airline
    query = "SELECT Flight.flight_number, Flight.departure_date_and_time, Flight.arrival_date_and_time, Flight.departure_airport_code, Flight.arrival_airport_code, Ticket.calculated_price_of_ticket FROM Ticket JOIN Flight ON Ticket.flight_number = Flight.flight_number WHERE Ticket.email_address = %s AND Flight.airline_name = %s"
    cursor.execute(query, (customer_email, airline_name))
    flights = cursor.fetchall()

    cursor.close()
    return render_template('Staff/view-customer-flight.html', flights=flights)


app.secret_key = 'some key that you will never guess'
# Run the app on localhost port 5000
# debug = True -> you don't have to restart flask
# for changes to go through, TURN OFF FOR PRODUCTION
if __name__ == "__main__":
    app.run('127.0.0.1', 5000, debug=True)
