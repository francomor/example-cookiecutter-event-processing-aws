from pydantic import BaseModel


# Shared properties
class ItemBase(BaseModel):
    title: str = None
    description: str = None


# Properties to receive on item creation
class ItemCreate(ItemBase):
    title: str


# Properties to receive on item update
class ItemUpdate(ItemBase):
    pass


# Properties shared by models stored in DB
class ItemInDBBase(ItemBase):
    id: int
    title: str

    class Config:
        orm_mode = True
