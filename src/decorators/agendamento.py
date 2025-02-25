import schedule
import time

def loop(f):
    try:
        schedule.every(5).seconds.do(f)

        while True:
            schedule.run_pending()
            time.sleep(1) 
    except Exception as e:
        print(e)


# Módulo onde o schendule irá executar a função principal recebendo da função decorada
# Necessita tratar outros erros

# schedule.every(10).minutes.do(tarefa)  # A cada 10 minutos
# schedule.every().hour.do(tarefa)       # A cada hora
# schedule.every().monday.do(tarefa)     # Toda segunda-feira
# schedule.every().wednesday.at("08:00").do(tarefa)  # Toda quarta às 08:00
