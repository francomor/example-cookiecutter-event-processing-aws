from runtime.src import crud
from runtime.src.db.session import db_session
from runtime.src.sqs import app
from runtime.tests.integration.utils.utils import create_sqs_event


def test_handler_for_scheduled_event(lambda_context):
    event = create_sqs_event([
        {
            "title": "item0",
            "description": "item0"
        },
        {
            "title": "item1",
            "description": "item1"
        }
    ])
    new_items_ids = app.lambda_handler(event, lambda_context)
    for i, new_item_id in enumerate(new_items_ids):
        stored_item = crud.item.get(db_session=db_session, _id=new_item_id)
        assert stored_item.id == new_item_id
        assert stored_item.title == f"item{i}"
        assert stored_item.description == f"item{i}"
