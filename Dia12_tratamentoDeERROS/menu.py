def menu():
    print("1. cadastrar")
    print("2. editar")
    print("3. excluir")
    print("4. listar")
    print("5. sair")
    

def main():
    while True:
        try:
            menu()
            op = int(input("Escolha uma opção: "))
        except ValueError:
            print("escolha um valor numerico")
            print("tente novamente !")
        else:
            if op == 1:
                print("cadastrando...")
            elif op == 2:
                print("editando...")
            elif op == 3:
                print("excluindo")
            elif op == 4:
                print("listando...")
            elif op == 5:
                print("saindo do sistema ...")
                break
            else:
                print("opção invalida !")
                print("tente novamente.")
                
                
if __name__ == "__main__":
    main()