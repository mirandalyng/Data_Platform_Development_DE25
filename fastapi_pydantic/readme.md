# Deletion of name - why?

## Servlet container

- Hosting of Application (locally)
- FastAPI introduces this new concept
- Removes traditional/ 'play/ start' button
- Requires FastAPI - start command (to run app)

## FastAPI

- Install: $ pip install "fastapi[standard]"
  - BONUS: uv alternative for performance
  - BONUS: COMMAND + F (filter for "success") in terminal
  - ERROR: "Consider adding this to path"
  - $ pip list - to see all of the added packages

  ## Endpoint
  - API och URL relatted
  - Consists of a path: "/example"
  - Accompanied by HTTP-Method (GET, POST, PUT, DELETE)

## Decorator

- Refers to the @ symbol
- Defference in how function executes
- Runs logic from externam decorator function
  - (Function over function)
- returns JSON data (automatic conversion)

```python
@decorator
def test_function():
```

## 1. Run the app:

```
fastapi dev FILENAME.py
```

**Important:** stand in the same folder as FILENAME.py

## 2. Go to localhost

```
localhost:8000
```

## 3. Go to documentation

```
localhost:8000/docs
```

- Parameters
- status code
- Media type
- Schema
- "Try it out"

## URL

Exempel: https://www.google.com/search?q =bananas&rlz=1C5CHFA_enSE1097SE1099&oq=bananas

- In this example we see a dynamic parameter
  - q == query (just a variable name)
  - ? == start of query
  - What comes after = is Dynamic_Value (client input)

## Pydantic

- Uses Schema to Define Logical data type structure
- Class based
- Used for data validation
- Facilitates conversion of JSON -> Python Objects
- Best practice - (seperated from its own package)
