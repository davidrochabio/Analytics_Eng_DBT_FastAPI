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

async def get_order(id_order: int, db: "Session"):
    order = db.query(models.Orders).filter(models.Orders.id_order == id_order).first()
    return order

async def get_orders_by_month(month: str, db: "Session") -> List[schemas.Orders]:
    orders_by_month = db.query(models.Orders).filter(models.Orders.month.match(f'%{month}%')).all()
    return list(map(schemas.Orders.from_orm, orders_by_month))

async def get_orders_by_city(city: str, db: "Session") -> List[schemas.Orders]:
    orders_by_city = db.query(models.Orders).filter(models.Orders.city.match(f'%{city}%')).all()
    return list(map(schemas.Orders.from_orm, orders_by_city))

async def get_orders_by_state(state: str, db: "Session") -> List[schemas.Orders]:
    state = state.upper()
    orders_by_state = db.query(models.Orders).filter(models.Orders.state.match(f'%{state}%')).all()
    return list(map(schemas.Orders.from_orm, orders_by_state))

async def get_orders_by_region(region: str, db: "Session") -> List[schemas.Orders]:
    orders_by_region = db.query(models.Orders).filter(models.Orders.region.match(f'%{region}%')).all()
    return list(map(schemas.Orders.from_orm, orders_by_region))

# orders_products

async def get_all_orders_products(db: "Session") -> List[schemas.OrdersProducts]:
    orders_products = db.query(models.OrdersProducts).all()
    return list(map(schemas.OrdersProducts.from_orm, orders_products))

async def get_order_p(id_order: int, db: "Session") -> List[schemas.OrdersProducts]:
    order = db.query(models.OrdersProducts).filter(models.OrdersProducts.id_order == id_order).all()
    return list(map(schemas.OrdersProducts.from_orm, order))

async def get_product_o(id_product: int, db: "Session") -> List[schemas.OrdersProducts]:
    product = db.query(models.OrdersProducts).filter(models.OrdersProducts.id_product == id_product).all()
    return list(map(schemas.OrdersProducts.from_orm, product))