import time

import redis
from celery import Celery, signals

from logging_config import setup_logging
from settings import config
import sentry_sdk
import warnings

warnings.filterwarnings("ignore", category=UserWarning)


# Wait until Redis is available
while True:
    try:
        r = redis.Redis.from_url(config.CELERY_BROKER_URL, socket_timeout=1)
        r.ping()
        print("Broker is reachable. Starting Celery...")
        break
    except redis.ConnectionError:
        print("Waiting for Broker...")
        time.sleep(5)

celery = Celery("worker-{{cookiecutter.project_slug}}")
celery.conf.broker_url = config.CELERY_BROKER_URL
celery.conf.result_backend = config.CELERY_RESULT_BACKEND
celery.conf.broker_connection_retry_on_startup = True
celery.conf.task_default_queue = "{{cookiecutter.project_slug}}.task_default_queue"

celery.autodiscover_tasks(["apps.base"])

@signals.after_setup_logger.connect
def setup_worker_logger(logger, *args, **kwargs):
    setup_logging()


@signals.after_setup_task_logger.connect
def setup_task_logger(logger, *args, **kwargs):
    setup_logging()

@signals.celeryd_init.connect
def init_sentry(**_kwargs):
    sentry_sdk.init(
        dsn="Your Sentry URL",
        traces_sample_rate=1.0,
        profiles_sample_rate=1.0,
    )
