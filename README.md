 # Information System Project

## Overview

This project aims to design, secure, optimize, and automate the management of an Information System (IS) for a used car dataset. The project involves preparing a relational schema, implementing security measures, optimizing queries, and automating tasks. The dataset contains information about used cars, which can be used for various purposes such as price prediction to exemplify the use of linear regression in Machine Learning.

## Dataset Details

The dataset contains the following columns:
- `name`
- `year`
- `selling_price`
- `km_driven`
- `fuel`
- `seller_type`
- `transmission`
- `Owner`

There are five different CSV files included in this dataset.

## Project Structure

The project is organized into the following branches:
- `DATASETS :` This branch contains all the .csv files used to create this database.
- `Features:`  This branch contains all chapter-wise sections along with related SQL queries, code, and other documents.

 <!--## Chapter 1

Database Schema for Car Management System
Overview
This database schema is designed to manage detailed information about cars, including their specifications, features, ownership, and dimensions. The schema consists of five tables: CarDetails, CarSpecifications, CarFeatures, CarOwnership, and CarDimensions.

# Tables and Their Descriptions
# CarDetails

# Purpose: Stores basic information about each car.

Columns:
 Car_ID: Primary key, unique identifier for each car.
 Make: Manufacturer of the car.
 Model: Model of the car.
 Price: Price of the car (must be non-negative).
 Year: Year of manufacture (must be between 1886 and 9999).
 Fuel_Type: Type of fuel the car uses.
 Location: Location of the car.
 Transmission: Type of transmission (e.g., automatic, manual).
 CarSpecifications

# Purpose: Stores technical specifications of each car.

Columns:
 Spec_ID: Primary key, unique identifier for each specification.
 Car_ID: Foreign key referencing CarDetails.
 Engine: Engine type.
 Max_Power: Maximum power output.
 Max_Torque: Maximum torque.
 Drivetrain: Type of drivetrain (e.g., FWD, RWD, AWD).
 CarFeatures

# Purpose: Stores additional features of each car.

Columns:
 Feature_ID: Primary key, unique identifier for each feature.
 Car_ID: Foreign key referencing CarDetails.
 Color: Color of the car.
 Seating_Capacity: Number of seats.
 Fuel_Tank_Capacity: Capacity of the fuel tank.
 CarOwnership

# Purpose: Stores ownership and usage information of each car.

Columns:
 Ownership_ID: Primary key, unique identifier for each ownership record.
 Car_ID: Foreign key referencing CarDetails.
 Owner: Name of the owner.
 Seller_Type: Type of seller (e.g., individual, dealer).
 Kilometer: Kilometers driven.
 CarDimensions

# Purpose: Stores dimensional information of each car.

Columns:
 Dimension_ID: Primary key, unique identifier for each dimension record.
 Car_ID: Foreign key referencing CarDetails.
 Length: Length of the car.
 Width: Width of the car.
 Height: Height of the car.
 User and Schema Management
 
# A new user C##car_schema is created and granted DBA privileges.
# The session is set to use the C##car_schema schema for creating tables.

Constraints
 Primary keys ensure uniqueness for each record.
 Foreign keys maintain referential integrity between tables.
 Check constraints ensure valid data entry for Price and Year.


## Chapter 2

User and Role Management for Car Management System
Overview
This section outlines the user and role management for the car management system, ensuring that different users have appropriate access levels to the database tables. The system includes three types of users: admin, manager, and regular users, each with specific roles and permissions.

