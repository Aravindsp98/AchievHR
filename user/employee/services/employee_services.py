from fastapi import HTTPException
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError

from user.employee.schemas.employee_schemas import EmployeeCreate
from user.employee.models.employee_models import Employee


def create_employee(db: Session, employee: EmployeeCreate):
    db_employee = Employee(
        prefix=employee.prefix,
        firstname=employee.firstname,
        middlename=employee.middlename,
        lastname=employee.lastname,
        employee_code=employee.employee_code,
        dob=employee.dob,
        gender=employee.gender,
        nationality=employee.nationality,
        work_email=employee.work_email,
        biometric_id=employee.biometric_id,
        isd_code=employee.isd_code,
        mobile_number=employee.mobile_number
    )
    
    db.add(db_employee)
    db.commit()
    db.refresh(db_employee)
    
    return db_employee


def get_employee(db: Session, employee_id: int):
    return db.query(Employee).filter(Employee.id == employee_id).first()


def get_employee_by_username(db: Session, username: str):
    return db.query(Employee).filter(Employee.work_email == username).first()



def update_employee_by_username(
    db: Session,
    username: str,
    employee: EmployeeCreate
):
    db_employee = get_employee_by_username(db=db, username=username)
    
    if db_employee is None:
        return None
    
    # Update employee attributes while preserving the username/email
    update_data = employee.dict(exclude_unset=True)
    
    # Prevent updating work_email if it's used for authentication
    if 'work_email' in update_data:
        del update_data['work_email']
    
    for field, value in update_data.items():
        setattr(db_employee, field, value)
    
    try:
        db.commit()
        db.refresh(db_employee)
    except SQLAlchemyError as e:
        db.rollback()
        raise HTTPException(
            status_code=400,
            detail="Failed to update employee"
        )
    
    return db_employee