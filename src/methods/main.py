from connection.main import Conn
from rabbitmq.publisher import RabbitmqPublisher
from querys.query_get_products import query_get_all_products, query_update_publish


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

    def update_publish(self, id):
        try:
            with self.connection.create_connection().cursor() as cursor:
                query = query_update_publish(id)
                cursor.execute(query)
                self.connection.commit()
        except Exception as e:
            print(f"Erro ao atualizar produto: {e}")
        finally:
                self.connection.close_connection()

    def publish_queue(self):
        products = self.get_products()

        if products:
            for product in products:
                if not product['publicado']:
                    self.rabbitmq_publisher.send_message(product)
                    self.update_publish(product['id'])
                else:
                    print("Produto já publicado!")
            
            # Preciso fazer uma validação - ok
            # Adicionar uma coluna no banco de publicado
            # esse publicado vai ser verificado aqui
            # para que se publicado for true ele não vai para a fila
            # pois ja foi publicado
            # após publicar o produto na fila deve marcar ele como publicado
            # assim não vai ficar repetindo produto