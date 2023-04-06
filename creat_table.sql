CREATE TABLE Airport (
  code CHAR(3),
  name VARCHAR(200) NOT NULL,
  city VARCHAR(20) NOT NULL,
  country VARCHAR(20) NOT NULL,
  airport_type VARCHAR(20) NOT NULL,
  PRIMARY KEY (code)
);

CREATE TABLE Airline (
  name VARCHAR(20),
  PRIMARY KEY (name)
);

CREATE TABLE Airplane (
  airline_name VARCHAR(20),
  identification_number VARCHAR(6),
  number_of_seats INT NOT NULL,
  manufacturing_company VARCHAR(20) NOT NULL,
  manufacturing DATE NOT NULL,
  PRIMARY KEY (identification_number, airline_name),
  FOREIGN KEY (airline_name) REFERENCES Airline(name)
);

CREATE TABLE Flight (
  airline_name VARCHAR(20),
  flight_number VARCHAR(20),
  departure_date_and_time TIMESTAMP,
  arrival_date_and_time TIMESTAMP NOT NULL,
  base_price_of_ticket NUMERIC(10,2) NOT NULL,
  arrival_airport_code CHAR(3) NOT NULL,
  departure_airport_code CHAR(3) NOT NULL,
  PRIMARY KEY (airline_name, flight_number, departure_date_and_time),
  FOREIGN KEY (airline_name) REFERENCES Airline(name),
  FOREIGN KEY (arrival_airport_code) REFERENCES Airport(code),
  FOREIGN KEY (departure_airport_code) REFERENCES Airport(code)
);

CREATE TABLE Fly (
  airline_name VARCHAR(20),
  flight_number VARCHAR(20),
  departure_date_and_time TIMESTAMP,
  identification_number VARCHAR(6),
  flight_status VARCHAR(10) NOT NULL,
  PRIMARY KEY (airline_name, flight_number, departure_date_and_time, identification_number),
  FOREIGN KEY (airline_name, flight_number, departure_date_and_time) REFERENCES Flight(airline_name, flight_number, departure_date_and_time),
  FOREIGN KEY (airline_name, identification_number) REFERENCES Airplane(airline_name, identification_number)
);


CREATE TABLE Payment_Information (
  card_number VARCHAR(20),
  card_type VARCHAR(8) NOT NULL,
  name_on_card VARCHAR(20) NOT NULL,
  expiration_date DATE NOT NULL,
  PRIMARY KEY (card_number)
);

CREATE TABLE Customer (
  email_address VARCHAR(30),
  first_name VARCHAR(20) NOT NULL,
  last_name VARCHAR(20) NOT NULL,
  c_password VARCHAR(255) NOT NULL,
  building_number INT NOT NULL,
  street_name VARCHAR(20) NOT NULL,
  apartment_number VARCHAR(10),
  city VARCHAR(20) NOT NULL,
  state VARCHAR(3) NOT NULL,
  zip_code INT NOT NULL,
  passport_number VARCHAR(9) NOT NULL,
  passport_expiration DATE NOT NULL,
  passport_country VARCHAR(10) NOT NULL,
  date_of_birth DATE NOT NULL,
  PRIMARY KEY (email_address)
);

CREATE TABLE Customer_Phone_Number (
  email_address VARCHAR(50),
  phone_number VARCHAR(20),
  PRIMARY KEY (email_address, phone_number),
  FOREIGN KEY (email_address) REFERENCES Customer(email_address) ON DELETE CASCADE
);

CREATE TABLE Ticket (
  ticket_ID VARCHAR(20),
  first_name VARCHAR(20) NOT NULL,
  last_name VARCHAR(20) NOT NULL,
  date_of_birth DATE NOT NULL,
  calculated_price_of_ticket NUMERIC(10,2) NOT NULL,
  airline_name VARCHAR(20) NOT NULL,
  flight_number VARCHAR(20) NOT NULL,
  departure_date_and_time TIMESTAMP NOT NULL,
  email_address VARCHAR(50) NOT NULL,
  PRIMARY KEY (ticket_ID),
  FOREIGN KEY (email_address) REFERENCES Customer(email_address),
  FOREIGN KEY (airline_name, flight_number, departure_date_and_time) REFERENCES Flight(airline_name, flight_number, departure_date_and_time)
);

CREATE TABLE Evaluation (
  email_address VARCHAR(20),
  airline_name VARCHAR(20),
  flight_number VARCHAR(20),
  departure_date_and_time TIMESTAMP,
  rate INT NOT NULL,
  comment VARCHAR(200),
  PRIMARY KEY (email_address, airline_name, flight_number, departure_date_and_time),
  FOREIGN KEY (email_address) REFERENCES Customer(email_address),
  FOREIGN KEY (airline_name, flight_number, departure_date_and_time) REFERENCES Flight(airline_name, flight_number, departure_date_and_time)
);

CREATE TABLE Airline_Staff (
  username VARCHAR(20),
  s_password VARCHAR(255) NOT NULL, 
  first_name VARCHAR(20) NOT NULL,
  last_name VARCHAR(20) NOT NULL,
  date_of_birth DATE NOT NULL,
  airline_name VARCHAR(20) NOT NULL, 
  PRIMARY KEY (username), 
  FOREIGN KEY (airline_name) REFERENCES Airline(name)
);

CREATE TABLE Staff_Email (
  username VARCHAR(20), 
  email_address VARCHAR(50),
  PRIMARY KEY (username, email_address), 
  FOREIGN KEY (username) REFERENCES Airline_Staff(username) ON DELETE CASCADE
);

CREATE TABLE Staff_Phone_Number (
  username VARCHAR(20), 
  phone_number VARCHAR(20),
  PRIMARY KEY (username, phone_number), 
  FOREIGN KEY (username) REFERENCES Airline_Staff(username) ON DELETE CASCADE
);

CREATE TABLE Purchase (
  ticket_ID VARCHAR(20),
  card_number VARCHAR(20),
  purchase_date_and_time TIMESTAMP NOT NULL,
  PRIMARY KEY (ticket_ID, card_number),
  FOREIGN KEY (ticket_ID) REFERENCES Ticket(ticket_ID),
  FOREIGN KEY (card_number) REFERENCES Payment_Information(card_number)
);