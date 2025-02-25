from connection.main import Conn
from rabbitmq.publisher import RabbitmqPublisher
from querys.query_get_products import query_get_all_products


class GetProducts():
    def __init__(self):
        self.connection = Conn()
        self.rabbitmq_publisher = RabbitmqPublisher()

    def get_products(self):
        try:
            with self.connection.create_connection().cursor() as cursor:
                query = query_get_all_products()
                cursor.execute(query)
                data = cursor.fetchall()
                return data
        except Exception as e:
            print(f"Erro ao buscar produtos: {e}")
        finally:
                self.connection.close_connection()
        
    def publish_queue(self):
         products = self.get_products()

         for product in products:
              # publicar produtos na fila
              self.rabbitmq_publisher.send_message(product)
