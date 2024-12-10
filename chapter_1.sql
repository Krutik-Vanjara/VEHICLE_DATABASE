SELECT SYS_CONTEXT('USERENV', 'CURRENT_SCHEMA') FROM DUAL;

CREATE USER C##car_schema IDENTIFIED BY password;
GRANT DBA TO C##car_schema;


ALTER SESSION SET CURRENT_SCHEMA = C##car_schema;

-- Create table 1 cars_dataset
CREATE TABLE CarDetails (
    Car_ID NUMBER PRIMARY KEY NOT NULL, -- set Car_ID as a PRIMARY KEY for this table
    Make VARCHAR2(50) NOT NULL,
    Model VARCHAR2(50) NOT NULL,
    Price NUMBER NOT NULL CHECK (Price >= 0),
    Year NUMBER NOT NULL CHECK (Year BETWEEN 1886 AND 9999),
    Fuel_Type VARCHAR2(20) NOT NULL,
    Location VARCHAR2(20) NOT NULL,
    Transmission VARCHAR2(20) NOT NULL
);
-- create table 2 specification_datasets 
CREATE TABLE CarSpecifications (
    Spec_ID NUMBER PRIMARY KEY, -- SET  Spec_ID  AS a  PRIMARY KEY for this table2 
    Car_ID NUMBER,
    Engine VARCHAR2(50),
    Max_Power VARCHAR2(50),
    Max_Torque VARCHAR2(50),
    Drivetrain VARCHAR2(50),
    CONSTRAINT fk_CarDetails FOREIGN KEY (Car_ID)
    REFERENCES CarDetails(Car_ID)
);
-- create table 3 features_dataset
CREATE TABLE CarFeatures (
    Feature_ID NUMBER PRIMARY KEY, -- Feature_ID as a PRIMARY KEY FOR THIS TABLE3
    Car_ID NUMBER,
    Color VARCHAR2(30),
    Seating_Capacity NUMBER,
    Fuel_Tank_Capacity NUMBER,
    CONSTRAINT fk_Car_Details FOREIGN KEY (Car_ID)
    REFERENCES CarDetails(Car_ID)
);
-- create table 4 ownership_datasets
CREATE TABLE CarOwnership (
    Ownership_ID NUMBER PRIMARY KEY, --  Ownership_ID as a PRIMARY KEY for this table4
    Car_ID NUMBER,
    Owner VARCHAR2(50),
    Seller_Type VARCHAR2(30),
    Kilometer NUMBER,
    CONSTRAINT fk_CarD FOREIGN KEY (Car_ID)
    REFERENCES CarDetails(Car_ID)
);
-- create table 5 dimensions_datasets
CREATE TABLE CarDimensions (
    Dimension_ID NUMBER PRIMARY KEY, --set Dimension_ID as a PRIMARY KEY for this table5
    Car_ID NUMBER,
    Length NUMBER,
    Width NUMBER,
    Height NUMBER,
    CONSTRAINT fk_CarDet FOREIGN KEY (Car_ID)
    REFERENCES CarDetails(Car_ID)
);

Select * from cardimensions;

SELECT cd.Model, cf.width
FROM CarDetails cd
JOIN cardimensions cf
ON cd.Car_ID = cf.Car_ID

