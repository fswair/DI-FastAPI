from fastapi import FastAPI, HTTPException

from injection import UserValidation, USDPrice

app = FastAPI()

@app.get("/profile")
async def read_root(user_validation: UserValidation):
    status, message = user_validation
    if status is False:
        raise HTTPException(status_code=401, detail=message)
    return {"message": "Welcome to your profile!", "user": message}

@app.get("/services/exchange_rates/converter")
async def calculate_usd_amount(
    try_amount: float,
    usd_price: USDPrice,
    user_validation: UserValidation,
):
    status, message = user_validation
    if status is False:
        message = f"This endpoint requires authentication. Details: {message}"
        raise HTTPException(status_code=401, detail=message)
    
    if try_amount < 0:
        raise HTTPException(status_code=400, detail="TRY amount must be a positive number")
    
    usd_amount = try_amount / usd_price if usd_price > 0 else 0.0
    return {"usd_amount": usd_amount, "usd_price": usd_price}