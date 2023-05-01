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
                       db='blog',
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


@app.route('/loginAuth', methods=['GET', 'POST'])
def loginAuth():
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
    # stores the results in a variable
    name = cursor.fetchone()
    cursor.close()
    error = None
    if (data):
        # creates a session for the the user
        # session is a built in
        session['username'] = username
        return redirect(url_for('staff_main'))
    else:
        # returns an error message to the html page
        error = 'Invalid login or email'
        return render_template('Staff/staff-login.html', error=error)


# Authenticates the register
@app.route('/registerAuth', methods=['GET', 'POST'])
def registerAuth():
    if request.method == 'POST':
        # grabs information from the forms
        username = request.form['username']
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        password = request.form['password']
        email1 = request.form['email1']
        email2 = request.form['email2']
        phone_number1 = request.form['phone_number1']
        phone_number2 = request.form['phone_number2']
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
        ins = "INSERT INTO Airline_Staff (username, s_password, first_name, last_name, date_of_birth, airline_name) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s,%s, %s, %s, %s, %s, %s)"
        cursor.execute(ins, (username, first_name, last_name, hashed_password, building_number, street_name, apartment_number, city,
                             state, zip_code, phone_number1, phone_number2, passport_number, passport_expiration, passport_country, date_of_birth))
        conn.commit()
        cursor.close()
        return render_template('index.html')


app.secret_key = 'some key that you will never guess'
# Run the app on localhost port 5000
# debug = True -> you don't have to restart flask
# for changes to go through, TURN OFF FOR PRODUCTION
if __name__ == "__main__":
    app.run('127.0.0.1', 5000, debug=True)
