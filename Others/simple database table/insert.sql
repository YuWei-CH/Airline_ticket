INSERT INTO Airline VALUES ('Jet Blue');

INSERT INTO Airport VALUES ('JFK', 'John F. Kennedy International Airport', 'New York City', 'USA','Both');
INSERT INTO Airport VALUES ('PVG','Shanghai Pudong International Airport', 'Shanghai', 'China','Both');

INSERT INTO Customer VALUES ('ys4680@nyu.edu', 'Yuwei', 'Sun', 'mypassword', 370, 'Jay St', 'Apt# 1109', 'Brooklyn', 'NY', 11201, 'CH1234567', DATE('2028-04-06'), 'China', DATE('2002-12-26'));
INSERT INTO Customer VALUES ('yw5490@nyu.edu', 'Yirong', 'Wang', 'mypassword', 370, 'Jay St', 'Apt# 2210', 'Brooklyn', 'NY', 11201, 'CH9876543', DATE('2029-04-05'), 'China', DATE('2003-03-25'));
INSERT INTO Customer VALUES ('elonmusk@yahoo.com', 'Elon', 'Musk', 'elonpassword', 1, 'Rocket Rd', NULL, 'Hawthorne', 'CA', 90250, 'US1234567', DATE('2030-09-01'), 'US', DATE('1971-06-28'));
INSERT INTO Customer_Phone_Number VALUES('ys4680@nyu.edu', '+1-347-123-4567');
INSERT INTO Customer_Phone_Number VALUES('ys4680@nyu.edu', '+1-347-456-7890');
INSERT INTO Customer_Phone_Number VALUES('yw5490@nyu.edu', '+1-123-520-1234');
INSERT INTO Customer_Phone_Number VALUES('elonmusk@yahoo.com', '+1-000-111-2345');

INSERT INTO Airplane VALUES ('Jet Blue', 'N123JB', 150, 'Airbus', DATE('2020-01-01'));
INSERT INTO Airplane VALUES ('Jet Blue', 'N345JB', 75, 'COMAC', DATE('2023-01-01'));
INSERT INTO Airplane VALUES ('Jet Blue', 'N789JB', 150, 'Boeing', DATE('2022-01-01'));

INSERT INTO Airline_Staff VALUES ('jbdl1', 'mypassword', 'David', 'Lee', DATE('2002-12-27'), 'Jet Blue');
INSERT INTO Staff_Email VALUES ('jbdl1', 'davidlee@jetblue.com');
INSERT INTO Staff_Phone_Number VALUES ('jbdl1', '+1-111-222-3333');

INSERT INTO Flight VALUES ('Jet Blue', 'JB23040601', '2023-04-06 10:30:00', '2023-04-06 22:30:00', 175.43, 'PVG', 'JFK');
INSERT INTO Flight VALUES ('Jet Blue', 'JB23040602', '2023-04-06 11:30:00', '2023-04-07 11:30:00', 345.43, 'PVG', 'JFK');
INSERT INTO Flight VALUES ('Jet Blue', 'JB23040603', '2023-05-06 10:00:00', '2023-05-06 22:30:00', 180.00, 'PVG', 'JFK');
INSERT INTO Fly VALUES ('Jet Blue', 'JB23040601', '2023-04-06 10:30:00', 'N123JB', 'on time');
INSERT INTO Fly VALUES ('Jet Blue', 'JB23040602', '2023-04-06 11:30:00', 'N345JB', 'delay');
INSERT INTO Fly VALUES ('Jet Blue', 'JB23040603', '2023-05-06 10:00:00', 'N789JB', 'on time');

INSERT INTO Payment_Information VALUES ('1234123412341234', 'debit', 'Yuwei Sun', DATE('2028-05-01'));
INSERT INTO Payment_Information VALUES ('5678567856785678', 'credit', 'Yirong Wang', DATE('2028-06-01'));
INSERT INTO Ticket VALUES (1, 'Yuwei', 'Sun', DATE('2002-12-26'), 200.00, 'Jet Blue', 'JB23040601', '2023-04-06 10:30:00', 'ys4680@nyu.edu');
INSERT INTO Ticket VALUES (2, 'Yirong', 'Wang', DATE('2003-03-25'), 210.00, 'Jet Blue', 'JB23040601', '2023-04-06 10:30:00', 'yw5490@nyu.edu');
INSERT INTO Ticket VALUES (3, 'David', 'Lee', DATE('2002-12-27'), 205.00, 'Jet Blue', 'JB23040601', '2023-04-06 10:30:00', 'yw5490@nyu.edu');
INSERT INTO Purchase VALUES (1, '1234123412341234', '2023-04-06 09:30:00');
INSERT INTO Purchase VALUES (2, '5678567856785678', '2023-04-06 09:30:00');
