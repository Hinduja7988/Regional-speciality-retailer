from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import SessionLocal
import models, schemas

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/inventory")
def add_inventory(data: schemas.InventorySchema, db: Session = Depends(get_db)):
    item = models.Inventory(**data.dict())
    db.add(item)
    db.commit()
    return {"message": "Inventory added"}

@router.get("/inventory")
def get_inventory(db: Session = Depends(get_db)):
    items = db.query(models.Inventory).all()
    return items