Users and Roles
Admin User (C##admin_user)

Role: C##admin_role
Permissions: Full access to all tables (CarDetails, CarSpecifications, CarFeatures, CarOwnership, CarDimensions).
Manager User (C##manager_user)

Role: C##manager_role
Permissions: Modify access (read, insert, update) to all tables, but no Data Definition Language (DDL) permissions.
Regular User (C##regular_user)

Role: C##regular_role
Permissions: Read-only access to all tables.
Role Creation and Privileges
Admin Role (C##admin_role): Granted full access to all tables.
Manager Role (C##manager_role): Granted select, insert, and update privileges on all tables.
Regular Role (C##regular_role): Granted select privileges on all tables.
Assigning Roles to Users
C##admin_role is assigned to C##admin_user.
C##manager_role is assigned to C##manager_user.
C##regular_role is assigned to C##regular_user.
Password Policy
The default profile is altered to set the password lifetime to 90 days, ensuring that passwords expire and need to be changed periodically.
Views for Restricted Access
A view CarDetails_View is created to restrict access to only specific columns (Car_ID, Make, Model) for users assigned to the C##regular_role. This ensures that the underlying table remains secure, with access to other columns restricted.

## Chapter 3

Queries for Car Management System
Overview
This section provides a set of SQL queries designed to retrieve and analyze data from the car management system. These queries cover various aspects such as listing cars with their specifications, calculating average prices, ranking cars by price, and optimizing query performance.

Queries and Their Descriptions

List All Cars with Specifications and Features

SELECT cd.Car_ID, cd.Make, cd.Model, cs.Engine, cs.Max_Power, cf.Color, cf.Seating_Capacity
FROM C##car_schema.CarDetails cd
JOIN C##car_schema.CarSpecifications cs ON cd.Car_ID = cs.Car_ID
JOIN C##car_schema.CarFeatures cf ON cd.Car_ID = cf.Car_ID;
Purpose: Retrieves a list of all cars along with their specifications and features.

Calculate Average Price of Cars by Fuel Type


SELECT Fuel_Type, ROUND(AVG(Price),2) AS Average_Price
FROM C##car_schema.CarDetails
GROUP BY Fuel_Type
ORDER BY Average_Price DESC;
Purpose: Calculates the average price of cars grouped by fuel type and orders the results by average price in descending order.
Find Cars Priced Higher Than the Average Price


SELECT Car_ID, Make, Model, Price
FROM C##car_schema.CarDetails
WHERE Price > (SELECT ROUND(AVG(Price),2) FROM C##car_schema.CarDetails);
Purpose: Identifies cars whose price is higher than the average price of all cars.
Rank Cars by Price Within Each Fuel Type


SELECT Car_ID, Make, Model, Price, Fuel_Type,
       RANK() OVER (PARTITION BY Fuel_Type ORDER BY Price DESC) AS Price_Rank
FROM C##car_schema.CarDetails;
Purpose: Ranks cars by price within each fuel type category.
Find Cars with Specifications but Missing Ownership Details


SELECT cd.Car_ID, cd.Make, cd.Model, cd.price, cd.year
FROM C##car_schema.CarDetails cd
LEFT JOIN C##car_schema.CarOwnership co ON cd.Car_ID = co.Car_ID
WHERE co.Car_ID IS NOT NULL;
Purpose: Identifies cars that have specifications but are missing ownership details.
Total Number of Cars by Location and Their Average Price


SELECT cd.Location, COUNT(cd.Car_ID) AS Total_Cars, ROUND(AVG(cd.Price),2) AS Average_Price
FROM C##car_schema.CarDetails cd
JOIN C##car_schema.CarOwnership co ON cd.Car_ID = co.Car_ID
GROUP BY cd.Location
ORDER BY Total_Cars DESC;
Purpose: Calculates the total number of cars and their average price grouped by location.
List Specific Cars with Their Specifications and Features


SELECT cd.Make, cd.Model, cd.price, cs.Engine, cs.Max_Power, cf.Color, cf.Seating_Capacity, cf.fuel_tank_capacity
FROM C##car_schema.CarDetails cd
JOIN C##car_schema.CarSpecifications cs ON cd.Car_ID = cs.Car_ID
JOIN C##car_schema.CarFeatures cf ON cd.Car_ID = cf.Car_ID
WHERE cd.Make IN ('Toyota', 'Honda');
Purpose: Lists specific cars (e.g., Toyota, Honda) along with their specifications and features.
Optimized Queries
Optimized Query with Index


CREATE INDEX idx_fuel_type ON C##car_schema.CarDetails(Fuel_Type);

SELECT Car_ID, Make, Model, Fuel_Type
FROM C##car_schema.CarDetails
WHERE Fuel_Type = 'Petrol';
Purpose: Creates an index on the Fuel_Type column to optimize queries filtering by fuel type.
Optimized Query with Rewritten Join


SELECT cd.Car_ID, cd.Make, cd.Model, cd.Price
FROM C##car_schema.CarDetails cd
JOIN (SELECT AVG(Price) AS AvgPrice FROM C##car_schema.CarDetails) avg_table
ON cd.Price > avg_table.AvgPrice;
Purpose: Optimizes the query to find cars priced higher than the average price using a subquery join.
Optimized Query of Join with Index


CREATE INDEX idx_car_id ON C##car_schema.CarFeatures(Car_ID);

SELECT cd.Car_ID, cd.Make, cd.Model, cf.Color
FROM C##car_schema.CarDetails cd
JOIN C##car_schema.CarFeatures cf ON cd.Car_ID = cf.Car_ID;
Purpose: Creates an index on the Car_ID column in the CarFeatures table to optimize join operations.
Optimized Query Using CTE


WITH AvgPricePerFuel AS (
    SELECT Fuel_Type, ROUND(AVG(Price), 2) AS Average_Price
    FROM C##car_schema.CarDetails
    GROUP BY Fuel_Type
)
SELECT *
FROM AvgPricePerFuel
ORDER BY Average_Price DESC;
Purpose: Uses a Common Table Expression (CTE) to calculate the average price of cars by fuel type and orders the results by average price in descending order.

## Chapter 4

riggers, Functions, and Procedures for Car Management System
Overview
This section describes the triggers, functions, and procedures implemented to manage and automate various operations within the car management system. These include logging deletions, restricting user actions, calculating total car values, updating car prices, and counting cars based on specific criteria.

Triggers
Trigger to Print Message on New Record Insertion


CREATE OR REPLACE TRIGGER trg_update_statistics
AFTER INSERT ON C##car_schema.CarDetails
FOR EACH ROW
BEGIN
    DBMS_OUTPUT.PUT_LINE('A new car record was inserted with Car_ID: ' || :NEW.Car_ID);
END;
Purpose: Prints a message to the console every time a new record is added to the CarDetails table.
Trigger to Log Deletions from CarSpecifications


CREATE TABLE C##car_schema.Log_Delete_Specifications (
    Log_ID NUMBER GENERATED BY DEFAULT AS IDENTITY PRIMARY KEY,
    Spec_ID NUMBER,
    Deleted_On DATE DEFAULT SYSDATE
);

CREATE OR REPLACE TRIGGER trg_log_deletions
BEFORE DELETE ON C##car_schema.CarSpecifications
FOR EACH ROW
BEGIN
    INSERT INTO C##car_schema.Log_Delete_Specifications (Spec_ID)
    VALUES (:OLD.Spec_ID);
END;
Purpose: Logs deletions from the CarSpecifications table by inserting the deleted Spec_ID into a log table.
Trigger to Restrict DELETE or UPDATE by Regular User


CREATE OR REPLACE TRIGGER trg_restrict_regular_user
BEFORE DELETE OR UPDATE ON C##car_schema.CarDetails
FOR EACH ROW
BEGIN
    IF SYS_CONTEXT('USERENV', 'SESSION_USER') = 'C##REGULAR_USER' THEN
        RAISE_APPLICATION_ERROR(-20001, 'You don''t have sufficient privileges');
    END IF;
END;
Purpose: Prevents the regular user from performing DELETE or UPDATE operations on the CarDetails table.
Functions
Function to Calculate Total Car Value


CREATE OR REPLACE FUNCTION get_total_car_value
RETURN NUMBER IS
    total_value NUMBER;
BEGIN
    SELECT SUM(Price)
    INTO total_value
    FROM C##car_schema.CarDetails;
    RETURN total_value;
END;
Purpose: Calculates the total value of all cars in the CarDetails table.
Usage:

SELECT get_total_car_value() AS Total_Value FROM DUAL;
Function to Calculate Total Car Value by Make


CREATE OR REPLACE FUNCTION get_total_car_value_by_make (
    p_make IN VARCHAR2
)
RETURN NUMBER IS
    total_value NUMBER;
BEGIN
    SELECT SUM(Price)
    INTO total_value
    FROM C##car_schema.CarDetails
    WHERE Make = p_make;
    RETURN NVL(total_value, 0);
END;
Purpose: Calculates the total value of cars for a specific make.
Usage:

SELECT get_total_car_value_by_make('Toyota') AS Total_Value FROM DUAL;
SELECT get_total_car_value_by_make('Honda') AS Total_Value FROM DUAL;
Procedures
Procedure to Update Car Price


CREATE OR REPLACE PROCEDURE update_car_price (
    p_car_id IN NUMBER,
    p_new_price IN NUMBER
) AS
BEGIN
    UPDATE C##car_schema.CarDetails
    SET Price = p_new_price
    WHERE Car_ID = p_car_id;
    COMMIT;
END;
Purpose: Updates the price of a specific car.
Usage:

BEGIN
    update_car_price(1, 25000);
END;
Procedure to Count Cars by Location and Fuel Type


CREATE OR REPLACE PROCEDURE get_car_count_by_location (
    p_location IN VARCHAR2,
    p_fuel_type IN VARCHAR2,
    car_count OUT NUMBER
) AS
BEGIN
    SELECT COUNT(*)
    INTO car_count
    FROM C##car_schema.CarDetails
    WHERE Location = p_location AND Fuel_Type = p_fuel_type;
END;
Purpose: Counts the number of cars based on location and fuel type.
Usage:

DECLARE
    count_result NUMBER;
BEGIN
    get_car_count_by_location('Pune', 'Petrol', count_result);
    DBMS_OUTPUT.PUT_LINE('Number of cars in Pune with Petrol: ' || count_result);
END;-->
