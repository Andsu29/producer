import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "src")))
from typing import Dict
from setup import RABBITMQ
import pika
import json


class RabbitmqPublisher:
    def __init__(
            self,
            host=RABBITMQ['host'],
            port=RABBITMQ['port'],
            username=RABBITMQ['username'],
            password=RABBITMQ['password'],
            exchange=RABBITMQ['exchange'],
            routing_key=RABBITMQ['routing_key']):
        self.__host = host
        self.__port = port
        self.__username = username
        self.__password = password
        self.__exchange = exchange
        self.__routing_key = routing_key
        self.__channel = self.__create_channel()

    def __create_channel(self):
        connection_parameters = pika.ConnectionParameters(
            host=self.__host,
            port=int(self.__port),
            credentials=pika.PlainCredentials(
                username=self.__username,
                password=self.__password
            )
        )

        channel = pika.BlockingConnection(connection_parameters).channel()
        return channel

    def send_message(self, body: Dict):
        self.__channel.basic_publish(
            exchange=self.__exchange,
            routing_key=self.__routing_key,
            body=json.dumps(body),
            properties=pika.BasicProperties(
                delivery_mode=2
            )
        )