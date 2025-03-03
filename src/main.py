from decorators.agendamento import loop
from methods.main import GetPublish


@loop
def main():
    get_publish = GetPublish()
    print("Iniciando serviço")
    get_publish.publish_queue()
    print("Serviço finalizado")
