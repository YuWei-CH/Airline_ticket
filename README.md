# Air Ticket Reservation System

There will be two types of
users of this system – Customers, and Airline Staff (Administrator). Using this system, customers can
search for flights (one way or round trip), purchase flights ticket, view their future flight status or see
their past flights etc. Airline Staff will add new airplanes, create new flights, and update flight status. In
general, this will be a simple air ticket reservation system. 

## Instruction for this project
1. If it is through direct download or clone this repository can be used directly after. If it is downloaded by zip, you need to **decompress** it and use it again.   
2. The runnable part of the file is stored in the "Project-code" folder. This folder contains static and templates folders and backend-server.py, a python file.   
3. If you have deployed **python 3.7** or above, you can read the next step directly, if not, please download and install python runtime environment according to your operating system type. 
5. Install flask and pymysql modules in python if required.   
6. Start your mysql database server and your apache server.   
7. Go to your browser and type **"127.0.0.1"** in the address bar and click on phyMyAdmin.   
8. Open your database. Please remember the name of your database. 
9. If you used a root password for your mysql database, edit the backend-server.py file to
  write that password in and **change the "db" to your database name**.
  ```python
  conn = pymysql.connect(host='localhost',
		                   port = 8889,
                       user='root',
                       password='root',
                       db='your_database_name',
                       charset='utf8mb4',
                       cursorclass=pymysql.cursors.DictCursor) line.
 ```   
9. Now create another tab in your browser, type **"127.0.0.1:5000"** in the address bar.
You should be able to see a main page. And your can start.   

### Structure of project
- In *Project-code*
1. static folder: all the static resources file, such as style.css.  
2. templates folder: all .html template file. It has 2 folderes: Staff, User and a index.html.  
3. backend-server.py which can be be execute.   
- In *Others* which contain part1 and part2 work

#### detailed structure
index.html: Home page, allowing customers and employees to register for login. It also allows to view future flights.   
no_permission.html: If the user performs some unauthorized operation, he will be returned to this page.  

Static:
- style.css: contain all style formant.    

Staff folder:    
- add-airplane.html: enable staff add plane.    
- add-airpoet.html: enable staff add airport.     
- change-status.html: allow staff change the status of a plane.    
- display-all-airplane.html: show all current airplane for this airline.   
- new-flight.html: add new flight.   
- staff-login.html: enable staff login system.        
- staff-register.html: register staff.   
- success.html: show a success result for some insertion and query.  
- view-customer-flight.html: view flight data for a specific customer.  
- view-customers.html: after click, staff can view this customer.  
- view-flights.html: view public flight.  
- view-ratings.html: view rating and comments for all or specific flights in this airline.  
     
User folder:    
- user-flight-booking.html: allow user search and book flight through some specific conditions.   
- user-login.html: allow user to login.   
- user-main.html: show personal flight information for this user.   
- user-payment.html: record customer's payment information.   
- user-purchase-result.html: display successful or error when costumer purchase a flight.    
- user-rate-result.html: display successful or error when costumer rate a previous flight.    
- user-register.html: customer register.    
- user-spend.html: show this customer spending for past year, past 6 months and a specific range of date.   
- user-track.html: show all flights for this customer. Also, customer can rate and write comment for a previous flight.    

Backend: backend-server.py which can be be execute.    
