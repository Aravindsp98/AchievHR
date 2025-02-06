from fastapi import Depends, Header, Request, HTTPException
from pydantic import BaseModel

from fastapi.middleware.cors import CORSMiddleware

from fastapi import FastAPI, HTTPException
from fastapi.security import OAuth2PasswordBearer
import jwt
from jwt import ExpiredSignatureError, InvalidTokenError
import jwt







# async def check_authentication(x_token: str = Header(...)):
#     if not x_token:
#         raise HTTPException(status_code=400, detail="Token is required")
    
#     try:
#         # Decode the JWT token without verifying the signature
#         payload = jwt.decode(x_token, options={"verify_signature": False})
#         family_name = payload.get("family_name")
#         given_name = payload.get("given_name")
#         username = payload.get("unique_name")
#         fullname = payload.get("name")

#         return {
#         "family_name": family_name,
#         "given_name": given_name,
#         "username":username,
#         "fullname":fullname
#     }   # Return the payload for further use in the endpoint

#     except jwt.ExpiredSignatureError:
#         raise HTTPException(status_code=401, detail="Token has expired")
#     except JWTError:
#         raise HTTPException(status_code=401, detail="Invalid token")




async def check_authentication(x_token: str = Header(...)):
    if not x_token:
        raise HTTPException(status_code=400, detail="Token is required")
    
    try:
       
        payload = jwt.decode(x_token, key=None, algorithms=["HS256"], options={"verify_signature": False})
        username = payload.get("unique_name")  
        if not username:
            raise HTTPException(status_code=400, detail="Username not found in token")

        return username 

    except ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token has expired")
    except InvalidTokenError as e:
        raise HTTPException(status_code=401, detail=str(e))
    


    