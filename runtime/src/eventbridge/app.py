from aws_lambda_powertools.utilities.data_classes import EventBridgeEvent, event_source
from aws_lambda_powertools.utilities.typing import LambdaContext

from .. import crud
from ..core.monitoring import init_monitoring
from ..db.session import Session
from ..models.item import ItemCreate

logger, metrics, tracer = init_monitoring()


@event_source(data_class=EventBridgeEvent)
def lambda_handler(event: EventBridgeEvent, context: LambdaContext):
    db = Session()
    logger.debug(event)
    item_in = ItemCreate(title="example", description="example")
    new_item = crud.item.create(
        db_session=db, item_in=item_in
    )
    item = crud.item.get(db, _id=new_item.id)
    logger.info(item.title)
    logger.info(item.description)
    db.close()
