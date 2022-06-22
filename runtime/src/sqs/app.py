import json

from aws_lambda_powertools.utilities.data_classes import SQSEvent, event_source
from aws_lambda_powertools.utilities.typing import LambdaContext

from .. import crud
from ..core.monitoring import init_monitoring
from ..db.session import Session
from ..models.item import ItemCreate

logger, metrics, tracer = init_monitoring()


@event_source(data_class=SQSEvent)
def lambda_handler(event: SQSEvent, context: LambdaContext):
    db = Session()
    logger.debug(event)
    logger.debug(context)
    new_items_ids = []
    for record in event.records:
        item_event = json.loads(record.body)
        item_in = ItemCreate(
            title=item_event.get("title"),
            description=item_event.get("description")
        )
        new_item = crud.item.create(
            db_session=db, item_in=item_in
        )
        new_items_ids.append(new_item.id)
    db.close()
    return new_items_ids  # for testing purposes
