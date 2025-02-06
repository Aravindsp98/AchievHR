from fastapi import APIRouter, FastAPI, FastAPI, Request, HTTPException,Depends
from fastapi.responses import RedirectResponse
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from fastapi.openapi.utils import get_openapi
from sqlalchemy.orm import Session

from user.authentication.services.auth_user_services import check_authentication
from user.employee.schemas.employee_schemas import EmployeeCreate
from user.employee.services.employee_services import create_employee, get_employee, get_employee_by_username, update_employee_by_username
from user.database import get_db


router = APIRouter()

@router.post("/register/", response_model=EmployeeCreate)
def register_employee(employee: EmployeeCreate, db: Session = Depends(get_db)):
 
    return create_employee(db=db, employee=employee)


@router.get("/employee/{employee_id}", response_model=EmployeeCreate)
def read_employee(employee_id: int, db: Session = Depends(get_db)):
    db_employee = get_employee(db=db, employee_id=employee_id)
    if db_employee is None:
        raise HTTPException(status_code=404, detail="Employee not found")
    return db_employee

@router.get("/employees/me", response_model=EmployeeCreate)
async def read_employee_me(username: str = Depends(check_authentication), db: Session = Depends(get_db)):
    db_employee = get_employee_by_username(db=db, username=username)
    if db_employee is None:
        raise HTTPException(status_code=404, detail="Employee not found")
    return db_employee



@router.put("/employees/me", response_model=EmployeeCreate)
async def update_employee_me(
    employee: EmployeeCreate,
    username: str = Depends(check_authentication),
    db: Session = Depends(get_db)
):
    updated_employee = update_employee_by_username(
        db=db,
        username=username,
        employee=employee
    )
    if updated_employee is None:
        raise HTTPException(
            status_code=404,
            detail="Employee not found"
        )
    return updated_employee