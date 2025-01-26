-- Create the database (if not already created)
-- SQLite automatically creates the database when you connect to it.

-- Connect to the database (this is done in your code, not in SQL)

-- Create Users Table
CREATE TABLE IF NOT EXISTS Users (
    user_id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL UNIQUE,
    vehicle_type TEXT NOT NULL,
    fuel_efficiency REAL NOT NULL,
    priority TEXT NOT NULL,
    avoid_tolls BOOLEAN DEFAULT 0,
    avoid_highways BOOLEAN DEFAULT 0,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);

-- Create Routes Table
CREATE TABLE IF NOT EXISTS Routes (
    route_id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    start_location TEXT NOT NULL,
    end_location TEXT NOT NULL,
    distance REAL NOT NULL,
    duration REAL NOT NULL,
    route_type TEXT NOT NULL,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES Users(user_id)
);

-- Create EcoMetrics Table
CREATE TABLE IF NOT EXISTS EcoMetrics (
    metric_id INTEGER PRIMARY KEY AUTOINCREMENT,
    route_id INTEGER NOT NULL,
    carbon_footprint REAL NOT NULL,
    fuel_consumption REAL NOT NULL,
    cost_savings REAL NOT NULL,
    emission_savings REAL NOT NULL,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (route_id) REFERENCES Routes(route_id)
);

-- Create ChargingStations Table (Optional)
CREATE TABLE IF NOT EXISTS ChargingStations (
    station_id INTEGER PRIMARY KEY AUTOINCREMENT,
    route_id INTEGER NOT NULL,
    station_name TEXT NOT NULL,
    location TEXT NOT NULL,
    station_type TEXT NOT NULL,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (route_id) REFERENCES Routes(route_id)
);