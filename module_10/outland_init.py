    # Title: Outlander Init Script
    # Authors: 	Chris Beatty
	# 			Brian Gossett
	# 			Larissa Passamani Lima
	# 			Christeen Safar
	# 			Michele Speidel

    # Date: 7 July 2022

import mysql.connector
from mysql.connector import errorcode

config = {
    "user": "outlander_user",
    "password": "adventure",
    "host": "127.0.0.1",
    "database": "outland_adventures",
    "raise_on_warnings": True
}


def dropAllTables(cursor):
    cursor.execute("DROP TABLE IF EXISTS employee_job")
    cursor.execute("DROP TABLE IF EXISTS employee_inoculation")
    cursor.execute("DROP TABLE IF EXISTS employee_visa")
    cursor.execute("DROP TABLE IF EXISTS customer_inoculation")
    cursor.execute("DROP TABLE IF EXISTS customer_visa")
    cursor.execute("DROP TABLE IF EXISTS destination_inoculation")
    cursor.execute("DROP TABLE IF EXISTS destination_visa")
    cursor.execute("DROP TABLE IF EXISTS employee_order")
    cursor.execute("DROP TABLE IF EXISTS customer_order")
    cursor.execute("DROP TABLE IF EXISTS trip_item")
    cursor.execute("DROP TABLE IF EXISTS trip_excursion")
    cursor.execute("DROP TABLE IF EXISTS employee_trip")
    cursor.execute("DROP TABLE IF EXISTS customer_trip")
    cursor.execute("DROP TABLE IF EXISTS job_responsibility")
    cursor.execute("DROP TABLE IF EXISTS visa")
    cursor.execute("DROP TABLE IF EXISTS inoculation")
    cursor.execute("DROP TABLE IF EXISTS excursion")
    cursor.execute("DROP TABLE IF EXISTS trip")
    cursor.execute("DROP TABLE IF EXISTS destination")
    cursor.execute("DROP TABLE IF EXISTS item")
    cursor.execute("DROP TABLE IF EXISTS customer")
    cursor.execute("DROP TABLE IF EXISTS employee")

