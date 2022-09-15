from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
from crud import crud
from models import models 
from schemas import schemas
from config import database
from config.database import SessionLocal, engine

models.Base.metadata.create_all(bind = engine)

app = FastAPI()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
async def get_docs():
    return "Welcome to Formula 1 Dataset API. Feel free to check the documentation (/docs)"

@app.get("/year-races")
def read_year_races(db: Session = Depends(get_db)):
    year_races = crud.get_year_most_races(db)
    return year_races

@app.get("/best-driver")
def read_best_driver(db: Session = Depends(get_db)):
    best_driver = crud.get_best_driver(db)
    return best_driver

@app.get("/most-run")
def read_most_run(db: Session = Depends(get_db)):
    most_run = crud.get_most_run(db)
    return most_run

@app.get("/best-score")
def read_best_score(db: Session = Depends(get_db)):
    best_score = crud.get_best_points(db)
    return best_score

# ------------------------------------------------------------------------------------------- #

@app.get("/circuits", response_model = list[schemas.circuit])
def read_circuits(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    try:
        circuits = crud.get_circuits(db, skip = skip, limit = limit)
        return circuits
    except HTTPException as e:
        return e

@app.get("/circuits/{circuitId}", response_model = schemas.circuit)
def read_circuit(circuitId: int, db: Session = Depends(get_db)):
    circuit = crud.get_circuit(db, circuitId = circuitId)
    return circuit

@app.get("/constructors", response_model = list[schemas.constructor])
def read_constructors(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    constructors = crud.get_constructors(db, skip = skip, limit = limit)
    return constructors


@app.get("/races", response_model = list[schemas.race])
def read_races(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    races = crud.get_races(db, skip = skip, limit = limit)
    return races

@app.get("/results", response_model = list[schemas.result])
def read_result(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    results = crud.get_results(db, skip = skip, limit = limit)
    return results

@app.get("/drivers", response_model = list[schemas.driver])
def read_drivers(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    drivers = crud.get_drivers(db, skip = skip, limit = limit)
    return drivers

@app.get("/qualifies", response_model = list[schemas.qualify])
def read_qualifies(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    qualifies = crud.get_qualifies(db, skip = skip, limit = limit)
    return qualifies

@app.get("/laptimes", response_model = list[schemas.lap_time])
def read_laptimes(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    laptimes = crud.get_laptimes(db, skip = skip, limit = limit)
    return laptimes

@app.get("/pitstops", response_model = list[schemas.pitstop])
def read_pitstops(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    pitstops = crud.get_pitstops(db, skip = skip, limit = limit)
    return pitstops



