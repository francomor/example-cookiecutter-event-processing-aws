from typing import List, Optional

from sqlalchemy.orm import Session

from ..db_models.item import Item
from ..models.item import ItemCreate, ItemUpdate


def get(db_session: Session, *, _id: int) -> Optional[Item]:
    return db_session.query(Item).filter(Item.id == _id).first()


def get_multi(db_session: Session, *, skip=0, limit=100) -> List[Optional[Item]]:
    return db_session.query(Item).offset(skip).limit(limit).all()


def create(db_session: Session, *, item_in: ItemCreate) -> Item:
    item_in_data = dict(item_in)
    item = Item(**item_in_data)
    db_session.add(item)
    db_session.commit()
    db_session.refresh(item)
    return item


def update(db_session: Session, *, item: Item, item_in: ItemUpdate) -> Item:
    item_data = item.__dict__
    update_data = item_in.dict(exclude_unset=True)
    for field in item_data:
        if field in update_data:
            setattr(item, field, update_data[field])
    db_session.add(item)
    db_session.commit()
    db_session.refresh(item)
    return item


def remove(db_session: Session, *, _id: int):
    item = db_session.query(Item).filter(Item.id == _id).first()
    db_session.delete(item)
    db_session.commit()
    return item
