-- CREATE TABLE Users (
--   user_id SERIAL PRIMARY KEY,
--   username VARCHAR(255),
--   email VARCHAR(255),
--   password VARCHAR(255),
--   user_type VARCHAR(50)
-- );

-- CREATE TABLE Hosts (
--   host_id SERIAL PRIMARY KEY,
--   user_id INT,
--   rate INT,
--   FOREIGN KEY (user_id) REFERENCES Users(user_id)
-- );

-- CREATE TABLE Guests (
--   guest_id SERIAL PRIMARY KEY,
--   user_id INT,
--   FOREIGN KEY (user_id) REFERENCES Users(user_id)
-- );

-- CREATE TABLE Rooms (
--   room_id SERIAL PRIMARY KEY,
--   host_id INT,
--   room_name VARCHAR(255),
--   description TEXT,
--   maximum_residents INT,
--   price_per_night INT,
--   review VARCHAR(255),
--   FOREIGN KEY (host_id) REFERENCES Hosts(host_id)
-- );

-- CREATE TABLE Reservations (
--   reservation_id SERIAL PRIMARY KEY,
--   guest_id INT,
--   room_id INT,
--   check_in_date DATE,
--   check_out_date DATE,
--   total_price INT,
--   payment VARCHAR(255),
--   FOREIGN KEY (guest_id) REFERENCES Guests(guest_id),
--   FOREIGN KEY (room_id) REFERENCES Rooms(room_id)
-- );

INSERT INTO Users (user_id, username, email, password, user_type)
VALUES
  (1, 'user1', 'user1@example.com', 'password1', 'guest'),
  (2, 'user2', 'user2@example.com', 'password2', 'host'),
  (3, 'user3', 'user3@example.com', 'password3', 'host'),
  (4, 'user4', 'user3@example.com', 'password3', 'host'),
  (5, 'user5', 'user1@example.com', 'password1', 'guest'),
  (6, 'user6', 'user1@example.com', 'password1', 'guest');

INSERT INTO Hosts (host_id, user_id, rate)
VALUES
  (1, 1, 4),
  (2, 4, 5),
  (3, 5, 4);

INSERT INTO Guests (user_id, guest_id)
VALUES
  (1, 1),
  (3, 3),
  (6, 6);

INSERT INTO Rooms (room_id, host_id, room_name, description, maximum_residents, price_per_night, review)
VALUES
  (1, 1, 'Cozy Cabin', 'A rustic cabin in the woods', 2, 100, 'Great place to relax'),
  (2, 2, 'Beachfront Villa', 'Luxurious beachfront property', 6, 300, 'Breathtaking views'),
  (3, 3, 'Downtown Apartment', 'City center convenience', 4, 150, 'Close to everything');

INSERT INTO Reservations (guest_id, room_id, check_in_date, check_out_date, total_price, payment)
VALUES
  (1, 1, '2023-10-01', '2023-10-05', 400, 'Credit Card'),
  (3, 2, '2023-09-15', '2023-09-20', 1500, 'PayPal'),
  (6, 3, '2023-11-01', '2023-11-05', 600, 'Credit Card');

SELECT U.username, U.user_id
FROM Users U
JOIN Guests G ON U.user_id = G.user_id
JOIN Reservations R ON G.guest_id = R.guest_id
GROUP BY U.username, U.user_id
ORDER BY COUNT(R.reservation_id) DESC
LIMIT 1;