# Import Flask Library
from flask import Flask, render_template, request, session, url_for, redirect
import pymysql.cursors
import datetime
import calendar

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


# Define a route to hello function
@app.route('/')
def hello():
    return render_template('index.html')

# Define logout


@app.route('/logout')
def logout():
    session.pop('username')
    session.pop('email')
    return redirect('/')


# Define route for login


@app.route('/User/user-login.html')
def login():
    return render_template('User/user-login.html')

# Define route for register


@app.route('/User/user-register.html')
def register():
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
    # executes query
    query = "SELECT * FROM Flight WHERE airline_name=%s OR flight_number=%s OR departure_date_and_time=%s OR arrival_date_and_time=%s OR arrival_airport_code=%s OR departure_airport_code=%s"
    cursor.execute(query, (airline_name, flight_number, departure_date_and_time,
                   arrival_date_and_time, arrival_airport_code, departure_airport_code))
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
def loginAuth():
    # grabs information from the forms
    email = request.form['email']
    password = request.form['password']

    # cursor used to send queries
    cursor = conn.cursor()
    # executes query
    query = 'SELECT * FROM Customer WHERE email_address = %s and c_password = %s'
    cursor.execute(query, (email, password))
    # stores the results in a variable
    data = cursor.fetchone()
    # use fetchall() if you are expecting more than 1 data row
    # search name
    name_query = 'SELECT first_name FROM Customer WHERE email_address = %s and c_password = %s'
    cursor.execute(name_query, (email, password))
    # stores the results in a variable
    name = cursor.fetchone()
    cursor.close()
    error = None
    if (data):
        # creates a session for the the user
        # session is a built in
        session['username'] = name
        session['email'] = email
        return redirect(url_for('user_main'))
    else:
        # returns an error message to the html page
        error = 'Invalid login or email'
        return render_template('User/user-login.html', error=error)


# Authenticates the register
@app.route('/registerAuth', methods=['GET', 'POST'])
def registerAuth():
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
        phone_number1 = request.form['phone_number1']
        phone_number2 = request.form['phone_number2']
        passport_number = request.form['passport_number']
        passport_expiration = request.form['passport_expiration']
        passport_country = request.form['passport_country']
        date_of_birth = request.form['date_of_birth']

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
        ins = "INSERT INTO Customer (email_address,first_name, last_name, c_password, building_number, street_name, apartment_number, city, state, zip_code, phone_number1, phone_number2, passport_number, passport_expiration, passport_country, date_of_birth) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s,%s, %s, %s, %s, %s, %s)"
        cursor.execute(ins, (email, first_name, last_name, password, building_number, street_name, apartment_number, city,
                             state, zip_code, phone_number1, phone_number2, passport_number, passport_expiration, passport_country, date_of_birth))
        conn.commit()
        cursor.close()
        return render_template('index.html')


