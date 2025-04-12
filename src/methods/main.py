from connection.main import Conn
from rabbitmq.publisher import RabbitmqPublisher
from querys.query_get_products import query_get_all_products, query_update_publish
import base64


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
        contador_prontos = 0
        contador_pendentes = 0

        if products:
            for product in products:
                if not product['publicado'] and product["imagens"]:
                    imagem_base64 = None
                    imagem_base64 = base64.b64encode(product['imagens']).decode("utf-8")
                    produto_formatado =    {
                                "id":  product["id"],
                                "titulo": product["titulo"],
                                "publicado": product["publicado"],
                                "descricao": product["descricao"],
                                "preco": product["preco"],
                                "categoria": product["categoria"],
                                "marca": product["marca"],
                                "modelo": product["modelo"],
                                "codpro": product["codpro"],
                                "imagens": imagem_base64
                            }
                    self.rabbitmq_publisher.send_message(produto_formatado)
                    self.update_publish(produto_formatado['id'])
                    contador_prontos += 1
                    print(f"{contador_prontos} Produtos publicados!")
                elif not product["imagens"]:
                    contador_pendentes += 1
                    print(f"{contador_pendentes} Produtos pendentes para serem publicados!")
                else:
                    pass
