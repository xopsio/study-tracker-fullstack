from sqlalchemy.orm import Session
from . import models

def get_studies(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Study).offset(skip).limit(limit).all()

# Lisää muita CRUD-funktioita tarpeen mukaan