@app.route('/user-main', methods=['GET', 'POST'])
def user_main():
    username = session['username']
    email = session['email']
    # cursor used to send queries
    cursor = conn.cursor()
    # executes query
    query = "SELECT * FROM (SELECT f.airline_name, f.departure_date_and_time, f.arrival_date_and_time, f.arrival_airport_code, f.departure_airport_code, f.flight_number FROM Ticket t JOIN Flight f ON f.flight_number=t.flight_number WHERE email_address= %s) AS derived_table_alias WHERE (derived_table_alias.departure_date_and_time > NOW()  AND derived_table_alias.arrival_date_and_time > NOW());"
    cursor.execute(query, (email))
    # stores the results in a variable
    flights = cursor.fetchall()
    cursor.close()
    return render_template('User/user-main.html', username=username, flights=flights)


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
    query = "SELECT * FROM (SELECT f.airline_name, f.departure_date_and_time, f.arrival_date_and_time, f.arrival_airport_code, f.departure_airport_code, f.flight_number FROM Ticket t JOIN Flight f ON f.flight_number=t.flight_number WHERE email_address= %s) AS derived_table_alias WHERE arrival_date_and_time < NOW();"
    cursor.execute(query, (email))
    # stores the results in a variable
    flights = cursor.fetchall()
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
    current_month = now.month
    current_year = now.year

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
    date_ranges = [(now - datetime.timedelta(days=30*i+29),
                    now - datetime.timedelta(days=30*i)) for i in range(6)]
    monthly_spending = {}
    for date_range in date_ranges:
        start_date = date_range[0].strftime('%Y-%m-%d 00:00:00')
        end_date = date_range[1].strftime('%Y-%m-%d 23:59:59')
        # print(start_date, end_date)
        query = "SELECT SUM(t.calculated_price_of_ticket) FROM Ticket t JOIN Purchase p ON t.ticket_ID = p.ticket_ID WHERE t.email_address = %s AND p.purchase_date_and_time BETWEEN %s AND %s;"
        cursor.execute(query, (email, start_date, end_date))
        monthly_spend = cursor.fetchone()['SUM(t.calculated_price_of_ticket)']
        # print(monthly_spend)
        if monthly_spend is None:
            monthly_spend = 0
        month_year = date_range[0].strftime('%B %Y')
        monthly_spending[month_year] = monthly_spend
    if 'specific_monthly_spending' in session:
        specific_monthly_spending = session['specific_monthly_spending']
    else:
        specific_monthly_spending = None

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
    # executes query
    # executes query
    query = "SELECT * FROM (SELECT f.airline_name, f.departure_date_and_time, f.arrival_date_and_time, f.arrival_airport_code, f.departure_airport_code, f.flight_number FROM Ticket t JOIN Flight f ON f.flight_number = t.flight_number WHERE email_address = %s) AS derived_table_alias WHERE derived_table_alias.flight_number = %s OR derived_table_alias.departure_date_and_time = %s OR derived_table_alias.arrival_date_and_time = %s OR derived_table_alias.arrival_airport_code = %s OR derived_table_alias.departure_airport_code = %s"
    cursor.execute(query, (email, flight_number, departure_date_and_time,
                   arrival_date_and_time, arrival_airport_code, departure_airport_code))
    # stores the results in a variable
    flights = cursor.fetchall()
    # use fetchall() if you are expecting more than 1 data row
    cursor.close()
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
    airline_name = request.form['airline_name']
    flight_number = request.form['flight_number']
    departure_date_and_time = request.form['departure_date_and_time']
    arrival_date_and_time = request.form['arrival_date_and_time']
    arrival_airport_code = request.form['arrival_airport_code']
    departure_airport_code = request.form['departure_airport_code']

    # cursor used to send queries
    cursor = conn.cursor()
    # executes query
    query = "SELECT * FROM Flight WHERE (departure_date_and_time>NOW() AND arrival_date_and_time>NOW()) AND (airline_name=%s OR flight_number=%s OR departure_date_and_time=%s  OR arrival_date_and_time=%s OR arrival_airport_code=%s OR departure_airport_code=%s)"
    cursor.execute(query, (airline_name, flight_number, departure_date_and_time,
                   arrival_date_and_time, arrival_airport_code, departure_airport_code))
    # stores the results in a variable
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
    if purchase_ratio > 0.8:
        calculated_price_of_ticket = base_price*1.2
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
    rate = request.form['rating']
    comment = request.form['comment']

    # cursor used to send queries
    cursor = conn.cursor()
    # executes query
    query = "INSERT INTO Evaluation (email_address,airline_name,flight_number,departure_date_and_time,rate,comment) VALUES (%s,%s,%s,%s,%s,%s);"
    cursor.execute(query, (email, airline_name, flight_number,
                   departure_date_and_time, rate, comment))
    # use fetchall() if you are expecting more than 1 data row
    conn.commit()
    cursor.close()
    # Return result
    return render_template('User/user-rate-result.html')

# track user spend specifically


@app.route('/track-specific-spend', methods=['POST'])
def track_specific_spend():
    cursor = conn.cursor()
    email = session['email']
    start_date = request.form['start-date']
    end_date = request.form['end-date']

    # get monthly spending
    start_year, start_month, _ = start_date.split('-')
    end_year, end_month, _ = end_date.split('-')
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
        last_day = calendar.monthrange(int(year), month)[1]
        start_time = "00:00:00"
        end_time = "23:59:59"
        date_range = (f"{year}-{month:02}-01 {start_time}",
                      f"{year}-{month:02}-{last_day} {end_time}")
        query = "SELECT SUM(t.calculated_price_of_ticket) FROM Ticket t JOIN Purchase p ON t.ticket_ID = p.ticket_ID WHERE t.email_address = %s AND p.purchase_date_and_time BETWEEN %s AND %s;"
        cursor.execute(query, (email, date_range[0], date_range[1]))
        monthly_spend = cursor.fetchone()['SUM(t.calculated_price_of_ticket)']
        if monthly_spend is None:
            monthly_spend = 0
        month_year = f"{calendar.month_name[month]} {year}"
        specific_monthly_spending[month_year] = monthly_spend
        session['specific_monthly_spending'] = specific_monthly_spending
    cursor.close()
    # send data back
    return redirect(url_for('track_spending'))


app.secret_key = 'some key that you will never guess'
# Run the app on localhost port 5000
# debug = True -> you don't have to restart flask
# for changes to go through, TURN OFF FOR PRODUCTION
if __name__ == "__main__":
    app.run('127.0.0.1', 5000, debug=True)
