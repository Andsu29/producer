# Módulo que vai instanciar a classe do módulo de busca
from utils.decorators import agendamento
from busca.main import teste


@agendamento
def testando():
    teste()