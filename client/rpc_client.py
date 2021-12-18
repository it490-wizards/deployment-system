import json
import os
import uuid
from typing import Any

import dotenv
import pika

dotenv.load_dotenv()


class Client:
    def __init__(self):
        self.connection = pika.BlockingConnection(
            pika.ConnectionParameters(
                host=os.getenv("PIKA_HOST"),
                port=5672,
                virtual_host="deployment",
                credentials=pika.PlainCredentials(
                    username=os.getenv("PIKA_USERNAME"),
                    password=os.getenv("PIKA_PASSWORD"),
                ),
            )
        )

        self.channel = self.connection.channel()

        result = self.channel.queue_declare(
            queue="",
            exclusive=True,
        )
        self.callback_queue = result.method.queue

        self.channel.basic_consume(
            queue=self.callback_queue,
            on_message_callback=self.on_response,
            auto_ack=True,
        )

    def on_response(self, ch, method, props, body: bytes):
        if self.corr_id == props.correlation_id:
            self.response = body.decode()

    def call(self, func: str, *args: Any) -> Any:
        request = json.dumps({"func": func, "args": args})
        self.response = None
        self.corr_id = str(uuid.uuid4())
        self.channel.basic_publish(
            exchange="",
            routing_key="rpc_queue",
            properties=pika.BasicProperties(
                reply_to=self.callback_queue,
                correlation_id=self.corr_id,
            ),
            body=request.encode(),
        )
        while self.response is None:
            self.connection.process_data_events()

        return json.loads(self.response)
