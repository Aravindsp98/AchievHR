from fastapi import APIRouter, FastAPI, FastAPI, Request, HTTPException,Depends
from fastapi.responses import RedirectResponse
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from fastapi.openapi.utils import get_openapi
from sqlalchemy.orm import Session


from admin.database import get_db

# Create a router object
router = APIRouter()


# Dependency function to validate authentication
async def get_authenticated_user(request: Request):
    """
    Dependency function to check if the user is authenticated.

    Args:
        request (Request): The incoming request.

    Returns:
        str: The authenticated user's email.

    Raises:
        HTTPException: If the user is not authenticated.
    """
    # For testing in Swagger UI, allow a fallback email
    if "swagger-ui" in request.headers.get("user-agent", "").lower():
        email = request.headers.get("X-Forwarded-Email", "test@example.com")
        return email



    # Get the email from the request headers (forwarded by OAuth2 Proxy)
    email = request.headers.get("X-Forwarded-Email") or request.headers.get("X-Auth-Request-Email")

    # Check if the email is present
    if not email:
        raise HTTPException(status_code=401, detail="Unauthorized")

    # Return the authenticated user's email
    return email

# Secured endpoint 1
@router.get("/secured-items/")
async def secure_data(email: str = Depends(get_authenticated_user)):
    """
    A secured endpoint that requires authentication.

    Args:
        email (str): The authenticated user's email (from the dependency).

    Returns:
        dict: A dictionary containing a message and the user's email.
    """
    return {
        "message": "Hello, authenticated admin!",
        "email": email
    }

# Secured endpoint 2
@router.get("/another-secured-endpoint/")
async def another_secure_endpoint(email: str = Depends(get_authenticated_user)):
    """
    Another secured endpoint that requires authentication.

    Args:
        email (str): The authenticated user's email (from the dependency).

    Returns:
        dict: A dictionary containing a message and the user's email.
    """
    return {
        "message": "This is another secured endpoint of admin service!",
        "email": email
    }


