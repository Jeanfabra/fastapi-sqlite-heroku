from sqlalchemy import Boolean, Column, Integer, String, Date, DateTime, Float, Text, ForeignKey
from config.database import Base
from sqlalchemy.orm import relationship

# We will use this Base class we created before to create the SQLAlchemy models.
# model = classes and instances that interact with the database.

class circuit(Base):
   
    __tablename__ = "circuit"

    circuitId = Column(Integer, primary_key = True, index = True)
    circuitRef = Column(String, index = True)
    circuitName = Column(String, index = True)
    location = Column(String, index = True)
    country = Column(String, index = True)
    latitude = Column(Float)
    longitude = Column(Float)
    altitude = Column(Integer)
    url = Column(String)

    races = relationship("race", backref='circuit')

class constructor(Base):
   
    __tablename__ = "constructor"

    constructorId = Column(Integer, primary_key = True, index = True)
    constructorRef = Column(String, index = True)
    constructorName = Column(String, index = True)
    nationality = Column(String, index = True)
    url = Column(String)

class driver(Base):

    __tablename__ = "driver"

    driverId = Column(Integer, primary_key = True, index = True)
    driverRef = Column(String, index = True)
    driverNumber = Column(String, index = True)
    driverCode = Column(String, index = True)
    driverName = Column(String, index = True)
    dob = Column(String)
    nationality = Column(String, index = True)
    url = Column(String)

class race(Base):

    __tablename__ = "race"

    raceId = Column(Integer, primary_key = True, index = True)
    raceYear = Column(Integer, index = True)
    round = Column(Integer)
    circuitId = Column(Integer, ForeignKey("circuit.circuitId"))
    raceName = Column(String, index = True)
    raceDate = Column(String)
    raceTime = Column(String)
    url = Column(String)

class qualify(Base):

    __tablename__ = "qualify"

    qualifyId = Column(Integer, primary_key = True, index = True)
    raceId = Column(Integer, ForeignKey("race.raceId"))
    driverId = Column(Integer, ForeignKey("driver.driverId"))
    constructorId = Column(Integer, ForeignKey("constructor.constructorId"))
    qualifyNumber = Column(Integer, index = True)
    position = Column(Integer)
    q1 = Column(String)
    q2 = Column(String)
    q3 = Column(String)

class lap_time(Base):

    __tablename__ = "lap_time"

    laptimeId = Column(Integer, primary_key = True, index = True)
    raceId = Column(Integer, ForeignKey("race.raceId"))
    driverId = Column(Integer, ForeignKey("driver.driverId"))
    laptimeStop = Column(Integer, index = True)
    laptimeTime = Column(Integer, index = True)
    duration = Column(String)
    milliseconds = Column(Integer)

class result(Base):

    __tablename__ = "result"

    resultId = Column(Integer, primary_key = True, index = True)
    raceId = Column(Integer, ForeignKey("race.raceId"))
    driverId = Column(Integer, ForeignKey("driver.driverId"))
    constructorId = Column(Integer, ForeignKey("constructor.constructorId"))
    result_number = Column(String, index = True)
    grid = Column(Integer)
    position = Column(String, index = True)
    positionText = Column(String)
    positionOrder = Column(Integer)
    points = Column(Float)
    laps = Column(Integer, index = True)
    resultTime = Column(String)
    milliseconds = Column(String)
    fastestLap = Column(String)
    resultRank = Column(String)
    fastestLapTime = Column(String)
    fastestLapSpeed = Column(String)
    statusId = Column(Integer)

class pitstop(Base):

    __tablename__ = "pitstop"

    pitstopId = Column(Integer, primary_key = True, index = True)
    raceId = Column(Integer, ForeignKey("race.raceId"))
    driverId = Column(Integer, ForeignKey("driver.driverId"))
    pitstopStop = Column(Integer, index = True)
    lap = Column(Integer)
    pitstopTime = Column(String)
    duration = Column(String)
    milliseconds = Column(Integer)

