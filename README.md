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

## Chapter 1

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
