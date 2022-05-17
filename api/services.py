from typing import TYPE_CHECKING, List

import database
import models
import schemas

if TYPE_CHECKING:
    from sqlalchemy.orm import Session

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

# source tables
# products
        
async def get_all_products(db: "Session") -> List[schemas.Products]:
    products = db.query(models.Products).all()
    return list(map(schemas.Products.from_orm, products))

async def get_product(id_product: int, db: "Session"):
    product = db.query(models.Products).filter(models.Products.id_product == id_product).first()
    return product

async def get_products_by_name(name: str, db: "Session") -> List[schemas.Products]:
    products_by_name = db.query(models.Products).filter(models.Products.name.match(f'%{name}%')).all()
    return list(map(schemas.Products.from_orm, products_by_name))

async def get_products_by_category(category: str, db: "Session") -> List[schemas.Products]:
    products_by_category = db.query(models.Products).filter(models.Products.category.match(f'%{category}%')).all()
    return list(map(schemas.Products.from_orm, products_by_category))

# orders

async def get_all_orders(db: "Session") -> List[schemas.Orders]:
    orders = db.query(models.Orders).all()
    return list(map(schemas.Orders.from_orm, orders))

async def get_order(id_order: str, db: "Session"):
    order = db.query(models.Orders).filter(models.Orders.id_order == id_order).first()
    return order

# orders_details

async def get_all_orders_details(db: "Session") -> List[schemas.OrdersDetails]:
    orders_details = db.query(models.OrdersDetails).all()
    return list(map(schemas.OrdersDetails.from_orm, orders_details))

async def get_order_p(id_order: int, db: "Session") -> List[schemas.OrdersDetails]:
    order = db.query(models.OrdersDetails).filter(models.OrdersDetails.id_order == id_order).all()
    return list(map(schemas.OrdersDetails.from_orm, order))

async def get_product_o(id_product: int, db: "Session") -> List[schemas.OrdersDetails]:
    product = db.query(models.OrdersDetails).filter(models.OrdersDetails.id_product == id_product).all()
    return list(map(schemas.OrdersDetails.from_orm, product))

# DW views

async def get_dates_dim(db: "Session") -> List[schemas.DatesDim]:
    dates_dim = db.query(models.DatesDim).all()
    return list(map(schemas.DatesDim.from_orm, dates_dim))

async def get_locations_dim(db: "Session") -> List[schemas.LocationsDim]:
    locations_dim = db.query(models.LocationsDim).all()
    return list(map(schemas.LocationsDim.from_orm, locations_dim))

async def get_products_dim(db: "Session") -> List[schemas.ProductsDim]:
    products_dim = db.query(models.ProductsDim).all()
    return list(map(schemas.ProductsDim.from_orm, products_dim))

async def get_orders_fact(db: "Session") -> List[schemas.OrdersFact]:
    orders_fact = db.query(models.OrdersFact).all()
    return list(map(schemas.OrdersFact.from_orm, orders_fact))