from fastapi import FastAPI
from admin.authentication.routers import auth_route
from admin.member.routers import member_routers
from admin.database import init_db 

app = FastAPI(
    title="Admin",
    version="1.0.0"
)

app.include_router(auth_route.router, prefix="/auth", tags=["Auth"])
app.include_router(member_routers.router, prefix="/member", tags=["Member"])


# Create tables on startup
@app.on_event("startup")
def startup_event():
    init_db()