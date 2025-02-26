from connection.main import Conn
from rabbitmq.publisher import RabbitmqPublisher
from querys.query_get_products import query_get_all_products


class GetPublish():
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
            # Preciso fazer uma validação
            # Adicionar uma coluna no banco de exportado
            # esse exportado vai ser verificado aqui
            # para que se exportado for true ele não vai para a fila
            # pois ja foi exportado
            self.rabbitmq_publisher.send_message(product)
            # após publicar o produto na fila deve marcar ele como exportado
            # assim não vai ficar repetindo produto