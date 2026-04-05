from pydantic import BaseModel

class UserCreate(BaseModel):
    email: str
    password: str

class UserLogin(BaseModel):
    email: str
    password: str

class ProductSchema(BaseModel):
    name: str
    price: int

class InventorySchema(BaseModel):
    product_id: int
    store_id: int
    quantity: int
