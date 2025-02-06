from fastapi import FastAPI, FastAPI, Request, HTTPException,Depends
from fastapi.responses import RedirectResponse
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from fastapi.openapi.utils import get_openapi
from user.authentication.routers import auth_user_route
from user.database import init_db
from user.employee.routers import employee_routers

DATABASE_URL = "postgresql://postgres:postgres@localhost:5433/achievhr_db"


init_db()

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

app = FastAPI(title="User", 
    version="1.0.0")

app.include_router(auth_user_route.user_router, prefix="/auth", tags=["auth"])
app.include_router(employee_routers.router, prefix="/employee", tags=["Employee"])

class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)

@app.get("/")
async def read_root():
    return {"Hello": "World"}





