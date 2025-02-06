from sqlalchemy.orm import Session
from sqlalchemy import text




def get_all_employees(db: Session):
    query = text("SELECT id, name, username FROM employees")  
    result = db.execute(query).fetchall()
    
    return [{"id": row.id, "name": row.name, "username": row.username} for row in result]