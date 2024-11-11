```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

```

```bash
uvicorn main:app --reload
```

```bash
# Add
curl -X POST "http://127.0.0.1:8000/items/" -H "Content-Type: application/json" -d "{\"id\": 1, \"name\": \"Sample Item\", \"description\": \"This is a sample item\", \"price\": 10.99}"

# All Items
curl -X GET "http://127.0.0.1:8000/items/"
# Single Item
curl -X GET "http://127.0.0.1:8000/items/1"

# Update Item
curl -X PUT "http://127.0.0.1:8000/items/1" -H "Content-Type: application/json" -d "{\"id\": 1, \"name\": \"Updated Item\", \"description\": \"This item has been updated\", \"price\": 15.99}"

# Delete Item
curl -X DELETE "http://127.0.0.1:8000/items/1"

```

