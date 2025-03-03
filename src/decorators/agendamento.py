import schedule
import time
import traceback

def loop(f):
    try:
        print("Iniciando loop...")
        schedule.every(1).minutes.do(f)
        print("Antes do While...")
        while True:
            print("Dentro do While 1...")
            schedule.run_pending()
            print("Dentro do While 2...")
            time.sleep(1) 
    except Exception as e:
        print(f"Erro no loop: {e}")
        print(traceback.format_exc())


# Módulo onde o schendule irá executar a função principal recebendo da função decorada
# Necessita tratar outros erros

# schedule.every(10).minutes.do(tarefa)  # A cada 10 minutos
# schedule.every().hour.do(tarefa)       # A cada hora
# schedule.every().monday.do(tarefa)     # Toda segunda-feira
# schedule.every().wednesday.at("08:00").do(tarefa)  # Toda quarta às 08:00
