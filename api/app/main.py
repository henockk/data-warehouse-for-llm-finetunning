from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from . import crud, models, schemas
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/raw_data/", response_model=schemas.RawData)
def create_raw_data(raw_data: schemas.RawDataCreate, db: Session = Depends(get_db)):
    return crud.create_raw_data(db=db, raw_data=raw_data)

@app.get("/raw_data/{data_id}", response_model=schemas.RawData)
def read_raw_data(data_id: int, db: Session = Depends(get_db)):
    db_raw_data = crud.get_raw_data(db, data_id=data_id)
    if db_raw_data is None:
        raise HTTPException(status_code=404, detail="Data not found")
    return db_raw_data

@app.get("/raw_data/source/{source}", response_model=list[schemas.RawData])
def read_raw_data_by_source(source: str, db: Session = Depends(get_db)):
    return crud.get_raw_data_by_source(db, source=source)
