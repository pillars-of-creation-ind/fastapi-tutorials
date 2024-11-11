from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

# Item model
class Item(BaseModel):
    id: int
    name: str
    description: str | None = None
    price: float

# In-memory database
items = []

# Create an item
@app.post("/items/", response_model=Item)
def create_item(item: Item):
    items.append(item)
    return item

# Read all items
@app.get("/items/", response_model=list[Item])
def read_items():
    return items

# Read single item by ID
@app.get("/items/{item_id}", response_model=Item)
def read_item(item_id: int):
    for item in items:
        if item.id == item_id:
            return item
    raise HTTPException(status_code=404, detail="Item not found")

# Update an item by ID
@app.put("/items/{item_id}", response_model=Item)
def update_item(item_id: int, updated_item: Item):
    for index, item in enumerate(items):
        if item.id == item_id:
            items[index] = updated_item
            return updated_item
    raise HTTPException(status_code=404, detail="Item not found")

# Delete an item by ID
@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    for index, item in enumerate(items):
        if item.id == item_id:
            del items[index]
            return {"detail": "Item deleted"}
    raise HTTPException(status_code=404, detail="Item not found")
