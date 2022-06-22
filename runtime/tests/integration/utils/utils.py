import hashlib
import json
from typing import List


def event_from_file(file_path):
    in_f = open(file_path, "r")
    payload = json.load(in_f)
    in_f.close()
    return payload


def create_sqs_event(records: List[dict]):
    return {
        "Records": [
            {
                "messageId": "2658b04b-3d29-4b9d-b165-ba44ef864c97",
                "receiptHandle": "uuid",
                "body": json.dumps(x, sort_keys=True),
                "attributes":
                {
                    "ApproximateReceiveCount": "1",
                    "SentTimestamp": "1652710452190",
                    "SenderId": "127.0.0.1",
                    "ApproximateFirstReceiveTimestamp": "1652710452198"
                },
                "messageAttributes": {},
                "md5OfBody": hashlib.md5(json.dumps(x, sort_keys=True).encode('utf-8')).hexdigest(),
                "eventSource": "aws:sqs",
                "eventSourceARN": "arn:aws:sqs:us-west-2:1234:test-event",
                "awsRegion": "us-west-2"
            }
            for x in records]
    }
