CREATE DATABASE gans;
USE gans;
-- DROP DATABASE gans;
CREATE TABLE cities(
	city_id INT AUTO_INCREMENT,
    city_name VARCHAR(200),
    country_code VARCHAR(20),
    PRIMARY KEY(city_id)
    );
    
-- TRUNCATE TABLE cities;

INSERT INTO cities (city_name, country_code) VALUES ('Berlin', 'DE');
INSERT INTO cities (city_name, country_code) VALUES ('Frankfurt', 'DE');

CREATE TABLE iss_data (
    id SERIAL PRIMARY KEY,
    location_lat FLOAT,
    location_lon FLOAT,
    iss_timestamp TIMESTAMP
);

CREATE TABLE airports (
    icao VARCHAR(4) PRIMARY KEY,
    iata VARCHAR(3),
    name VARCHAR(255),
    shortName VARCHAR(255),
    municipalityName VARCHAR(255),
    countryCode VARCHAR(3),
    location_lat FLOAT,
    location_lon FLOAT,
    city VARCHAR(255)
);

CREATE TABLE flights (
    id SERIAL PRIMARY KEY,
    icao VARCHAR(4),
    flight_number VARCHAR(255),
    terminal VARCHAR(255),
    arrival_time VARCHAR(255)
);

CREATE TABLE weather (
    id SERIAL PRIMARY KEY,
    forecast_time TIMESTAMP NOT NULL,
    outlook VARCHAR(255) NOT NULL,
    temperature FLOAT NOT NULL,
    feels_like FLOAT NOT NULL,
    wind_speed FLOAT NOT NULL
);

