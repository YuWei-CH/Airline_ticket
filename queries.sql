-- Show all the future flights in the system.
SELECT * 
FROM Flight
WHERE Flight.departure_date_and_time > NOW();

-- Show all of the delayed flights in the system.
SELECT * 
FROM Flight NATURAL JOIN Fly
WHERE Fly.flight_status = 'delay';

-- Show the customer names who bought the tickets.
