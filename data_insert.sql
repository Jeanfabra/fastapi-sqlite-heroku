USE pi_data03;
-- ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY 'root';

DROP TABLE IF EXISTS constructor;
CREATE TABLE IF NOT EXISTS constructor (
	constructorId INT,
    constructorRef VARCHAR(100),
    constructorName VARCHAR(100),
    nationality VARCHAR(100),
    url VARCHAR(100),
    PRIMARY KEY (constructorId)
) ENGINE = InnoDB DEFAULT CHARSET = utf8mb4 COLLATE = utf8mb4_spanish_ci;
LOAD DATA INFILE "C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/constructor.csv"
INTO TABLE constructor FIELDS TERMINATED BY ',' ENCLOSED BY '"' ESCAPED BY '' LINES TERMINATED BY '\r\n'  IGNORE 1 ROWS;

DROP TABLE IF EXISTS driver;
CREATE TABLE IF NOT EXISTS driver (
	driverId INT,
    driverRef VARCHAR(200),
    driverNumber VARCHAR(200),
    driverCode VARCHAR(200),
    driverName VARCHAR(200),
    dob VARCHAR(200),
    nationality VARCHAR(200),
    url VARCHAR(200),
    PRIMARY KEY (driverId)
) ENGINE = InnoDB DEFAULT CHARSET = utf8mb4 COLLATE = utf8mb4_spanish_ci;
LOAD DATA INFILE "C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/drivers.csv"
INTO TABLE driver FIELDS TERMINATED BY ',' ENCLOSED BY '"' ESCAPED BY '' LINES TERMINATED BY '\r\n'  IGNORE 1 ROWS;

DROP TABLE IF EXISTS result;
CREATE TABLE IF NOT EXISTS result (
	resultId INT,
    raceId INT,
    driverId INT,
    constructorId INT,
    result_number VARCHAR(100),
    grid INT,
    position VARCHAR(100),
    positionText VARCHAR(100),
    positionOrder INT,
    points FLOAT,
    laps INT,
    resultTime VARCHAR(100),
    milliseconds VARCHAR(100),
    fastestLap VARCHAR(100),
    resultRank VARCHAR(100),
    fastestLapTime VARCHAR(100),
    fastestLapSpeed VARCHAR(100),
    statusId INT,
    PRIMARY KEY (resultId),
    FOREIGN KEY (raceId) REFERENCES race(raceId),
    FOREIGN KEY (driverId) REFERENCES driver(driverId),
    FOREIGN KEY (constructorId) REFERENCES constructor(constructorId)
) ENGINE = InnoDB DEFAULT CHARSET = utf8mb4 COLLATE = utf8mb4_spanish_ci;
LOAD DATA INFILE "C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/results.csv"
INTO TABLE result FIELDS TERMINATED BY ',' ENCLOSED BY '"' ESCAPED BY '' LINES TERMINATED BY '\r\n'  IGNORE 1 ROWS;

DROP TABLE IF EXISTS pitstop;
CREATE TABLE IF NOT EXISTS pitstop (
	pitstopId INT,
    raceId INT,
    driverId INT,
    pitstopStop INT,
    lap INT,
    pitstopTime VARCHAR(100),
    duration VARCHAR(100),
    milliseconds INT,
    PRIMARY KEY (pitstopId),
    FOREIGN KEY (raceId) REFERENCES race(raceId),
    FOREIGN KEY (driverId) REFERENCES driver(driverId)
) ENGINE = InnoDB DEFAULT CHARSET = utf8mb4 COLLATE = utf8mb4_spanish_ci;
LOAD DATA INFILE "C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/pitstops.csv"
INTO TABLE pitstop FIELDS TERMINATED BY ',' ENCLOSED BY '"' ESCAPED BY '' LINES TERMINATED BY '\r\n'  IGNORE 1 ROWS;

DROP TABLE IF EXISTS circuit;
CREATE TABLE IF NOT EXISTS circuit (
	circuitId INT,
    circuitRef VARCHAR(50),
    circuitName VARCHAR(100),
    location VARCHAR(100),
    country VARCHAR(50),
    latitude FLOAT,
    longitude FLOAT,
    altitude INT,
    url VARCHAR(200),
    PRIMARY KEY (circuitId)
) ENGINE = InnoDB DEFAULT CHARSET = utf8mb4 COLLATE = utf8mb4_spanish_ci;
LOAD DATA INFILE "C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/circuits.csv"
INTO TABLE circuit FIELDS TERMINATED BY ',' ENCLOSED BY '"' ESCAPED BY '' LINES TERMINATED BY '\r\n'  IGNORE 1 ROWS;

DROP TABLE IF EXISTS race;
CREATE TABLE IF NOT EXISTS race (
	raceId INT,
    raceYear INT,
    round INT,
    circuitId INT,
    raceName VARCHAR(100),
    raceDate VARCHAR(100),
    raceTime VARCHAR(100),
    url VARCHAR(100),
    PRIMARY KEY (raceId)
) ENGINE = InnoDB DEFAULT CHARSET = utf8mb4 COLLATE = utf8mb4_spanish_ci;
LOAD DATA INFILE "C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/races.csv"
INTO TABLE race FIELDS TERMINATED BY ',' ENCLOSED BY '"' ESCAPED BY '' LINES TERMINATED BY '\r\n'  IGNORE 1 ROWS;

DROP TABLE IF EXISTS lap_time;
CREATE TABLE IF NOT EXISTS lap_time (
    laptimeId INT,
	raceId INT,
    driverId INT,
    laptimeStop INT,
    laptimeTime INT,
    duration VARCHAR(100),
	milliseconds INT,
    PRIMARY KEY(laptimeId),
    FOREIGN KEY(raceId) REFERENCES race(raceId),
    FOREIGN KEY(driverId) REFERENCES driver(driverId)
) ENGINE = InnoDB DEFAULT CHARSET = utf8mb4 COLLATE = utf8mb4_spanish_ci;
LOAD DATA INFILE "C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/laptimes.csv"
INTO TABLE lap_time FIELDS TERMINATED BY ',' ENCLOSED BY '"' ESCAPED BY '' LINES TERMINATED BY '\r\n'  IGNORE 1 ROWS;

DROP TABLE IF EXISTS qualify;
CREATE TABLE IF NOT EXISTS qualify (
	qualifyId INT,
    raceId INT,
    driverId INT,
    constructorId INT,
    qualifyNumber INT,
    position INT,
    q1 VARCHAR(100),
    q2 VARCHAR(100),
    q3 VARCHAR(100),
    PRIMARY KEY (qualifyId),
    FOREIGN KEY (raceId) REFERENCES race(raceId),
    FOREIGN KEY (driverId) REFERENCES driver(driverId),
    FOREIGN KEY (constructorId) REFERENCES constructor(constructorId)
) ENGINE = InnoDB DEFAULT CHARSET = utf8mb4 COLLATE = utf8mb4_spanish_ci;
LOAD DATA INFILE "C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/qualifying.csv"
INTO TABLE qualify FIELDS TERMINATED BY ',' ENCLOSED BY '"' ESCAPED BY '' LINES TERMINATED BY '\r\n'  IGNORE 1 ROWS;