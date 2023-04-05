CREATE TABLE Airport (
  code CHAR(3) NOT NULL,
  name VARCHAR(20) NOT NULL,
  city VARCHAR(20) NOT NULL,
  country VARCHAR(20) NOT NULL,
  airport_type VARCHAR(20) NOT NULL,
  PRIMARY KEY (code)
);

CREATE TABLE Airline (
  name VARCHAR(20) NOT NULL,
  PRIMARY KEY (name)
);

CREATE TABLE Airplane (
  airline_name VARCHAR(20) NOT NULL,
  identification_number VARCHAR(6) NOT NULL,
  number_of_seats INT NOT NULL,
  manufacturing_company VARCHAR(20) NOT NULL,
  manufacturing DATE NOT NULL,
  PRIMARY KEY (identification_number,airline_name),
  FOREIGN KEY (airline_name) REFERENCES Airline(name)
);

CREATE TABLE Flight (
  airline_name VARCHAR(20) NOT NULL,
  flight_number VARCHAR(20) NOT NULL,
  departure_date_and_time TIMESTAMP NOT NULL,
  arrival_date_and_time TIMESTAMP NOT NULL,
  base_price_of_ticket NUMERIC(10,2) NOT NULL,
  arrival_airport_code CHAR(3) NOT NULL,
  departure_airport_code CHAR(3) NOT NULL,
  PRIMARY KEY (flight_number,departure_date_and_time),
  FOREIGN KEY (airline_name) REFERENCES Airline(name),
  FOREIGN KEY (arrival_airport_code) REFERENCES Airport(code),
  FOREIGN KEY (departure_airport_code) REFERENCES Airport(code)
);

CREATE TABLE Fly (
  airline_name VARCHAR(20) NOT NULL,
  flight_number VARCHAR(20) NOT NULL,
  departure_date_and_time TIMESTAMP NOT NULL,
  identification_number VARCHAR(6) NOT NULL,
  flight_status VARCHAR(10) NOT NULL,
  PRIMARY KEY (airline_name,flight_number,departure_date_and_time,identification_number),
  FOREIGN KEY (airline_name) REFERENCES Airplane(name),
  FOREIGN KEY (flight_number) REFERENCES Flight(flight_number),
  FOREIGN KEY (departure_date_and_time) REFERENCES Flight(departure_date_and_time),
  FOREIGN KEY (identification_number) REFERENCES Airplane(identification_number)
);


CREATE TABLE Payment_Information (
  card_number VARCHAR(20) NOT NULL,
  card_type VARCHAR(8) NOT NULL,
  name_on_card VARCHAR(20) NOT NULL,
  expiration_date DATE NOT NULL,
  PRIMARY KEY (card_number)
);

CREATE TABLE Customer (
  email_address VARCHAR(20) NOT NULL,
  first_name VARCHAR(20) NOT NULL,
  last_name TIMESTAMP NOT NULL,
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
  email_address VARCHAR(20) NOT NULL,
  phone_number VARCHAR(20) NOT NULL,
  PRIMARY KEY (email_address,phone_number),
  FOREIGN KEY (email_address) REFERENCES Customer(email_address) ON DELETE CASCADE
);

CREATE TABLE Ticket (
  ticket_ID VARCHAR(20) NOT NULL,
  first_name VARCHAR(20) NOT NULL,
  last_name TIMESTAMP NOT NULL,
  date_of_birth DATE NOT NULL,
  calculated_price_of_ticket NUMERIC(10,2) NOT NULL,
  email_address VARCHAR(20) NOT NULL,
  airline_name VARCHAR(20) NOT NULL,
  flight_number VARCHAR(20) NOT NULL,
  departure_date_and_time TIMESTAMP NOT NULL,
  PRIMARY KEY (ticket_ID),
  FOREIGN KEY (email_address) REFERENCES Customer(email_address),
  FOREIGN KEY (airline_name) REFERENCES Flight(airline_name),
  FOREIGN KEY (flight_number) REFERENCES Flight(flight_number),
  FOREIGN KEY (departure_date_and_time) REFERENCES Flight(departure_date_and_time)
);

CREATE TABLE Evaluation (
  email_address VARCHAR(20) NOT NULL,
  airline_name VARCHAR(20) NOT NULL,
  flight_number VARCHAR(20) NOT NULL,
  departure_date_and_time TIMESTAMP NOT NULL,
  rate INT NOT NULL,
  commment VARCHAR(200),
  PRIMARY KEY (email_address,airline_name,flight_number,departure_date_and_time),
  FOREIGN KEY (email_address) REFERENCES Customer(email_address),
  FOREIGN KEY (airline_name) REFERENCES Flight(airline_name),
  FOREIGN KEY (flight_number) REFERENCES Flight(flight_number),
  FOREIGN KEY (departure_date_and_time) REFERENCES Flight(departure_date_and_time)
);

