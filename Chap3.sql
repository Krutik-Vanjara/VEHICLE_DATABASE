SELECT SYS_CONTEXT('USERENV', 'CURRENT_SCHEMA') FROM DUAL;

ALTER SESSION SET CURRENT_SCHEMA = C##car_schema;

----Query to list all cars with their specifications and features:
SELECT cd.Car_ID, cd.Make, cd.Model, cs.Engine, cs.Max_Power, cf.Color, cf.Seating_Capacity
FROM C##car_schema.CarDetails cd
JOIN C##car_schema.CarSpecifications cs ON cd.Car_ID = cs.Car_ID
JOIN C##car_schema.CarFeatures cf ON cd.Car_ID = cf.Car_ID;

----Query to calculate the average price of cars by fuel type

SELECT Fuel_Type, ROUND(AVG(Price),2) AS Average_Price
FROM C##car_schema.CarDetails
GROUP BY Fuel_Type
ORDER BY Average_Price DESC;

-----Query to find cars whose price is higher than the average price:

SELECT Car_ID, Make, Model, Price
FROM C##car_schema.CarDetails
WHERE Price > (SELECT ROUND(AVG(Price),2) FROM C##car_schema.CarDetails);

---Query to rank cars by price within each fuel type:
SELECT Car_ID, Make, Model, Price, Fuel_Type,
       RANK() OVER (PARTITION BY Fuel_Type ORDER BY Price DESC) AS Price_Rank
FROM C##car_schema.CarDetails;

---Query to find cars with specifications but missing ownership details:
SELECT cd.Car_ID, cd.Make, cd.Model, cd.price, cd.year
FROM C##car_schema.CarDetails cd
LEFT JOIN C##car_schema.CarOwnership co ON cd.Car_ID = co.Car_ID
WHERE co.Car_ID IS NOT NULL;


---Query to get the total number of cars by location and their average price:
SELECT cd.Location, COUNT(cd.Car_ID) AS Total_Cars, Round(AVG(cd.Price),2) AS Average_Price
FROM C##car_schema.CarDetails cd
JOIN C##car_schema.CarOwnership co ON cd.Car_ID = co.Car_ID
GROUP BY cd.Location
ORDER BY Total_Cars DESC;

----Query to list specific cars with their specifications and features:
SELECT cd.Make, cd.Model,cd.price, cs.Engine, cs.Max_Power, cf.Color, cf.Seating_Capacity, cf.fuel_tank_capacity
FROM C##car_schema.CarDetails cd
JOIN C##car_schema.CarSpecifications cs ON cd.Car_ID = cs.Car_ID
JOIN C##car_schema.CarFeatures cf ON cd.Car_ID = cf.Car_ID
WHERE cd.Make IN ('Toyota', 'Honda');

----- Optimized Query with Index

CREATE INDEX idx_fuel_type ON C##car_schema.CarDetails(Fuel_Type);

SELECT Car_ID, Make, Model, Fuel_Type
FROM C##car_schema.CarDetails
WHERE Fuel_Type = 'Petrol';

----- Optimized Query with Rewritten Join

SELECT cd.Car_ID, cd.Make, cd.Model, cd.Price
FROM C##car_schema.CarDetails cd
JOIN (SELECT AVG(Price) AS AvgPrice FROM C##car_schema.CarDetails) avg_table
ON cd.Price > avg_table.AvgPrice;

----- Optimized Query Of Join with Index

CREATE INDEX idx_car_id ON C##car_schema.CarFeatures(Car_ID);

SELECT cd.Car_ID, cd.Make, cd.Model, cf.Color
FROM C##car_schema.CarDetails cd
JOIN C##car_schema.CarFeatures cf ON cd.Car_ID = cf.Car_ID;


------Optimized Query Using CTE

WITH AvgPricePerFuel AS (
    SELECT Fuel_Type, ROUND(AVG(Price), 2) AS Average_Price
    FROM C##car_schema.CarDetails
    GROUP BY Fuel_Type
)
SELECT * 
FROM AvgPricePerFuel
ORDER BY Average_Price DESC;
