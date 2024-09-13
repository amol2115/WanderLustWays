from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal, engine, Base
from .models import Hotel


app = FastAPI()

Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/hotels/")
def read_hotels(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    hotels = db.query(Hotel).offset(skip).limit(limit).all()
    return hotels

@app.post("/hotels/")
def create_hotel(hotel: Hotel, db: Session = Depends(get_db)):
    db.add(hotel)
    db.commit()
    db.refresh(hotel)
    return hotel
