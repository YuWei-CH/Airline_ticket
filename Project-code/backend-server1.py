# Import Flask Library
from flask import Flask, render_template, request, session, url_for, redirect
import pymysql.cursors
from datetime import datetime

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

# Define route for login


@app.route('/User/user-login.html')
def login():
    return render_template('User/user-login.html')

# Define route for register


@app.route('/User/user-register.html')
def register():
    return render_template('User/user-register.html')

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
        session['name'] = name
        session['email'] = email
        return redirect(url_for('user_main'))
    else:
        # returns an error message to the html page
        error = 'Invalid login or email'
        return render_template('login.html', error=error)


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
        return render_template('register.html', error=error)
    else:
        ins = "INSERT INTO Customer (email_address,first_name, last_name, c_password, building_number, street_name, apartment_number, city, state, zip_code, phone_number1, phone_number2, passport_number, passport_expiration, passport_country, date_of_birth) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s,%s, %s, %s, %s, %s, %s)"
        cursor.execute(ins, (email, first_name, last_name, password, building_number, street_name, apartment_number, city,
                             state, zip_code, phone_number1, phone_number2, passport_number, passport_expiration, passport_country, date_of_birth))
        conn.commit()
        cursor.close()
        return render_template('index.html')


'''
@app.route('/logout')
def logout():
    session.pop('username')
    return redirect('/')
'''


@app.route('/user-main', methods=['GET', 'POST'])
def user_main():
    username = session['name']
    email = session['email']
    # cursor used to send queries
    cursor = conn.cursor()
    # executes query
    query = 'SELECT * FROM Ticket JOIN Flight WHERE email_address = %s AND Ticket.flight_number = Flight.flight_number'
    cursor.execute(query, (email))
    # stores the results in a variable
    flights = cursor.fetchall()
    return render_template('User/user-main.html', username=username, flights=flights)


@app.route('/user-flight-booking.html', methods=['GET', 'POST'])
def get_user_ticket():
    # temp data
    flights = [
        {'flight_number': 'CA123', 'departure_date': '2023-05-01',
         'arrival_date': '2023-05-01', 'departure_airport': 'PEK', 'arrival_airport': 'JFK'},
        {'flight_number': 'MU456', 'departure_date': '2023-05-01',
         'arrival_date': '2023-05-01', 'departure_airport': 'SHA', 'arrival_airport': 'LAX'},
        {'flight_number': 'CZ789', 'departure_date': '2023-05-02',
         'arrival_date': '2023-05-02', 'departure_airport': 'CAN', 'arrival_airport': 'SFO'}
    ]
    return render_template('User/user-flight-booking.html', flights=flights)


app.secret_key = 'some key that you will never guess'
# Run the app on localhost port 5000
# debug = True -> you don't have to restart flask
# for changes to go through, TURN OFF FOR PRODUCTION
if __name__ == "__main__":
    app.run('127.0.0.1', 5000, debug=True)
