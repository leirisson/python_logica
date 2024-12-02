import os
import json

# função para carregar tarefas
def carregar_tarefas():
    if os.path.exists('Dia13_arquivos/arquivos/data_tarefas.json'):
        with open('Dia13_arquivos/arquivos/data_tarefas.json', 'r') as data_tarefas:
            return json.load(data_tarefas)
    return []

# menu principal
def menu():
    print(" === GERENCIADOR DE TAREFAS === ")
    print("1. Adcionar Tarefa")
    print("2. Listar Tarefas")
    print("3. concluir Tarefa")
    print("4. Remover Tarefa")
    print("5. Sair")


def salvar_tarefas(tarefas):
    with open("Dia13_arquivos/arquivos/data_tarefas.json", "w") as arquivo:
        json.dump(tarefas, arquivo, indent=2)
        

#criar uma tarefa
def adcionar_tarefas(tarefas):
    print("== Adcionar nova tarefa ==")
    
    id = len(tarefas) + 1
    
    titulo = input("titulo da tarefa: ")
    descricao = input("descrição da tarefa: ")
    
    tarefa = {
        'id': id,
        'titulo': titulo,
        'descricao': descricao,
        'status': False
    }
    
    tarefas.append(tarefa)
    salvar_tarefas(tarefas)
    
    
    

# finção para exibir todas as tarefas
def listar_tarefas(tarefas):
    print("=== TAREFAS ===")
    for tarefa in tarefas:
        status = "Concluida" if tarefa['status'] else "Pendente"
        print(f"Id: {tarefa['id']}, Titulo: {tarefa['titulo']}, Status: {status}")




def main():
    tarefas = carregar_tarefas()
    while True:
        menu()
        op = input("escolha uma opção: ")
        
        if op =='1':
            adcionar_tarefas(tarefas)
        elif op == '2':
            listar_tarefas(tarefas)


if __name__ == "__main__":
    main()