CREATE TABLE clients_database(
    id_clent integer primary key ,
    client_name text not null,
    client_phone integer not null,
    client_email text,
    client_city text not null);
    
ALTER TABLE clients_database RENAME TO client_db;
ALTER TABLE client_db RENAME COLUMN client_name TO full_name;
ALTER TABLE client_db ADD COLUMN gender text not null;

INSERT INTO client_db VALUES(1, 'Stas', 0991234567890, 'stas@gmail.com', 'Kherson', 'M');
INSERT INTO client_db VALUES(2, 'Danylo', 0991234567891, 'danylo@gmail.com', 'Kherson', 'M');
INSERT INTO client_db VALUES(3, 'Kate', 0991234567892, 'kate@gmail.com', 'Kherson', 'F');
INSERT INTO client_db VALUES(4, 'Natasha', 0991234567893, 'natasha@gmail.com', 'Odessa', 'F');

UPDATE client_db SET full_name = 'Daniel' WHERE full_name = 'Danylo';
UPDATE client_db SET client_phone = 1234567890 WHERE client_phone = 0991234567891;
DELETE FROM client_db WHERE client_city = 'Odessa';
