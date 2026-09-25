from typing import Optional

from pydantic import BaseModel, EmailStr, Field


# =========================
# Authentication Schemas
# =========================

class UserRegister(BaseModel):
    name: str
    email: EmailStr
    password: str = Field(min_length=6)
    role: str = "doctor"


class UserLogin(BaseModel):
    email: EmailStr
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str


# =========================
# Doctor Schemas
# =========================

class DoctorCreate(BaseModel):
    name: str
    specialization: str
    email: EmailStr
    is_active: bool = True


class DoctorResponse(BaseModel):
    id: int
    name: str
    specialization: str
    email: EmailStr
    is_active: bool

    class Config:
        from_attributes = True


# =========================
# Patient Schemas
# =========================

class PatientCreate(BaseModel):
    name: str
    age: int = Field(gt=0)
    phone: str = Field(
        min_length=10,
        max_length=15,
        pattern=r"^\d{10,15}$"
    )
class PatientUpdate(BaseModel):
    name: str
    age: int = Field(gt=0)
    phone: str = Field(
        min_length=10,
        max_length=15,
        pattern=r"^\d{10,15}$"
    )

class PatientResponse(BaseModel):
    id: int
    name: str
    age: int
    phone: str
    doctor_id: Optional[int] = None

    class Config:
        from_attributes = True

        