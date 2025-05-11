import json
import logging

import redis
from settings import config

logger = logging.getLogger("celery")


class RedisConnector:
    def __init__(self):
        self.client = redis.Redis(
            host=config.REDIS_SERVER, port=int(config.REDIS_PORT), decode_responses=True
        )

    def add_to_stream(self, stream_name: str, data: dict):
        """Add data to a Redis stream."""
        logger.info(f"Add to stream : {stream_name} {data}")
        self.client.xadd(stream_name, data)

    def get_from_stream(self, stream_name: str, key: str, timeout: int = 120000):
        """Get data from a Redis stream with a timeout (in milliseconds)."""
        while True:
            messages = self.client.xread({stream_name: '$'}, block=timeout, count=1)
            logger.info(f"Messages from stream : {messages}")

            if not messages:
                logger.info("No messages")
                return None  # Return None if no messages arrive within the timeout

            for message in messages:
                stream, message_data = message
                message_id, fields = message_data[0]
                # Acknowledge the message so it is marked as processed
                self.client.xack(stream_name, 'my_group', message_id)
                print(fields['data'])
                result: dict = json.loads(fields['data'])
                print(result)
                if result.get(key, None):
                    return result.get(key, None)
