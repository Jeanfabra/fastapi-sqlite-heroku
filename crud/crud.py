from sqlalchemy.orm import Session
from sqlalchemy import func, distinct, select, literal, or_, and_, desc
from models import models
from schemas import schemas


'''Functions for: 
   1. Year with the most races
   2. Driver with the most first places
   3. Name of the most run circuit
   4. Driver with the highest number of points in total 
    whose constructor is American or British nationality'''


# Query #1
def get_year_most_races(db: Session):
    result = db.query((models.race.raceYear).label("year"), 
        func.count().label("Count")).group_by("year").order_by(desc("Count")).first()
    return result

# Query #2
def get_best_driver(db: Session):
    result = db.query((models.driver.driverName).label("DriverName"), 
        func.count(models.qualify.position).label("Count"),
        ).select_from(models.driver).join(models.qualify, models.qualify.driverId == models.driver.driverId,
        ).filter(models.qualify.position == 1).group_by("DriverName").order_by(desc("Count")).first()

    return result

# Query #3
def get_most_run(db: Session):
    result = db.query((models.circuit.circuitName).label("CircuitName"), func.count(models.circuit.circuitId).label("Count"),
          ).select_from(models.circuit).join(models.race, models.race.circuitId == models.circuit.circuitId,
          ).group_by("CircuitName").order_by(desc("Count")).first()

    return result

# Query #4
def get_best_points(db: Session):
    result = db.query((models.driver.driverName).label("DriverName"), func.sum(models.result.points).label("TotalPoints"),
        ).select_from(models.driver).join(models.result, models.result.driverId == models.driver.driverId,
        ).join(models.constructor, models.constructor.constructorId == models.result.constructorId,
        ).filter(or_(models.constructor.nationality == "British", models.constructor.nationality == "American"),
        ).group_by("DriverName").order_by(desc("TotalPoints")).first()

    return result
# ---------------------------------------------------------------------------------------------- #

def get_circuits(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.circuit).offset(skip).limit(limit).all()

def get_circuit(db: Session, circuitId: int):
    return db.query(models.circuit).filter(models.circuit.circuitId == circuitId).first()

def get_constructors(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.constructor).offset(skip).limit(limit).all()

def get_races(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.race).offset(skip).limit(limit).all()

def get_drivers(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.driver).offset(skip).limit(limit).all()

def get_qualifies(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.qualify).offset(skip).limit(limit).all()

def get_laptimes(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.lap_time).offset(skip).limit(limit).all()

def get_results(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.result).offset(skip).limit(limit).all()

def get_pitstops(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.pitstop).offset(skip).limit(limit).all()





