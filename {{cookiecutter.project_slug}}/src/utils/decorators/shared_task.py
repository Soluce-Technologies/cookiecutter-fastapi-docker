import worker
from functools import wraps


def custom_shared_task(*args, **kwargs):
    def decorator(func):
        @worker.celery.task(*args, **kwargs)
        @wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            return result

        return wrapper

    return decorator
