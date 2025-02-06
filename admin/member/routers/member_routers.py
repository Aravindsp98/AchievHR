from fastapi import APIRouter,Depends

from sqlalchemy.orm import Session

from admin.member.services.member_services import get_all_employees
from admin.member.schemas.member_schemas import EmployeeCreate

from admin.database import get_db


router = APIRouter()

@router.get("/employees/", response_model=list[EmployeeCreate])  
def list_employees(db: Session = Depends(get_db)):
    employees = get_all_employees(db=db)
    return employees