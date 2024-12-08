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
- [SQL Commands to Create Tables](#sql-commands-to-create-tables)
- [Representing in GUI](#representing-in-gui)
- [Example GUI Layout](#example-gui-layout)

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
