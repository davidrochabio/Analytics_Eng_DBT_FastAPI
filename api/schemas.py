import pydantic

class Products(pydantic.BaseModel):
    index: int
    id_product: int
    name: str
    category: str
    price: float
    
    class Config:
        orm_mode = True
    
class Orders(pydantic.BaseModel):
    index: int
    id_order: int
    month: str
    city: str
    state: str
    region:str
    time_separate: float
    
    class Config:
        orm_mode = True
        
class OrdersProducts(pydantic.BaseModel):
    index: int
    id_order: int
    id_product: int
    quantity: int
    
    class Config:
        orm_mode = True