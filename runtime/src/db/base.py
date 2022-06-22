# Import all the models, so that Base has them before being
# imported by Alembic
from ..db_models.item import Item  # noqa
from .base_class import Base  # noqa
