from pydantic import BaseModel,Field
from typing import Optional
from datetime import datetime,timedelta

class Item(BaseModel):

    id:int
    name:str
    description: Optional[str]=None
    price: float

    created_at: datetime = datetime.now()
    updated_at: datetime = datetime.now()

    expire_at: datetime = Field(
        default_factory=lambda: datetime.utcnow() + timedelta(days=14)
    )