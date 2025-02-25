# Módulo que vai instanciar a classe do módulo de busca
from decorators.agendamento import loop
from methods.get_products import teste


@loop
def testando():
    teste()