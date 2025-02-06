from typing import Optional
from pydantic import BaseModel
from datetime import date

class EmployeeCreate(BaseModel):
    prefix: str
    firstname: str
    middlename: str
    lastname: str
    employee_code: str
    dob: date 
    gender: str  
    nationality: str  
    work_email: str 
    biometric_id: str = None 
    isd_code: str = None 
    mobile_number: str = None  



class EmployeeUpdate(BaseModel):
    prefix: Optional[str] = None
    firstname: Optional[str] = None
    middlename: Optional[str] = None
    lastname: Optional[str] = None
    employee_code: Optional[str] = None
    dob: Optional[date] = None
    gender: Optional[str] = None
    nationality: Optional[str] = None
    biometric_id: Optional[str] = None
    isd_code: Optional[str] = None
    mobile_number: Optional[str] = None