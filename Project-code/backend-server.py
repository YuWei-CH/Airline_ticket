# Import Flask Library
from flask import Flask, render_template, request, session, url_for, redirect
import pymysql.cursors

# Initialize the app from Flask
app = Flask(__name__)

# Configure MySQL
conn = pymysql.connect(host='localhost',
                       port=8889,
                       user='root',
                       password='root',
                       db='blog',
                       charset='utf8mb4',
                       cursorclass=pymysql.cursors.DictCursor)

# Define a route to hello function


@app.route('/')
def hello():
    return render_template('index.html')

# Define route for login


@app.route('/login')
def login():
    return render_template('login.html')

# Define route for register


@app.route('/register')
def register():
    return render_template('register.html')

# Authenticates the login


@app.route('/loginAuth', methods=['GET', 'POST'])
def loginAuth():
    # grabs information from the forms
    username = request.form['username']
    password = request.form['password']

    # cursor used to send queries
    cursor = conn.cursor()
    # executes query
    query = 'SELECT * FROM user WHERE username = %s and password = %s'
    cursor.execute(query, (username, password))
    # stores the results in a variable
    data = cursor.fetchone()
    # use fetchall() if you are expecting more than 1 data row
    cursor.close()
    error = None
    if (data):
        # creates a session for the the user
        # session is a built in
        session['username'] = username
        return redirect(url_for('home'))
    else:
        # returns an error message to the html page
        error = 'Invalid login or username'
        return render_template('login.html', error=error)

# Authenticates the register


@app.route('/registerAuth', methods=['GET', 'POST'])
def registerAuth():
    # grabs information from the forms
    username = request.form['username']
    password = request.form['password']

    # cursor used to send queries
    cursor = conn.cursor()
    # executes query
    query = 'SELECT * FROM user WHERE username = %s'
    cursor.execute(query, (username))
    # stores the results in a variable
    data = cursor.fetchone()
    # use fetchall() if you are expecting more than 1 data row
    error = None
    if (data):
        # If the previous query returns data, then user exists
        error = "This user already exists"
        return render_template('register.html', error=error)
    else:
        ins = 'INSERT INTO user VALUES(%s, %s)'
        cursor.execute(ins, (username, password))
        conn.commit()
        cursor.close()
        return render_template('index.html')


@app.route('/user-main.html', methods=['GET', 'POST'])
def get_future_ticket():
    # temp data
    flights = [
        {'flight_number': 'CA123', 'departure_date': '2023-05-01',
         'arrival_date': '2023-05-01', 'departure_airport': 'PEK', 'arrival_airport': 'JFK'},
        {'flight_number': 'MU456', 'departure_date': '2023-05-01',
         'arrival_date': '2023-05-01', 'departure_airport': 'SHA', 'arrival_airport': 'LAX'},
        {'flight_number': 'CZ789', 'departure_date': '2023-05-02',
         'arrival_date': '2023-05-02', 'departure_airport': 'CAN', 'arrival_airport': 'SFO'}
    ]
    return render_template('user-main.html', flights=flights)


@app.route('/logout')
def logout():
    session.pop('username')
    return redirect('/')


app.secret_key = 'some key that you will never guess'
# Run the app on localhost port 5000
# debug = True -> you don't have to restart flask
# for changes to go through, TURN OFF FOR PRODUCTION
if __name__ == "__main__":
    app.run('127.0.0.1', 5000, debug=True)
