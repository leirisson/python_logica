from modulos.moduloDeTarefas import menu
from modulos.moduloDeTarefas import criar_tarefa
from modulos.moduloDeTarefas import editar_tarefa
from modulos.moduloDeTarefas import excluir_tarefas
from modulos.moduloDeTarefas import listar_tarefas




def gerenciadorDeTarefas():
    tasks = [{"titulo": "comprar pão"}, {"titulo": "lavar roupas"}]
       
    
    while True:
        menu()
        op = int(input("escolha uma opção: "))
        try:
            if op == 1:
                criar_tarefa(tasks)
            elif op == 2:
                editar_tarefa(tasks)
            elif op == 3:
                excluir_tarefas(tasks)
            elif op == 4:
                listar_tarefas(tasks)
            elif op == 0:
                print("Saindo... Até logo!")
                break
            else:
                print("Opção invalida tente novamente.")
                
        except ValueError:
            print("valor informado não é um numero.")

       
if __name__ == "__main__":
    gerenciadorDeTarefas()