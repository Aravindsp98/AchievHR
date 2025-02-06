from sqlalchemy import Column, Integer, String
from user.database import Base 

from sqlalchemy import Column, Integer, String, Date

class Employee(Base):
    __tablename__ = "employees"

    id = Column(Integer, primary_key=True, index=True)
    prefix = Column(String, index=True)
    firstname = Column(String, index=True)
    middlename = Column(String, index=True)
    lastname = Column(String, index=True)  
    employee_code = Column(String, index=True)
    dob = Column(Date, nullable=False)  
    gender = Column(String, nullable=False)  
    nationality = Column(String, nullable=False)  
    work_email = Column(String, unique=True, nullable=False) 
    biometric_id = Column(String, unique=True) 
    isd_code = Column(String) 
    mobile_number = Column(String)