def createAllTables(cursor):
    createCommand = ["CREATE TABLE employee (employee_id     INT         	NOT NULL        AUTO_INCREMENT,first_name   	VARCHAR(75)     NOT NULL,last_name      	VARCHAR(75)     NOT NULL,nick_name     	VARCHAR(75),job_title      	VARCHAR(75)     NOT NULL,begin_date      DATE     		NOT NULL,end_date      	DATE,PRIMARY KEY(employee_id))", 
    "CREATE TABLE job_responsibility (job_responsibility_id 		INT         	NOT NULL        AUTO_INCREMENT,responsibility				VARCHAR(75)     NOT NULL,description			      	VARCHAR(100)    NOT NULL,PRIMARY KEY(job_responsibility_id))", 
    "CREATE TABLE employee_job (employee_job_id             INT         	NOT NULL        AUTO_INCREMENT,employee_id                 INT         	NOT NULL,job_responsibility_id 		INT         	NOT NULL,PRIMARY KEY(employee_job_id),FOREIGN KEY(employee_id)    REFERENCES employee(employee_id),FOREIGN KEY(job_responsibility_id)    REFERENCES job_responsibility(job_responsibility_id))", 
    "CREATE TABLE inoculation (inoculation_id      	INT         	NOT NULL        AUTO_INCREMENT,inoculation_type		VARCHAR(75)     NOT NULL,PRIMARY KEY(inoculation_id))", 
    "CREATE TABLE visa (visa_id 			    INT         	NOT NULL        AUTO_INCREMENT,country					VARCHAR(75)     NOT NULL,travel_purpose			VARCHAR(75)     NOT NULL,travel_requirements		VARCHAR(75)     NOT NULL,PRIMARY KEY(visa_id))", 
    "CREATE TABLE employee_inoculation (employee_inoculation_id 	INT         	NOT NULL        AUTO_INCREMENT,employee_id                 INT         	NOT NULL,inoculation_id      	    INT         	NOT NULL,date_administered		    DATE		    NOT NULL,date_expires			    DATE,PRIMARY KEY(employee_inoculation_id),FOREIGN KEY(employee_id)    REFERENCES employee(employee_id),FOREIGN KEY(inoculation_id)    REFERENCES inoculation(inoculation_id) )", 
    "CREATE TABLE employee_visa (employee_visa_id 			INT         	NOT NULL        AUTO_INCREMENT,employee_id                 INT         	NOT NULL,visa_id 		    	    INT         	NOT NULL,visa_number				    VARCHAR(75)     NOT NULL,PRIMARY KEY(employee_visa_id),FOREIGN KEY(employee_id)    REFERENCES employee(employee_id),FOREIGN KEY(visa_id)    REFERENCES visa(visa_id) )", 
    "CREATE TABLE customer (customer_id         INT         	NOT NULL        AUTO_INCREMENT,first_name   	    VARCHAR(75)     NOT NULL,last_name       	VARCHAR(75)     NOT NULL,card_number         INT             NOT NULL,emergency_contact   VARCHAR(20)     NOT NULL,PRIMARY KEY(customer_id))", 
    "CREATE TABLE customer_inoculation (customer_inoculation_id 	INT         	NOT NULL        AUTO_INCREMENT,customer_id                 INT         	NOT NULL,inoculation_id      	    INT         	NOT NULL,date_administered		    DATE		    NOT NULL,date_expires			    DATE,PRIMARY KEY(customer_inoculation_id),FOREIGN KEY(customer_id)    REFERENCES customer(customer_id),FOREIGN KEY(inoculation_id)    REFERENCES inoculation(inoculation_id))", 
    "CREATE TABLE customer_visa (customer_visa_id 			INT         	NOT NULL        AUTO_INCREMENT,customer_id                 INT         	NOT NULL,visa_id 		    	    INT         	NOT NULL,visa_number				    VARCHAR(75)     NOT NULL,PRIMARY KEY(customer_visa_id),FOREIGN KEY(customer_id)    REFERENCES customer(customer_id),FOREIGN KEY(visa_id)    REFERENCES visa(visa_id))", 
    "CREATE TABLE item (item_id 		        INT             NOT NULL        AUTO_INCREMENT,date_aquired		    DATE            NOT NULL,date_expires		    DATE,item_type	      	    VARCHAR(75)     NOT NULL,last_maintenance		DATE,is_available    		BOOLEAN         NOT NULL,PRIMARY KEY(item_id))", 
    "CREATE TABLE employee_order (employee_order_id 		INT             NOT NULL        AUTO_INCREMENT,employee_id		        INT             NOT NULL,item_id		            INT             NOT NULL,out_date                DATE            NOT NULL,in_date                 DATE,PRIMARY KEY(employee_order_id),FOREIGN KEY(employee_id)    REFERENCES employee(employee_id),FOREIGN KEY(item_id)    REFERENCES item(item_id))", 
    "CREATE TABLE customer_order (customer_order_id 		INT             NOT NULL        AUTO_INCREMENT,customer_id		        INT             NOT NULL,item_id		            INT             NOT NULL,out_date                DATE            NOT NULL,in_date                 DATE,is_rental               BOOLEAN         NOT NULL,PRIMARY KEY(customer_order_id),FOREIGN KEY(customer_id)    REFERENCES customer(customer_id),FOREIGN KEY(item_id)    REFERENCES item(item_id))",  
    "CREATE TABLE destination (destination_id 		INT             NOT NULL        AUTO_INCREMENT,region  		    VARCHAR(50)     NOT NULL,airfare_fee		    VARCHAR(50)     NOT NULL,PRIMARY KEY(destination_id))",    
    "CREATE TABLE destination_inoculation (destination_inoculation_id 	INT         	NOT NULL        AUTO_INCREMENT,destination_id                  INT         	NOT NULL,inoculation_id      	        INT         	NOT NULL,PRIMARY KEY(destination_inoculation_id),FOREIGN KEY(destination_id)    REFERENCES destination(destination_id),FOREIGN KEY(inoculation_id)    REFERENCES inoculation(inoculation_id))", 
    "CREATE TABLE destination_visa (destination_visa_id 			INT         	NOT NULL        AUTO_INCREMENT,destination_id                  INT         	NOT NULL,visa_id 		    	        INT         	NOT NULL,PRIMARY KEY(destination_visa_id),FOREIGN KEY(destination_id)    REFERENCES destination(destination_id),FOREIGN KEY(visa_id)    REFERENCES visa(visa_id))",
    "CREATE TABLE trip (trip_id 		    INT         NOT NULL        AUTO_INCREMENT,destination_id 		INT         NOT NULL,begin_date          DATE        NOT NULL,end_date            DATE        NOT NULL,PRIMARY KEY(trip_id),FOREIGN KEY(destination_id)    REFERENCES destination(destination_id))",  
    "CREATE TABLE excursion (excursion_id            INT             NOT NULL        AUTO_INCREMENT,excursion_description   VARCHAR(100)    NOT NULL,PRIMARY KEY(excursion_id))", 
    "CREATE TABLE trip_excursion (trip_excursion_id       INT         	NOT NULL        AUTO_INCREMENT,trip_id                 INT         	NOT NULL,excursion_id            INT         	NOT NULL,begin_date_time         DATETIME        NOT NULL,end_date_time           DATETIME        NOT NULL,PRIMARY KEY(trip_excursion_id),FOREIGN KEY(trip_id)    REFERENCES trip(trip_id),FOREIGN KEY(excursion_id)    REFERENCES excursion(excursion_id))", 
    "CREATE TABLE trip_item (trip_item_id       INT         	NOT NULL        AUTO_INCREMENT,trip_id            INT         	NOT NULL,item_id            INT         	NOT NULL,PRIMARY KEY(trip_item_id),FOREIGN KEY(trip_id)    REFERENCES trip(trip_id),FOREIGN KEY(item_id)    REFERENCES item(item_id))", 
    "CREATE TABLE employee_trip (employee_trip_id        INT         	NOT NULL        AUTO_INCREMENT,employee_id             INT         	NOT NULL,trip_id                 INT         	NOT NULL,PRIMARY KEY(employee_trip_id),FOREIGN KEY(employee_id)    REFERENCES employee(employee_id),FOREIGN KEY(trip_id)    REFERENCES trip(trip_id))",  
    "CREATE TABLE customer_trip (customer_trip_id        INT         	NOT NULL        AUTO_INCREMENT,customer_id             INT         	NOT NULL,trip_id                 INT         	NOT NULL,PRIMARY KEY(customer_trip_id),FOREIGN KEY(customer_id)    REFERENCES customer(customer_id),FOREIGN KEY(trip_id)    REFERENCES trip(trip_id))" 
    ]
    for create in createCommand:
        cursor.execute(create)

