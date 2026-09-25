from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.auth.utils import get_current_user, require_admin
from app.database import get_db
from app.models import Doctor, Patient, User
from app.schemas import PatientCreate, PatientResponse, PatientUpdate


router = APIRouter()


# =========================
# Create Patient
# =========================

@router.post(
    "/",
    response_model=PatientResponse,
    status_code=status.HTTP_201_CREATED
)
def create_patient(
    patient_data: PatientCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    new_patient = Patient(
        name=patient_data.name,
        age=patient_data.age,
        phone=patient_data.phone
    )

    db.add(new_patient)
    db.commit()
    db.refresh(new_patient)

    return new_patient


# =========================
# Get All Patients
# Admin → All patients
# Doctor → Assigned patients only
# =========================

@router.get(
    "/",
    response_model=list[PatientResponse]
)
def get_patients(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    if current_user.role == "admin":
        patients = db.query(Patient).all()

    elif current_user.role == "doctor":

        if not current_user.doctor:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Doctor profile not found"
            )

        patients = db.query(Patient).filter(
            Patient.doctor_id == current_user.doctor.id
        ).all()

    else:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Access denied"
        )

    return patients


# =========================
# Get Patient By ID
# Admin → Any patient
# Doctor → Assigned patient only
# =========================

@router.get(
    "/{patient_id}",
    response_model=PatientResponse
)
def get_patient(
    patient_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    patient = db.query(Patient).filter(
        Patient.id == patient_id
    ).first()

    if not patient:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Patient not found"
        )

    # Admin can access any patient
    if current_user.role == "admin":
        return patient

    # Doctor can access only assigned patients
    if current_user.role == "doctor":

        if not current_user.doctor:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Doctor profile not found"
            )

        if patient.doctor_id != current_user.doctor.id:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="You can access only your assigned patients"
            )

        return patient

    raise HTTPException(
        status_code=status.HTTP_403_FORBIDDEN,
        detail="Access denied"
    )


# =========================
# Update Patient
# Admin → Any patient
# Doctor → Assigned patient only
# =========================

@router.put(
    "/{patient_id}",
    response_model=PatientResponse
)
def update_patient(
    patient_id: int,
    patient_data: PatientUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    patient = db.query(Patient).filter(
        Patient.id == patient_id
    ).first()

    if not patient:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Patient not found"
        )

    # Doctor access check
    if current_user.role == "doctor":

        if not current_user.doctor:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Doctor profile not found"
            )

        if patient.doctor_id != current_user.doctor.id:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="You can update only your assigned patients"
            )

    elif current_user.role != "admin":
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Access denied"
        )

    patient.name = patient_data.name
    patient.age = patient_data.age
    patient.phone = patient_data.phone

    db.commit()
    db.refresh(patient)

    return patient


# =========================
# Assign Patient To Doctor
# Admin Only
# =========================

@router.put(
    "/{patient_id}/assign-doctor/{doctor_id}",
    response_model=PatientResponse
)
def assign_patient_to_doctor(
    patient_id: int,
    doctor_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(require_admin)
):
    patient = db.query(Patient).filter(
        Patient.id == patient_id
    ).first()

    if not patient:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Patient not found"
        )

    doctor = db.query(Doctor).filter(
        Doctor.id == doctor_id,
        Doctor.is_active == True
    ).first()

    if not doctor:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Doctor not found"
        )

    patient.doctor_id = doctor.id

    db.commit()
    db.refresh(patient)

    return patient