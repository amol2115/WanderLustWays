
from sqlalchemy import Column, String, Integer, Float, Boolean  
from sqlalchemy.ext.declarative import declarative_base 
from sqlalchemy.orm import sessionmaker 
from sqlalchemy import create_engine 

class TouristSpot(Base):
    __tablename__ = "tourist_spots"

    id = Column(Integer, primary_key=True, index=True)
    zone = Column(String, nullable=False)
    state = Column(String, nullable=False)
    city = Column(String, nullable=False)
    name = Column(String, nullable=False)
    type = Column(String, nullable=False)  
    establishment_year = Column(Integer)  
    time_needed_to_visit_hrs = Column(Float)  
    google_review_rating = Column(Float) 
    entrance_fee_in_inr = Column(Integer)  
    airport_within_50km = Column(Boolean)  
    weekly_off = Column(String)  
    significance = Column(String)  
    dslr_allowed = Column(Boolean)  
    number_of_google_reviews_lakhs = Column(Float)
    best_time_to_visit = Column(String) 
Base.metadata.create_all(bind=engine)