def insertAllTables(cursor):
    
    insertCommands = [
    "INSERT INTO employee(first_name, last_name, nick_name, job_title, begin_date, end_date )    VALUES('Blythe', 'Timmerson', NULL, 'CEO', '20220101', NULL),    	('Jim', 'Ford', NULL, 'CEO', '20220101', NULL),    	('John', 'MacNell', NULL, 'CEO', '20220201', NULL),    	('D.B.', 'Marland', NULL, 'CEO', '20220201', NULL),    	('Anita', 'Gallegos', NULL, 'CEO', '20220201', NULL),    	('Dimitrios', 'Stravopolous', NULL, 'CEO', '20220201', NULL),    	('Mei', 'Wong ', NULL, 'CEO', '20220601', NULL)",
    "INSERT INTO job_responsibility(responsibility, description)    VALUES('CEO', 'In charge of the company'),    	('Marketing', 'markets the companys services'),    	('Guides', 'takes people on path'),    	('Trip Planning', 'plans trip'),    	('Visa Checking', 'validates visa'),   	    ('Inoculation Checking', 'validates shots'),   	    ('Airfares', 'plane ride price checker'),   	    ('Inventory', 'orders products'),   	    ('E-commerce', 'marketing geniouse')",
    "INSERT INTO employee_job(employee_id, job_responsibility_id)    VALUES((SELECT employee_id FROM employee WHERE first_name = 'Blythe'), (SELECT job_responsibility_id FROM job_responsibility WHERE responsibility = 'CEO')),    ((SELECT employee_id FROM employee WHERE first_name = 'Blythe'), (SELECT job_responsibility_id FROM job_responsibility WHERE responsibility = 'Trip Planning')),    ((SELECT employee_id FROM employee WHERE first_name = 'Blythe'), (SELECT job_responsibility_id FROM job_responsibility WHERE responsibility = 'Marketing')),    ((SELECT employee_id FROM employee WHERE first_name = 'Jim'), (SELECT job_responsibility_id FROM job_responsibility WHERE responsibility = 'CEO')),    ((SELECT employee_id FROM employee WHERE first_name = 'Jim'), (SELECT job_responsibility_id FROM job_responsibility WHERE responsibility = 'Trip Planning')),    ((SELECT employee_id FROM employee WHERE first_name = 'Jim'), (SELECT job_responsibility_id FROM job_responsibility WHERE responsibility = 'Marketing')),       ((SELECT employee_id FROM employee WHERE first_name = 'John'), (SELECT job_responsibility_id FROM job_responsibility WHERE responsibility = 'Guides')),        ((SELECT employee_id FROM employee WHERE first_name = 'John'), (SELECT job_responsibility_id FROM job_responsibility WHERE responsibility = 'Trip Planning')),       ((SELECT employee_id FROM employee WHERE first_name = 'John'), (SELECT job_responsibility_id FROM job_responsibility WHERE responsibility = 'Visa Checking')),        ((SELECT employee_id FROM employee WHERE first_name = 'John'), (SELECT job_responsibility_id FROM job_responsibility WHERE responsibility = 'Inoculation Checking')),        ((SELECT employee_id FROM employee WHERE first_name = 'John'), (SELECT job_responsibility_id FROM job_responsibility WHERE responsibility = 'Airfares')),        ((SELECT employee_id FROM employee WHERE first_name = 'D.B.'), (SELECT job_responsibility_id FROM job_responsibility WHERE responsibility = 'Guides')),        ((SELECT employee_id FROM employee WHERE first_name = 'D.B.'), (SELECT job_responsibility_id FROM job_responsibility WHERE responsibility = 'Trip Planning')),        ((SELECT employee_id FROM employee WHERE first_name = 'D.B.'), (SELECT job_responsibility_id FROM job_responsibility WHERE responsibility = 'Visa Checking')),        ((SELECT employee_id FROM employee WHERE first_name = 'D.B.'), (SELECT job_responsibility_id FROM job_responsibility WHERE responsibility = 'Inoculation Checking')),    ((SELECT employee_id FROM employee WHERE first_name = 'D.B.'), (SELECT job_responsibility_id FROM job_responsibility WHERE responsibility = 'Airfares')),    ((SELECT employee_id FROM employee WHERE first_name = 'Dimitrios'), (SELECT job_responsibility_id FROM job_responsibility WHERE responsibility = 'Inventory')),    ((SELECT employee_id FROM employee WHERE first_name = 'Dimitrios'), (SELECT job_responsibility_id FROM job_responsibility WHERE responsibility = 'E-commerce'))",
    "INSERT INTO inoculation(inoculation_type)    VALUES('Covid-19'),    ('Chickenpox'),    ('Cholera'),    ('Diphtheria'),    ('Hepatitis A'),    ('Hepatitis B'),    ('Hib')",
    "INSERT INTO visa(country, travel_purpose, travel_requirements )    VALUES('China', 'Tourism', 'Money bring docs'),    ('Italy', 'Tourism', 'Money bring docs'),    ('South Africa', 'Tourism', 'Money bring docs'),    ('Greese', 'Tourism', 'Money bring docs'),    ('Colombia', 'Tourism', 'Money bring docs'),    ('Brazil', 'Tourism', 'Money bring docs'),    ('China', 'Work', 'A Job Money bring docs'),    ('Italy', 'Work', 'A Job Money bring docs'),    ('South Africa', 'Work', 'A Job Money bring docs'),    ('Greese', 'Work', 'A Job Money bring docs'),    ('Colombia', 'Work', 'A Job Money bring docs'),    ('Brazil', 'Work', 'A Job Money bring docs')",
    "INSERT INTO employee_inoculation(employee_id, inoculation_id, date_administered, date_expires)    VALUES((SELECT employee_id FROM employee WHERE first_name = 'Blythe'), (SELECT inoculation_id FROM inoculation WHERE inoculation_type = 'Covid-19'), '20220201', '20230201' ),    	((SELECT employee_id FROM employee WHERE first_name = 'Jim'), (SELECT inoculation_id FROM inoculation WHERE inoculation_type = 'Covid-19'), '20220201', '20230201' ),    	((SELECT employee_id FROM employee WHERE first_name = 'John'), (SELECT inoculation_id FROM inoculation WHERE inoculation_type = 'Covid-19'), '20220201', '20230201' ),    	((SELECT employee_id FROM employee WHERE first_name = 'D.B.'), (SELECT inoculation_id FROM inoculation WHERE inoculation_type = 'Covid-19'), '20220201', '20230201' ),        ((SELECT employee_id FROM employee WHERE first_name = 'Anita'), (SELECT inoculation_id FROM inoculation WHERE inoculation_type = 'Covid-19'), '20220201', '20230201' ),    	((SELECT employee_id FROM employee WHERE first_name = 'Dimitrios'), (SELECT inoculation_id FROM inoculation WHERE inoculation_type = 'Covid-19'), '20220201', '20230201' ),   	    ((SELECT employee_id FROM employee WHERE first_name = 'Mei'), (SELECT inoculation_id FROM inoculation WHERE inoculation_type = 'Covid-19'), '20220201', '20230201' )",
    "INSERT INTO employee_visa(employee_id, visa_id, visa_number)    VALUES((SELECT employee_id FROM employee WHERE first_name = 'Blythe'), (SELECT visa_id FROM visa WHERE travel_purpose = 'Tourism' AND country= 'China'), 88878800),    	((SELECT employee_id FROM employee WHERE first_name = 'Jim'), (SELECT visa_id FROM visa WHERE travel_purpose = 'Tourism' AND country= 'China'), 88456800),    	((SELECT employee_id FROM employee WHERE first_name = 'John'), (SELECT visa_id FROM visa WHERE travel_purpose = 'Tourism' AND country= 'China'), 13878230),    	((SELECT employee_id FROM employee WHERE first_name = 'D.B.'), (SELECT visa_id FROM visa WHERE travel_purpose = 'Tourism' AND country= 'China'), 48678320),    	((SELECT employee_id FROM employee WHERE first_name = 'Anita'), (SELECT visa_id FROM visa WHERE travel_purpose = 'Tourism' AND country= 'China'), 90004500),    	((SELECT employee_id FROM employee WHERE first_name = 'Dimitrios'), (SELECT visa_id FROM visa WHERE travel_purpose = 'Tourism' AND country= 'China'), 9868560),    	((SELECT employee_id FROM employee WHERE first_name = 'Mei'), (SELECT visa_id FROM visa WHERE travel_purpose = 'Tourism' AND country= 'China'), 43278990)",
    "INSERT INTO customer(first_name, last_name, card_number, emergency_contact)    VALUES('Zack', 'Petisso', 77772323, '626-666-6661'),    	('Mary', 'Louis', 33332421, '999-919-9922'),    	('Fabricio', 'Pontic', 45453377, '888-878-8989'),    	('Fernanda', 'Clark', 80089773, '797-096-5645'),    	('Pickle', 'Rick', 69583232, '531-452-7895'),    	('Pepe', 'Yee', 47851236, '485-253-4236'),    	('John', 'Smith', 63985265, '987-789-7894'),    	('Jimmy', 'Newtron', 74586589, '321-356-6431')",
    "INSERT INTO customer_inoculation(customer_id, inoculation_id, date_administered, date_expires)    VALUES((SELECT customer_id FROM customer WHERE first_name = 'Zack'), (SELECT inoculation_id FROM inoculation WHERE inoculation_type = 'Covid-19'), '20220201', '20230201' ),    	((SELECT customer_id FROM customer WHERE first_name = 'Mary'), (SELECT inoculation_id FROM inoculation WHERE inoculation_type = 'Covid-19'), '20220201', '20230201' ),    	((SELECT customer_id FROM customer WHERE first_name = 'Fabricio'), (SELECT inoculation_id FROM inoculation WHERE inoculation_type = 'Covid-19'), '20220201', '20230201' ),    	((SELECT customer_id FROM customer WHERE first_name = 'Fernanda'), (SELECT inoculation_id FROM inoculation WHERE inoculation_type = 'Covid-19'), '20220201', '20230201' ),    	((SELECT customer_id FROM customer WHERE first_name = 'Pickle'), (SELECT inoculation_id FROM inoculation WHERE inoculation_type = 'Covid-19'), '20220201', '20230201' ),    	((SELECT customer_id FROM customer WHERE first_name = 'Pepe'), (SELECT inoculation_id FROM inoculation WHERE inoculation_type = 'Covid-19'), '20220201', '20230201' ),    	((SELECT customer_id FROM customer WHERE first_name = 'John'), (SELECT inoculation_id FROM inoculation WHERE inoculation_type = 'Covid-19'), '20220201', '20230201' ),    	((SELECT customer_id FROM customer WHERE first_name = 'Jimmy'), (SELECT inoculation_id FROM inoculation WHERE inoculation_type = 'Covid-19'), '20220201', '20230201' )",
    "INSERT INTO customer_visa(customer_id, visa_id, visa_number)    VALUES((SELECT customer_id FROM customer WHERE first_name = 'Zack'), (SELECT visa_id FROM visa WHERE travel_purpose = 'Tourism' AND country= 'China'), 46597589),    	((SELECT customer_id FROM customer WHERE first_name = 'Mary'), (SELECT visa_id FROM visa WHERE travel_purpose = 'Tourism' AND country= 'China'), 46597589),    	((SELECT customer_id FROM customer WHERE first_name = 'Fabricio'), (SELECT visa_id FROM visa WHERE travel_purpose = 'Tourism' AND country= 'China'), 46597589),    	((SELECT customer_id FROM customer WHERE first_name = 'Fernanda'), (SELECT visa_id FROM visa WHERE travel_purpose = 'Tourism' AND country= 'China'), 46597589),    	((SELECT customer_id FROM customer WHERE first_name = 'Pickle'), (SELECT visa_id FROM visa WHERE travel_purpose = 'Tourism' AND country= 'China'), 46597589),    	((SELECT customer_id FROM customer WHERE first_name = 'Pepe'), (SELECT visa_id FROM visa WHERE travel_purpose = 'Tourism' AND country= 'China'), 46597589),    	((SELECT customer_id FROM customer WHERE first_name = 'John'), (SELECT visa_id FROM visa WHERE travel_purpose = 'Tourism' AND country= 'China'), 46597589),    	((SELECT customer_id FROM customer WHERE first_name = 'Jimmy'), (SELECT visa_id FROM visa WHERE travel_purpose = 'Tourism' AND country= 'China'), 46597589)",
    "INSERT INTO item(date_aquired, date_expires, item_type, last_maintenance, is_available)    VALUES('20180423', NULL, 'Trekking poles', '20220115', TRUE),        ('20220222', '20220115', 'Sunscreen', NULL, TRUE),        ('20190324', NULL, 'First aid kit', NULL, TRUE),        ('20210501', NULL, 'Rain coat', NULL, TRUE),        ('20220211', NULL, 'Flashlight', '20220516', TRUE),        ('20211121', '20231121', 'Water bottles', NULL, TRUE)",
    "INSERT INTO employee_order(employee_id, item_id, out_date, in_date)    VALUES((SELECT employee_id FROM employee WHERE first_name = 'John'), (SELECT item_id FROM item WHERE item_type = 'Trekking poles'), '20220201', '20220501' ),    	((SELECT employee_id FROM employee WHERE first_name = 'John'), (SELECT item_id FROM item WHERE item_type = 'Flashlight'), '20220201', '20220501' ),    	((SELECT employee_id FROM employee WHERE first_name = 'John'), (SELECT item_id FROM item WHERE item_type = 'Rain coat'), '20220201', '20220501' ),    	((SELECT employee_id FROM employee WHERE first_name = 'D.B.'), (SELECT item_id FROM item WHERE item_type = 'Water bottles'), '20220201', '20220501' ),    	((SELECT employee_id FROM employee WHERE first_name = 'D.B.'), (SELECT item_id FROM item WHERE item_type = 'First aid kit'), '20220201', '20220501' ),    	((SELECT employee_id FROM employee WHERE first_name = 'D.B.'), (SELECT item_id FROM item WHERE item_type = 'Sunscreen'), '20220201', '20220501' )",
    "INSERT INTO customer_order(customer_id, item_id, out_date, in_date, is_rental)    VALUES((SELECT customer_id FROM customer WHERE first_name = 'Zack'), (SELECT item_id FROM item WHERE item_type = 'Trekking poles'), '20220201', '20220501', TRUE ),    	((SELECT customer_id FROM customer WHERE first_name = 'Mary'), (SELECT item_id FROM item WHERE item_type = 'Trekking poles'), '20220201', '20220501', TRUE ),    	((SELECT customer_id FROM customer WHERE first_name = 'Zack'), (SELECT item_id FROM item WHERE item_type = 'Trekking poles'), '20220201', '20220501', TRUE ),    	((SELECT customer_id FROM customer WHERE first_name = 'Fabricio'), (SELECT item_id FROM item WHERE item_type = 'Trekking poles'), '20220201', '20220501', TRUE ),    	((SELECT customer_id FROM customer WHERE first_name = 'Fernanda'), (SELECT item_id FROM item WHERE item_type = 'Trekking poles'), '20220201', '20220501', TRUE ),    	((SELECT customer_id FROM customer WHERE first_name = 'pepe'), (SELECT item_id FROM item WHERE item_type = 'Trekking poles'), '20220201', '20220501', TRUE ),    	((SELECT customer_id FROM customer WHERE first_name = 'pickle'), (SELECT item_id FROM item WHERE item_type = 'Trekking poles'), '20220201', '20220501', TRUE )",
    "INSERT INTO destination(region, airfare_fee)    VALUES('South America', '10000'),    	('southern Africa', '5000'),    	('North America', '20000'),    	('southern Europe', '12452'),    	('northern Europe', '6874'),    	('heaven', '666639')",
    "INSERT INTO destination_inoculation(destination_id, inoculation_id)    VALUES((SELECT destination_id FROM destination WHERE region = 'South America'), (SELECT inoculation_id FROM inoculation WHERE inoculation_type = 'Covid-19')),    	((SELECT destination_id FROM destination WHERE region = 'southern Africa'), (SELECT inoculation_id FROM inoculation WHERE inoculation_type = 'Covid-19')),    	((SELECT destination_id FROM destination WHERE region = 'North America'), (SELECT inoculation_id FROM inoculation WHERE inoculation_type = 'Covid-19')),    	((SELECT destination_id FROM destination WHERE region = 'southern Europe'), (SELECT inoculation_id FROM inoculation WHERE inoculation_type = 'Covid-19')),    	((SELECT destination_id FROM destination WHERE region = 'northern Europe'), (SELECT inoculation_id FROM inoculation WHERE inoculation_type = 'Covid-19')),    	((SELECT destination_id FROM destination WHERE region = 'heaven'), (SELECT inoculation_id FROM inoculation WHERE inoculation_type = 'Covid-19'))",
    "INSERT INTO destination_visa(destination_id, visa_id)    VALUES((SELECT destination_id FROM destination WHERE region = 'South America'), (SELECT visa_id FROM visa WHERE travel_purpose = 'Tourism' AND country= 'Brazil')),    	((SELECT destination_id FROM destination WHERE region = 'southern Africa'), (SELECT visa_id FROM visa WHERE travel_purpose = 'Tourism' AND country= 'South Africa')),    	((SELECT destination_id FROM destination WHERE region = 'North America'), (SELECT visa_id FROM visa WHERE travel_purpose = 'Tourism' AND country= 'Colombia')),    	((SELECT destination_id FROM destination WHERE region = 'southern Europe'), (SELECT visa_id FROM visa WHERE travel_purpose = 'Tourism' AND country= 'Italy')),    	((SELECT destination_id FROM destination WHERE region = 'northern Europe'), (SELECT visa_id FROM visa WHERE travel_purpose = 'Tourism' AND country= 'Greese')),    	((SELECT destination_id FROM destination WHERE region = 'heaven'), (SELECT visa_id FROM visa WHERE travel_purpose = 'Tourism' AND country= 'Brazil'))",
    "INSERT INTO trip(destination_id, begin_date, end_date)    VALUES((SELECT destination_id FROM destination WHERE region = 'South America'), '20220201', '20220501'),    	((SELECT destination_id FROM destination WHERE region = 'South America'), '20230201', '20230501'),    	((SELECT destination_id FROM destination WHERE region = 'southern Africa'), '20240201', '20220801'),    	((SELECT destination_id FROM destination WHERE region = 'North America'), '20250201', '20220801'),    	((SELECT destination_id FROM destination WHERE region = 'southern Europe'), '20260201', '20221101'),    	((SELECT destination_id FROM destination WHERE region = 'northern Europe'), '20270201', '20221101'),    	((SELECT destination_id FROM destination WHERE region = 'heaven'), '20280201', '20230501')",
    "INSERT INTO excursion(excursion_description)    VALUES('Rock Climbing'),    	('Swimming'),    	('Tea Time'),    	('Camp Games'),    	('Outdoor Cooking Class'),    	('The Big Event')",
    "INSERT INTO trip_excursion(trip_id, excursion_id, begin_date_time, end_date_time)    VALUES((SELECT trip_id FROM trip WHERE begin_date = '20220201'), (SELECT excursion_id FROM excursion WHERE excursion_description = 'Rock Climbing'), '20220201122432', '20220201222432'),    	((SELECT trip_id FROM trip WHERE begin_date = '20230201'), (SELECT excursion_id FROM excursion WHERE excursion_description = 'Rock Climbing'), '20220201122432', '20220201222432'),    	((SELECT trip_id FROM trip WHERE begin_date = '20240201'), (SELECT excursion_id FROM excursion WHERE excursion_description = 'Rock Climbing'), '20220201122432', '20220201222432'),    	((SELECT trip_id FROM trip WHERE begin_date = '20250201'), (SELECT excursion_id FROM excursion WHERE excursion_description = 'Rock Climbing'), '20220201122432', '20220201222432'),    	((SELECT trip_id FROM trip WHERE begin_date = '20260201'), (SELECT excursion_id FROM excursion WHERE excursion_description = 'Rock Climbing'), '20220201122432', '20220201222432'),    	((SELECT trip_id FROM trip WHERE begin_date = '20270201'), (SELECT excursion_id FROM excursion WHERE excursion_description = 'Rock Climbing'), '20220201122432', '20220201222432')",
    "INSERT INTO trip_item(trip_id, item_id)    VALUES((SELECT trip_id FROM trip WHERE begin_date = '20220201'), (SELECT item_id FROM item WHERE item_type = 'Trekking poles')),    	((SELECT trip_id FROM trip WHERE begin_date = '20230201'), (SELECT item_id FROM item WHERE item_type = 'Trekking poles')),    	((SELECT trip_id FROM trip WHERE begin_date = '20240201'), (SELECT item_id FROM item WHERE item_type = 'Trekking poles')),    	((SELECT trip_id FROM trip WHERE begin_date = '20250201'), (SELECT item_id FROM item WHERE item_type = 'Trekking poles')),    	((SELECT trip_id FROM trip WHERE begin_date = '20260201'), (SELECT item_id FROM item WHERE item_type = 'Trekking poles')),    	((SELECT trip_id FROM trip WHERE begin_date = '20270201'), (SELECT item_id FROM item WHERE item_type = 'Trekking poles'))",
    "INSERT INTO employee_trip(employee_id, trip_id)    VALUES((SELECT employee_id FROM employee WHERE first_name = 'John'), (SELECT trip_id FROM trip WHERE begin_date = '20220201')),    	((SELECT employee_id FROM employee WHERE first_name = 'John'), (SELECT trip_id FROM trip WHERE begin_date = '20230201')),    	((SELECT employee_id FROM employee WHERE first_name = 'John'), (SELECT trip_id FROM trip WHERE begin_date = '20240201')),    	((SELECT employee_id FROM employee WHERE first_name = 'D.B.'), (SELECT trip_id FROM trip WHERE begin_date = '20250201')),    	((SELECT employee_id FROM employee WHERE first_name = 'D.B.'), (SELECT trip_id FROM trip WHERE begin_date = '20260201')),    	((SELECT employee_id FROM employee WHERE first_name = 'D.B.'), (SELECT trip_id FROM trip WHERE begin_date = '20270201'))",
    "INSERT INTO customer_trip(customer_id, trip_id)    VALUES((SELECT customer_id FROM customer WHERE first_name = 'Zack'), (SELECT trip_id FROM trip WHERE begin_date = '20220201')),    	((SELECT customer_id FROM customer WHERE first_name = 'Mary'), (SELECT trip_id FROM trip WHERE begin_date = '20230201')),    	((SELECT customer_id FROM customer WHERE first_name = 'Fabricio'), (SELECT trip_id FROM trip WHERE begin_date = '20240201')),    	((SELECT customer_id FROM customer WHERE first_name = 'Fernanda'), (SELECT trip_id FROM trip WHERE begin_date = '20250201')),    	((SELECT customer_id FROM customer WHERE first_name = 'Pickle'), (SELECT trip_id FROM trip WHERE begin_date = '20260201')),    	((SELECT customer_id FROM customer WHERE first_name = 'Pepe'), (SELECT trip_id FROM trip WHERE begin_date = '20270201'))"
    ]
    for insert in insertCommands:
        cursor.execute(insert)

def selectAllTables(cursor):
    tables = [
        "employee_job",
        "employee_inoculation",
        "employee_visa",
        "customer_inoculation",
        "customer_visa",
        "destination_inoculation",
        "destination_visa",
        "employee_order",
        "customer_order",
        "trip_item",
        "trip_excursion",
        "employee_trip",
        "customer_trip",
        "job_responsibility",
        "visa",
        "inoculation",
        "excursion",
        "trip",
        "destination",
        "item",
        "customer",
        "employee"]
    for table in tables:
        playerTeamSearch = "SELECT * FROM " + table

        cursor.execute(playerTeamSearch)

        players = cursor.fetchall()

        print("-- DISPLAYING " + table + " AFTER INSERT --")
        for player in players:
            print(player)
            # for field in player:
            #     print(field)




try:
    db = mysql.connector.connect(**config)
    print("\nDatabase user {} connected to MySQL on host {} with database {}".format(config["user"],config["host"],config["database"]))

    cursor = db.cursor()

    selectAllTables(cursor)


    # input("\n\nPress any key to continue...")
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("The supplied username or password are invalid")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("The specified database does not exist")
    else:
        print(err)

finally:
    db.close()
