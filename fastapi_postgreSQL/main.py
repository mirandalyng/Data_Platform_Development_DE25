from fastapi import FastAPI, status
from psycopg_pool import ConnectionPool
from schema.product import ProductSchema
from psycopg.types.json import Json
from psycopg import Connection


DATABASE_URL = DATABASE_URL = "postgresql://postgres:mirandalyng@localhost:5433/lektion_5"

pool = ConnectionPool(DATABASE_URL)

app = FastAPI(title="Postgresql_fastapi")


@app.get("/")
def root() -> dict:
    return {"Hello": "world"}


@app.post(
    "/products",
    status_code=status.HTTP_201_CREATED,
    response_model=ProductSchema
)
def post_product(product: ProductSchema) -> ProductSchema:
    # Query -Insert
    with pool.connection() as conn:
        insert_product(conn, product.model_dump())
        conn.commit()  # execute logic : (close connection when done)
    return product

# Helper Method for DB - Queries


# Helper Method for DB-Queries
def insert_product(conn: Connection, product: ProductSchema):
    conn.execute(
        "INSERT INTO products_raw (product) VALUES (%s)",
        (Json(product),)    # TODO - Explore the Syntax
    )
