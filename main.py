from fastapi import FastAPI
import models
from database import engine
from routes import user, inventory

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Retail Operations Platform")

app.include_router(user.router)
app.include_router(inventory.router)

@app.get("/")
def root():
    return {"message": "Omni-Channel Retail Platform Running"}
