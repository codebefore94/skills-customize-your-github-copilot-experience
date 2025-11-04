"""Starter FastAPI application for the assignment.

This provides a minimal in-memory CRUD API for items.
"""
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import Dict, Optional

app = FastAPI(title="Simple Items API (Starter)")


class Item(BaseModel):
    id: Optional[int] = None
    name: str = Field(..., example="Red Ball")
    description: Optional[str] = Field(None, example="A red bouncy ball")
    price: float = Field(..., gt=0, example=9.99)


# Simple in-memory store: id -> Item dict
_items: Dict[int, Item] = {}
_next_id = 1


@app.get("/items")
def list_items(name: Optional[str] = None, min_price: Optional[float] = None, max_price: Optional[float] = None):
    """Return a list of items, optionally filtered by name or price range."""
    results = list(_items.values())
    if name:
        results = [it for it in results if name.lower() in it.name.lower()]
    if min_price is not None:
        results = [it for it in results if it.price >= min_price]
    if max_price is not None:
        results = [it for it in results if it.price <= max_price]
    return results


@app.post("/items", status_code=201)
def create_item(item: Item):
    """Create a new item and return it with an assigned id."""
    global _next_id
    item.id = _next_id
    _items[_next_id] = item
    _next_id += 1
    return item


@app.get("/items/{item_id}")
def get_item(item_id: int):
    """Retrieve a single item by id."""
    item = _items.get(item_id)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    return item


@app.put("/items/{item_id}")
def update_item(item_id: int, updated: Item):
    """Update an existing item. All fields are replaced by the provided payload."""
    if item_id not in _items:
        raise HTTPException(status_code=404, detail="Item not found")
    updated.id = item_id
    _items[item_id] = updated
    return updated


@app.delete("/items/{item_id}", status_code=204)
def delete_item(item_id: int):
    """Delete an item by id."""
    if item_id not in _items:
        raise HTTPException(status_code=404, detail="Item not found")
    del _items[item_id]
    return None


if __name__ == "__main__":
    # Simple check to allow running: `python starter-code.py` (optional)
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)
