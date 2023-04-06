-- 1. Show all the future flights in the system.
SELECT * 
FROM Flight
WHERE departure_date_and_time > NOW();

/*
Result:
('Jet Blue', 'JB23040603', '2023-05-06 10:00:00', '2023-05-06 22:30:00', 180.00, 'PVG', 'JFK')
*/


-- 2. Show all of the delayed flights in the system.
SELECT flight.airline_name, flight.flight_number, flight.departure_date_and_time, flight.arrival_date_and_time, flight.base_price_of_ticket, flight.arrival_airport_code, flight.departure_airport_code
FROM Flight NATURAL JOIN Fly
WHERE Fly.flight_status = 'delay';

/*
Result:
('Jet Blue', 'JB23040602', '2023-04-06 11:30:00', '2023-04-07 11:30:00', 345.43, 'PVG', 'JFK')
*/


-- 3. Show the customer names who bought the tickets.
SELECT DISTINCT Customer.first_name, Customer.last_name
FROM Customer NATURAL JOIN Ticket

/*
Result:
('Yuwei', 'Sun'), 
('Yirong', 'Wang')
*/


-- 4. Show all the airplanes owned by the airline Jet Blue.
SELECT *
FROM Airplane
WHERE Airplane.airline_name = 'Jet Blue';

/*
Result:
('Jet Blue', 'N123JB', 150, 'Airbus', DATE('2020-01-01')), 
('Jet Blue', 'N345JB', 75, 'COMAC', DATE('2023-01-01')),
('Jet Blue', 'N789JB', 150, 'Boeing', DATE('2022-01-01'))
*/