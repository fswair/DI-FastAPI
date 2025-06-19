from fastapi import Depends, Header
from typing import Optional, Annotated, TypeVar, Union

from services.usdprice import get_usd_price

MISSING  = TypeVar("MISSING")
NOTFOUND = TypeVar("NOTFOUND")

def fake_db():
    return {
        "bearer_venus": {
            "id": 1,
            "name": "Venus",
            "email": "info@example.com"
        }
    }

def get_user(db, bearer: str = None) -> Union[MISSING, NOTFOUND]:
    if bearer is None or not bearer:
        return MISSING
    return db.get(bearer, NOTFOUND)

def validate_user(authorization: Optional[str] = Header(None), db: dict = Depends(fake_db)):
    if authorization is None or not authorization:
        return False, "Authorization header is missing or empty"

    if not authorization.startswith("Bearer "):
        return False, "Authorization header must start with 'Bearer '"
    
    token = authorization[7:]
    
    user = get_user(db, token)
    
    if user is MISSING:
        return False, "Bearer token is missing or empty"
    
    if user is NOTFOUND:
        return False, "User not found in the database"
    
    return True, user


UserValidation = Annotated[
    tuple[bool, Union[dict, str]],
    Depends(validate_user)
]

USDPrice = Annotated[
    float,
    Depends(get_usd_price)
]