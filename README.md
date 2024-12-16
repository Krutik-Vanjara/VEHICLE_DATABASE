# Features = All chapters

## This branch contains all code and queries related to the chapters.
- [Chapter 1: Preparing Your Relational Schema](#chapter-1-preparing-your-relational-schema)
- [Chapter 2: Security and User Management](#chapter-2-Security-and-User-Management)
- [ Chapter 3: Queries and Optimization](#Chapter-3-Queries-and-Optimization)
- [Chapter 4: Automation of the Information System](#Chapter-4-Automation-of-the-Information-System)
- [Chapter 5: Graphical Interface](#Chapter-5-Graphical-Interface)


## Chapter 1: Preparing Your Relational Schema
- This database schema manages comprehensive information about cars, covering specifications, features, ownership, and dimensions. It includes five tables: CarDetails, CarSpecifications, CarFeatures, CarOwnership, and CarDimensions. 

- [You can see here in details](https://github.com/Krutik-Vanjara/VEHICLE_DATABASE/tree/DATASET)
## Chapter 2: Security and User Management
 **Overview** 
- This section details user and role management in the car management system, ensuring appropriate access levels to database tables for different users. The system accommodates three user types: admin, manager, and regular users, each with distinct roles and permissions.
 **Users and Roles**  
**1.Admin User (C##admin_user)**
  **Role:** C##admin_role  
  **Permissions:** Full access to all tables (CarDetails, CarSpecifications, CarFeatures, CarOwnership, CarDimensions).  
**2.Manager User (C##manager_user)**  
  **Role:** C##manager_role  
  **Permissions:** Modify access (read, insert, update) to all tables, with no Data Definition Language (DDL) permissions.  
**3.Regular User (C##regular_user)**  
  **Role:** C##regular_role  
  **Permissions:** Read-only access to all tables.  
**Role Creation and Privileges**  
  **Admin Role (C##admin_role):** Full access to all tables.  
  **Manager Role (C##manager_role):** Select, insert, and update privileges on all tables.  
  **Regular Role (C##regular_role):** Select privileges on all tables.  
**Assigning Roles to Users**  
  C##admin_role is assigned to C##admin_user.  
  C##manager_role is assigned to C##manager_user.  
  C##regular_role is assigned to C##regular_user.  
**Password Policy**  
  The default profile is modified to set a 90-day password lifetime, requiring periodic password changes.  
**Views for Restricted Access**  
A view, CarDetails_View, is created to limit access to specific columns (Car_ID, Make, Model) for users with the C##regular_role, ensuring the underlying table remains secure by restricting access to other columns.
## Chapter 3: Queries and Optimization

## Chapter 4: Automation of the Information System

## Chapter 5: Graphical Interface

 -The first version of the GUI created with Python's CustomTkinter is complete, but it is not connected to a database.

## To run this GUI, first install the dependencies:

pip install customtkinter pillow python3

-  Clone these two files:
-  (# [gui_system.py](https://github.com/Krutik-Vanjara/VEHICLE_DATABASE/blob/Features/gui_system.py))
-  (# [shopping.ico](https://github.com/Krutik-Vanjara/VEHICLE_DATABASE/blob/Features/shopping.ico))
