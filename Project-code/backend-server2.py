# Import Flask Library
from flask import Flask, render_template, request, session, url_for, redirect
import pymysql.cursors
import hashlib

# Initialize the app from Flask
app = Flask(__name__)

# Configure MySQL
conn = pymysql.connect(host='localhost',
                       user='root',
                       password='',
                       db='air_ticket_system',
                       charset='utf8mb4',
                       cursorclass=pymysql.cursors.DictCursor)

# Define a route to hello function


@app.route('/')
def hello():
    return render_template('index.html')


@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')

# Define route for login


@app.route('/Staff/staff-login.html')
def login():
    return render_template('Staff/staff-login.html')

# Define route for register


@app.route('/Staff/staff-register.html')
def register():
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
    error = None
    if (data):
        # If the previous query returns data, then user exists
        error = "This user already exists"
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
    '''
    # cursor used to send queries
    cursor = conn.cursor()
    # executes query
    query = ""
    cursor.execute(query, (username))
    # stores the results in a variable
    flights = cursor.fetchall()
    cursor.close()
    '''
    flights = None
    return render_template('Staff/staff-main.html', name=name, flights=flights)


@app.route('/search_flights', methods=['POST'])
def search_flights():  # Search Flight for index.html
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


app.secret_key = 'some key that you will never guess'
# Run the app on localhost port 5000
# debug = True -> you don't have to restart flask
# for changes to go through, TURN OFF FOR PRODUCTION
if __name__ == "__main__":
    app.run('127.0.0.1', 5000, debug=True)
