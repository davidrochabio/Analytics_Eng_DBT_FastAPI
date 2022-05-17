from typing import TYPE_CHECKING, List
import fastapi
import sqlalchemy.orm as orm

import schemas
import services

if TYPE_CHECKING:
    from sqlalchemy.orm import Session
    
import time
time.sleep(60)

description = """

- The language of the actual data inside the tables is Portuguese-BR

Searching queries: search products by name -> query = "ryzen & 5" or search by product category -> query = "mouse | teclado"

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
        "name": "orders_details",
        "description": "Pichau orders_details table that makes the connection to products and orders tables",
    },
    {
        "name": "dates_dim",
        "description": "dates dimension view",
    },
    {
        "name": "locations_dim",
        "description": "locations dimension view",
    },
    {
        "name": "products_dim",
        "description": "products dimension view",
    },
    {
        "name": "orders_fact",
        "description": "orders fact view",
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

# orders_details

@app.get("/pichau/orders_details/", tags=['orders_details'], response_model=List[schemas.OrdersDetails])
async def get_all_orders_details(db: orm.Session = fastapi.Depends(services.get_db)):
    return await services.get_all_orders_details(db=db)

@app.get("/pichau/orders_details/id_order/{id_order}/", tags=['orders_details'], response_model=List[schemas.OrdersDetails])
async def get_order_p(id_order: int, db: orm.Session = fastapi.Depends(services.get_db)):
    return await services.get_order_p(id_order=id_order, db=db)

@app.get("/pichau/orders_details/id_product/{id_product}/", tags=['orders_details'], response_model=List[schemas.OrdersDetails])
async def get_product_o(id_product: int, db: orm.Session = fastapi.Depends(services.get_db)):
    return await services.get_product_o(id_product=id_product, db=db)

# DW views

@app.get("/pichau/dates_dim/", tags=['dates_dim'], response_model=List[schemas.DatesDim])
async def get_dates_dim(db: orm.Session = fastapi.Depends(services.get_db)):
    return await services.get_dates_dim(db=db)

@app.get("/pichau/locations_dim/", tags=['locations_dim'], response_model=List[schemas.LocationsDim])
async def get_locations_dim(db: orm.Session = fastapi.Depends(services.get_db)):
    return await services.get_locations_dim(db=db)

@app.get("/pichau/products_dim/", tags=['products_dim'], response_model=List[schemas.ProductsDim])
async def get_products_dim(db: orm.Session = fastapi.Depends(services.get_db)):
    return await services.get_products_dim(db=db)

@app.get("/pichau/orders_fact/", tags=['orders_fact'], response_model=List[schemas.OrdersFact])
async def get_orders_fact(db: orm.Session = fastapi.Depends(services.get_db)):
    return await services.get_orders_fact(db=db)