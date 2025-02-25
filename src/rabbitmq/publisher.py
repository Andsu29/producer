from typing import Dict
import pika
import json


class RabbitmqPublisher:
    def __init__(
            self,
            host="env",
            port="env",
            username="env",
            password="env",
            exchange="env",
            routing_key="env"):
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
            port=self.__port,
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

# Provavelmente vou precisar colocar valores dinamicos nos parametros do init
# Para assim poder reaproveitar o código para publicar em outras filas