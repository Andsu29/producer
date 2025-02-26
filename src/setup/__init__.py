import os
import dotenv


dotenv.load_dotenv()

DB1 = {     
        "host": os.environ['DB_HOST'],
        "user": os.environ['MYSQL_ROOT'],
        "password": os.environ['MYSQL_ROOT_PASSWORD'],
        "database": os.environ['MYSQL_DATABASE'],
        "port": os.environ['DB_PORT']
}

RABBITMQ = {     
        "host": os.environ['RABBITMQ_HOST'],
        "username": os.environ['RABBITMQ_USER'],
        "password": os.environ['RABBITMQ_PASS'],
        "exchange": os.environ['RABBITMQ_EXCHANGE'],
        "queue": os.environ['RABBITMQ_QUEUE'],
        "routing_key": os.environ['RABBITMQ_RK'],
        "port": os.environ['RABBITMQ_PORT']
}