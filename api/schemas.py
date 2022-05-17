import pydantic
import datetime

from typing import Union

# source tables

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
    id_order: str
    date: datetime.datetime
    location_code: int
    time_separate: float
    
    class Config:
        orm_mode = True
        
class OrdersDetails(pydantic.BaseModel):
    index: int
    id_order: str
    id_product: int
    quantity: int
    
    class Config:
        orm_mode = True

# DW views

class DatesDim(pydantic.BaseModel):
    index: int
    date: datetime.datetime
    year: int
    quarter: int
    month: int
    day: int
    day_of_week: int
    hour: int
    
    class Config:
        orm_mode = True

class LocationsDim(pydantic.BaseModel):
    index: int
    location_code: int
    state: str
    city: str
    region: str
    population: Union[int, None] = None
    size: Union[str, None] = None
    capital: Union[str, None] = None
    
    class Config:
        orm_mode = True
    
class ProductsDim(pydantic.BaseModel):
    index: int
    id_product: int
    name: str
    category: str
    
    class Config:
        orm_mode = True

class OrdersFact(pydantic.BaseModel):
    index: int
    id_order: str
    date: datetime.datetime
    location_code: int
    id_product: int
    quantity: int
    unit_price : float
    prod_final_price:float
    
    class Config:
        orm_mode = True