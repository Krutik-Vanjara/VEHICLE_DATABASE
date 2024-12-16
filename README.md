 # Car Database Relational Schema

This Branch contains the relational schema for a car database. The schema is designed to store information about cars, their features, specifications, dimensions, and ownership details.

## Table of Contents

- [Entities and Tables](#entities-and-tables)
- [Relational Schema Design](#relational-schema-design)
  - [Cars Table](#cars-table)
  - [Features Table](#features-table)
  - [Specifications Table](#specifications-table)
  - [Dimensions Table](#dimensions-table)
  - [Ownership Table](#ownership-table)


## Entities and Tables

The database is organized into the following entities and tables:

1. **Cars**
2. **Features**
3. **Specifications**
4. **Dimensions**
5. **Ownership**

## Relational Schema Design

### Cars Table

Stores basic information about each car.

- **Columns:**
  - `CAR_ID` (Primary Key)
  - `MAKE`
  - `MODEL`
  - `PRICE`
  - `YEAR`
  - `FUEL_TYPE`
  - `LOCATION`
  - `TRANSMISSION`

### Features Table

Stores additional features of each car.

- **Columns:**
  - `FEATURE_ID` (Primary Key)
  - `CAR_ID` (Foreign Key)
  - `COLOR`
  - `SEATING_CAPACITY`
  - `FUEL_TANK_CAPACITY`

### Specifications Table

Stores technical specifications of each car.

- **Columns:**
  - `SPEC_ID` (Primary Key)
  - `CAR_ID` (Foreign Key)
  - `ENGINE`
  - `MAX_POWER`
  - `MAX_TORQUE`
  - `DRIVETRAIN`

### Dimensions Table

Stores dimensional details of each car.

- **Columns:**
  - `DIMENSION_ID` (Primary Key)
  - `CAR_ID` (Foreign Key)
  - `LENGTH`
  - `WIDTH`
  - `HEIGHT`

### Ownership Table

Stores ownership and seller information of each car.

- **Columns:**
  - `OWNERSHIP_ID` (Primary Key)
  - `CAR_ID` (Foreign Key)
  - `OWNER`
  - `SELLER_TYPE`
  - `KILOMETER`
 
  ## Table Constraints

1. **`CHK_PRICE`**
   - **Constraint Type:** Check
   - **Search Condition:** Price >= 0

2. **`CHK_YEAR`**
   - **Constraint Type:** Check
   - **Search Condition:** Year BETWEEN 1886 AND 9999

3. **`SYS_C008363`**
   - **Constraint Type:** Primary Key
   - **Search Condition:** (null)

4. **`SYS_C008364`**
   - **Constraint Type:** Check
   - **Search Condition:** "CAR_ID" IS NOT NULL

5. **`SYS_C008365`**
   - **Constraint Type:** Check
   - **Search Condition:** "MAKE" IS NOT NULL

6. **`SYS_C008366`**
   - **Constraint Type:** Check
   - **Search Condition:** "MODEL" IS NOT NULL

7. **`SYS_C008367`**
   - **Constraint Type:** Check
   - **Search Condition:** "PRICE" IS NOT NULL

8. **`SYS_C008368`**
   - **Constraint Type:** Check
   - **Search Condition:** "YEAR" IS NOT NULL

9. **`SYS_C008369`**
   - **Constraint Type:** Check
   - **Search Condition:** "FUEL_TYPE" IS NOT NULL

10. **`SYS_C008370`**
    - **Constraint Type:** Check
    - **Search Condition:** "LOCATION" IS NOT NULL

11. **`SYS_C008371`**
    - **Constraint Type:** Check
    - **Search Condition:** "TRANSMISSION" IS NOT NULL

