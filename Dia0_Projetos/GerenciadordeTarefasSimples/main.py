
def menu():
        print("1 - criar tarefa")
        print("2 - editar tarefa")
        print("3 - excluir tarefa")
        print("4 - deletar tarefa")
        print("0 - sair")


def gerenciadorDeTarefas():
    tarefas = []
    tarefa = {}
 
    
    
    while True:
        menu()
        op = int(input("escolha uma opção: "))
        try:
            if op == 1:
                titulo_tarefa = input("qual a tarefa: ")    
                tarefa['titulo'] = titulo_tarefa 
                tarefas.append(tarefa)
                print('tarefa cadastrada com sucesso. ',tarefas)
            elif op == 2:
                tamanha = len(tarefas)
                posicao = 0
                if tamanha > 0:
                        for tf in tarefas:
                            print(f"{tf[0]}")
                            print(f"{posicao}º: {tf[0]['titulo']}")
                            posicao += 1
                else:
                    input("sem tarefas para editar. Aperte enter para continuar.")
            elif op == 0:
                print("saindo...")
                break
                
        except ValueError:
            print("valor informado nãoa é um numero.")

       
    
    

if __name__ == "__main__":
    gerenciadorDeTarefas()