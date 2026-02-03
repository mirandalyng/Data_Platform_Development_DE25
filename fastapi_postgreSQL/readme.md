# Postgresql & fastapi

## Installation

(Use uv if that's your relevant tech)

```
$ uv add
$ pip install "fastapi[standard]"
$ pip install "psycopg[binary]"
$ python -m pip install "psycopg[pool]"
```

## Run app

- fastapi dev main.py

## Storing data - philosophy

- What's the purpose of our data?
  - Bulk uploading
  - JSON data storage
  - Unorganized data
  - PostgreSQL database

- What's the dataype of said data?
  - Unorganized
  - unstrucured
  - JSON

## Database - PostgreSQL

A newly created database does NOT contain any TABLES by default.

**Step 1 - Create new Table (Products)**

```postgresql
CREATE TABLE IF NOT EXISTS products_raw (
 id BIGSERIAL PRIMARY KEY,
 created_at TIMESTAMPTZ NOT NULL DEFAULT now(),
 product JSONB NOT NULL
);
```

**Step 2 - Create a connection with the database using URL**

```python
DATABASE_URL = "postgresql://USERNAME:PASSWORD:PORT/NAME"
DATABASE_URL = "postgresql://postgres:password:PORT/DB_NAME"
```

Postman test aganst "localhost:8000/products

**PGAdmin4**

- Username: rightclick your database -> properties -> username
- Password: you should know this one
  change password ->
- Port: right click Postgesql17 - properties -> connection -> port
- Adress: same as Port

## Psycopg3
