# FastAPI Dependency Injection Example

An example about use-case of DI in FastAPI application.

# Using Depends in FastAPI App

```python3
async def validate_user(token: str = Query(), db: T = Depends(get_db)):
    return await user_api.validate(token)

@app.get("/")
async def home(user_validation: T = Depends(validate_user)):
    return await user_validation.result()
```

# Annotated Dependency Specification

```python3
ValidateUserDepsT = Annotated[T, Depends(validate_user)]
```

...and then:

```python3
@app.get("/")
async def home(user_validation: ValidateUserDepsT):
    return await user_validation.result()
```

# Test

Test the project by running following commands:

**Start the server:**

```sh 
make serve
```

**Install requirements:**

```sh 
make install
```

**Run tests:**

```sh 
make test
```
