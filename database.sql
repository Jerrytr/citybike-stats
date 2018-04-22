DROP DATABASE IF EXISTS bike_info_db;
CREATE DATABASE bike_info_db;
USE bike_info_db;

CREATE TABLE Bikestations (
    StationID VARCHAR(10) NOT NULL,
    StationName VARCHAR(255) NOT NULL,
    StationLon VARCHAR(255) NOT NULL,
    StationLat VARCHAR(255) NOT NULL,
    PRIMARY KEY(StationID)
);

CREATE TABLE Bikestats (
    StationID VARCHAR(10) NOT NULL,
    Bikesfree INT,
    Timestamp datetime,
    FOREIGN KEY(StationID) REFERENCES Bikestations(StationID)
);