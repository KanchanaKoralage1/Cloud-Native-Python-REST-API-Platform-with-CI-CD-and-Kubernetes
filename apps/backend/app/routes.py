from fastapi import APIRouter, HTTPException
from app.model import Item
from datetime import datetime

router=APIRouter()

items=[]

#create an item
@router.post("/items")
def create_item(item:Item):
    item.created_at=datetime.now()
    item.updated_at=datetime.now()

    items.append(item)
    return{
        "message":"Items added successfully",
        "item":item
    }

#get items
@router.get("/items")
def get_items():
    return items

#get item by id
@router.get("/items/{item_id}")
def get_item_by_id(item_id: int):
    for item in items:
        if item.id == item_id:
            return item
    raise HTTPException(status_code=404, detail="item not found")

#update item by id
@router.put("/items/{item_id}")
def update_item(item_id: int, updated_item: Item):
    for index, item in enumerate(items):
        if item.id == item_id:
            updated_item.created_at = item.created_at
            updated_item.updated_at = datetime.now()
            items[index] = updated_item
            return {
                "message": "Item updated successfully",
                "item": updated_item
            }
    raise HTTPException(status_code=404, detail="Item not found")

#delete item by id
@router.delete("/items/{item_id}")
def delete_item(item_id: int):
    for index, item in enumerate(items):
        if item.id == item_id:
            items.pop(index)
            return {"message": "Item deleted successfully"}
    raise HTTPException(status_code=404, detail="Item not found")