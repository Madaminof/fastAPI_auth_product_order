from pydantic import BaseModel

class UserCreate(BaseModel):
    username: str
    email: str
    password: str

class UserResponse(BaseModel):
    id: int
    username: str
    email: str

    class Config:
        orm_mode = True

class Product(BaseModel):
    name: str
    description: str
    price: int

    class Config:
        orm_mode = True

class OrderCreate(BaseModel):
    user_id: int
    product_id: int
    quantity: int

    class Config:
        orm_mode = True

class OrderResponse(BaseModel):
    id: int
    user_id: int
    product_id: int
    quantity: int

    class Config:
        orm_mode = True

class Login(BaseModel):
    username: str
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: str | None = None
