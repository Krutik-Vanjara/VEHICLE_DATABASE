SELECT SYS_CONTEXT('USERENV', 'CURRENT_SCHEMA') FROM DUAL;

ALTER SESSION SET CURRENT_SCHEMA = C##car_schema;

-- Create admin user
CREATE USER C##admin_user IDENTIFIED BY password;

-- Create manager user
CREATE USER C##manager_user IDENTIFIED BY password;

-- Create regular user
CREATE USER C##regular_user IDENTIFIED BY password;


-- Grant connect privilege to all users
GRANT CONNECT TO C##admin_user;
GRANT CONNECT TO C##manager_user;
GRANT CONNECT TO C##regular_user;

-- Create roles
CREATE ROLE C##admin_role;
CREATE ROLE C##manager_role;
CREATE ROLE C##regular_role;

-- Admin Role: Full access to all tables
GRANT ALL ON CarDetails TO C##admin_role;
GRANT ALL ON CarSpecifications TO C##admin_role;
GRANT ALL ON CarFeatures TO C##admin_role;
GRANT ALL ON CarOwnership TO C##admin_role;
GRANT ALL ON CarDimensions TO C##admin_role;

-- Manager Role: Modify access (read, insert, update, delete) but no DDL permissions
GRANT SELECT, INSERT, UPDATE, DELETE ON CarDetails TO C##manager_role;
GRANT SELECT, INSERT, UPDATE, DELETE ON CarSpecifications TO C##manager_role;
GRANT SELECT, INSERT, UPDATE, DELETE ON CarFeatures TO C##manager_role;
GRANT SELECT, INSERT, UPDATE, DELETE ON CarOwnership TO C##manager_role;
GRANT SELECT, INSERT, UPDATE, DELETE ON CarDimensions TO C##manager_role;

-- Regular Role: Read-only access
GRANT SELECT ON CarDetails TO C##regular_role;
GRANT SELECT ON CarSpecifications TO C##regular_role;
GRANT SELECT ON CarFeatures TO C##regular_role;
GRANT SELECT ON CarOwnership TO C##regular_role;
GRANT SELECT ON CarDimensions TO C##regular_role;

-- Assign roles to users
GRANT C##admin_role TO C##admin_user;
GRANT C##manager_role TO C##manager_user;
GRANT C##regular_role TO C##regular_user;

ALTER PROFILE DEFAULT LIMIT PASSWORD_LIFE_TIME 90; -- Password expires in 90 days

--This approach restricts access to only the specified columns (Car_ID, Make, Model) for users
--assigned to the regular_role. The underlying table remains secure, with access to other columns restricted.

CREATE OR REPLACE VIEW C##car_schema.CarDetails_View AS --Create a View with Limited Columns:
SELECT Car_ID, Make, Model
FROM C##car_schema.CarDetails;

GRANT SELECT ON C##car_schema.CarDetails_View TO C##regular_role;


-- View privileges for a specific user
SELECT * FROM USER_TAB_PRIVS WHERE GRANTEE = 'C##MANAGER_USER';

SELECT * FROM DBA_TAB_PRIVS WHERE GRANTEE = 'C##MANAGER_USER';


-- View roles assigned to users
SELECT * FROM DBA_ROLE_PRIVS WHERE GRANTEE IN ('C##ADMIN_USER', 'C##MANAGER_USER', 'C##REGULAR_USER');

SELECT USERNAME FROM DBA_USERS WHERE USERNAME IN ('C##ADMIN_USER', 'C##MANAGER_USER', 'C##REGULAR_USER');
