from typing import TYPE_CHECKING, List
import fastapi
import sqlalchemy.orm as orm

import schemas
import services

if TYPE_CHECKING:
    from sqlalchemy.orm import Session

description = """

- The lanaguage of the actual data inside the tables is Portuguese-BR

- DB schema:

    orders connects to orders_products on id_order, and orders_products connects to products on id_products

- Check the schema of the table and the data type of the field you want to query

- Search fields (string) -> utilize the logical or = | and logical and = & operators to separate words

    Example: search products by name -> query = ryzen & 5 or search by product catgeory -> query = mouse | teclado

    products.category, products.name

    orders.month, orders.city, orders.state, orders.region

"""

tags_metadata = [
    {
        "name": "products",
        "description": "Pichau products table",
    },
    {
        "name": "orders",
        "description": "Pichau orders table.",
    },
    {
        "name": "orders_products",
        "description": "Pichau orders_products table that makes the connection to products and orders tables",
    },
]
    
app = fastapi.FastAPI(title='PostgreSQL API 🚀', description=description, openapi_tags=tags_metadata)

# products

@app.get("/pichau/products/", tags=['products'], response_model=List[schemas.Products])
async def get_all_products(db: orm.Session = fastapi.Depends(services.get_db)):
    return await services.get_all_products(db=db)

@app.get("/pichau/products/id_products/{id_products}/", tags=['products'], response_model=schemas.Products)
async def get_product(id_product: int, db: orm.Session = fastapi.Depends(services.get_db)):
    return await services.get_product(id_product=id_product, db=db)

@app.get("/pichau/products/category/{category}}", tags=['products'], response_model=List[schemas.Products])
async def get_products_by_category(category: str, db: orm.Session = fastapi.Depends(services.get_db)):
    return await services.get_products_by_category(category=category, db=db)

@app.get("/pichau/products/name/{name}}", tags=['products'], response_model=List[schemas.Products])
async def get_products_by_name(name: str, db: orm.Session = fastapi.Depends(services.get_db)):
    return await services.get_products_by_name(name=name, db=db)

# orders

@app.get("/pichau/orders/", tags=['orders'], response_model=List[schemas.Orders])
async def get_all_orders(db: orm.Session = fastapi.Depends(services.get_db)):
    return await services.get_all_orders(db=db)

@app.get("/pichau/orders/id_order/{id_order}/", tags=['orders'], response_model=schemas.Orders)
async def get_order(id_order: int, db: orm.Session = fastapi.Depends(services.get_db)):
    return await services.get_order(id_order=id_order, db=db)

@app.get("/pichau/orders/month/{month}}", tags=['orders'], response_model=List[schemas.Orders])
async def get_orders_by_month(month: str, db: orm.Session = fastapi.Depends(services.get_db)):
    return await services.get_orders_by_month(month=month, db=db)

@app.get("/pichau/orders/city/{city}}", tags=['orders'], response_model=List[schemas.Orders])
async def get_orders_by_city(city: str, db: orm.Session = fastapi.Depends(services.get_db)):
    return await services.get_orders_by_city(city=city, db=db)

@app.get("/pichau/orders/state/{state}}", tags=['orders'], response_model=List[schemas.Orders])
async def get_orders_by_state(state: str, db: orm.Session = fastapi.Depends(services.get_db)):
    return await services.get_orders_by_state(state=state, db=db)

@app.get("/pichau/orders/region/{region}}", tags=['orders'], response_model=List[schemas.Orders])
async def get_orders_by_region(region: str, db: orm.Session = fastapi.Depends(services.get_db)):
    return await services.get_orders_by_region(region=region, db=db)

# orders_products

@app.get("/pichau/orders_products/", tags=['orders_products'], response_model=List[schemas.OrdersProducts])
async def get_all_orders_products(db: orm.Session = fastapi.Depends(services.get_db)):
    return await services.get_all_orders_products(db=db)

@app.get("/pichau/orders_products/id_order/{id_order}/", tags=['orders_products'], response_model=List[schemas.OrdersProducts])
async def get_order_p(id_order: int, db: orm.Session = fastapi.Depends(services.get_db)):
    return await services.get_order_p(id_order=id_order, db=db)

@app.get("/pichau/porders_products/id_product/{id_product}/", tags=['orders_products'], response_model=List[schemas.OrdersProducts])
async def get_product_o(id_product: int, db: orm.Session = fastapi.Depends(services.get_db)):
    return await services.get_product_o(id_product=id_product, db=db)