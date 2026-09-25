from fastapi import FastAPI

from app.database import Base, engine
from app import models

from app.auth import router as auth_router
from app.routers import doctors, patients


Base.metadata.create_all(bind=engine)


app = FastAPI(
    title="Doctor Patient Management API",
    version="1.0.0"
)


app.include_router(
    auth_router.router,
    prefix="/auth",
    tags=["Authentication"]
)


app.include_router(
    doctors.router,
    prefix="/doctors",
    tags=["Doctors"]
)


app.include_router(
    patients.router,
    prefix="/patients",
    tags=["Patients"]
)


@app.get("/")
def root():
    return {
        "message": "Doctor Patient API is running"
    }