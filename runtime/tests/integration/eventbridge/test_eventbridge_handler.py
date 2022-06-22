import logging
from pathlib import Path

from runtime.src.eventbridge import app
from runtime.tests.integration.utils.utils import event_from_file


def test_handler_for_scheduled_event(lambda_context, caplog):
    event_path = Path(__file__).parent / "events" / "event_schedule_1.json"
    event = event_from_file(event_path)
    app.lambda_handler(event, lambda_context)
    record = next(iter(caplog.records))
    assert record.levelno == logging.INFO
    assert record.message == "example"
    assert record.message == "example"
