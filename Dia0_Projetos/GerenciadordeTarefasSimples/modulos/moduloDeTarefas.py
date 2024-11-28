def menu():
        print("1 - criar tarefa")
        print("2 - editar tarefa")
        print("3 - excluir tarefa")
        print("4 - listar tarefas")
        print("0 - sair")

def criar_tarefa(tasks):
    title_task = input("Digite o titulo da tarefa")
    new_task = {'titulo':title_task}
    tasks.append(new_task)
    print(f"Tarefa: '{title_task}' cadastrada com sucesso.")


def editar_tarefa(tasks):
    if not tasks:
        print("Não existe tarefas cadastradas")
        print("Voltando para o Menu")
        return
    search_task = input("Qual tarefa deseja editar ?")
    for index, task in enumerate(tasks):
        if search_task.lower() in task['titulo'].lower():
            new_title_task = input("Digite o novo titulo da tarefa: ")
            tasks[index]['titulo'] = new_title_task
            print(f"Tarefa editada com sucesso: {new_title_task}")
            return


def excluir_tarefas(tasks):
    if not tasks:
        print("Sem tarefas para excluir !")
        return
    search_title = input("Qual o nome da tarefa ? ")
    for indice_tarefa, task in enumerate(tasks):
        if search_title.lower() in task['titulo'].lower():
            tasks.pop(indice_tarefa)
            print(f"Tarefa: {search_title} excluida com sucesso.")
            return
    print("Tarefa não encontrada.")
    

def listar_tarefas(tasks):
    if not tasks:
        print("Nenhuma tarefa cadastrada.")
        return
    
    print("\nLista de tarefas:")
    
    for indice, task in enumerate(tasks, start=1):
        print(f"{indice}ª. {task['titulo']}")