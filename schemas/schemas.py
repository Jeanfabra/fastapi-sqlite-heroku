from typing import Union
from pydantic import BaseModel

'''Creating Pydantic models (schemas) that will be used
   when reading data, when returning it from the API.
   Config Class is used to provide configurations to Pydantic'''

# Circuit
class circuitBase(BaseModel):
    circuitRef: str
    circuitName: str 
    location: str
    country: str
    latitude: float 
    longitude: float
    altitude: int
    url: str

class circuitCreate(circuitBase):
    pass

class circuit(circuitBase):
    circuitId: int

    class Config:
        orm_mode = True

# Constructor
class constructorBase(BaseModel):
    constructorRef: str
    constructorName: str
    nationality: str
    url: str

class constructorCreate(constructorBase):
    pass

class constructor(constructorBase):
    constructorId: int

    class Config:
        orm_mode = True    

# Driver
class driverBase(BaseModel):
    driverRef: str
    driverCode: str
    driverName: str
    dob: str
    nationality: str
    url: str

class driverCreate(driverBase):
    pass

class driver(driverBase):
    driverId: int

    class Config:
        orm_mode = True

# Race
class raceBase(BaseModel):
    raceYear: int
    round: int
    raceName: str
    raceDate: str
    raceTime: str
    url: str

class raceCreate(raceBase):
    pass

class race(raceBase):
    raceId: int
    circuitId: int

    class Config:
        orm_mode = True

# Qualify
class qualifyBase(BaseModel):
    qualifyNumber: int
    position: int
    q1: str
    q2: str
    q3: str

class qualifyCreate(qualifyBase):
    pass

class qualify(qualifyBase):
    qualifyId: int
    raceId: int
    driverId: int
    constructorId: int

    class Config:
        orm_mode = True

# Lap_time
class lap_timeBase(BaseModel):
    laptimeStop: int
    laptimeTime: int
    duration: str
    milliseconds: int

class lap_timeCreate(lap_timeBase):
    pass

class lap_time(lap_timeBase):
    laptimeId: int
    raceId: int
    driverId: int

    class Config:
        orm_mode = True

# Result
class resultBase(BaseModel):
    result_number: str
    grid: int
    position: str
    positionText: str
    positionOrder: int
    points: float
    laps: int
    resultTime: str
    milliseconds: str
    fastestLap: str
    resultRank: str
    fastestLapTime: str
    fastestLapSpeed: str
    statusId: int

class resultCreate(resultBase):
    pass

class result(resultBase):
    resultId: int
    raceId: int
    driverId: int
    constructorId: int

    class Config:
        orm_mode = True

class pitstopBase(BaseModel):
    pitstopStop: int
    lap: int
    pitstopTime: str
    duration: str
    milliseconds: int

class pitstopCreate(pitstopBase):
    pass

class pitstop(pitstopBase):
    pitstopId: int
    raceId: int
    driverId: int

    class Config:
        orm_mode = True


