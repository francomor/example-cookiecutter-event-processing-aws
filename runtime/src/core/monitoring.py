import os
from typing import Tuple

from aws_lambda_powertools import Logger, Metrics, Tracer


def init_monitoring() -> Tuple[Logger, Metrics, Tracer]:
    """initialize logger, metrics and tracer"""
    env = os.environ.get("DEPLOY_ENV", "dev")
    logger = Logger()
    logger.append_keys(env=env)
    metrics = Metrics()
    metrics.set_default_dimensions(env=env)
    tracer = Tracer()

    return logger, metrics, tracer
