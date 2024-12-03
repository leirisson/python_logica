def menu():
    print("==============================")
    print("====  SISTEMA DE CADASTRO ====")
    print("1. CADASTRAR")
    print("2. LISTAR ")
    print("==============================")

def cadastrar():
    try:
        # nome_do_arquivo = input("nome do arquivo: ")
        nome_do_produto =input("nome produto: ")
        marca = input("maraca do produto: ")
        quantidade = int(input("quantidade: "))
        produto = {"nome":nome_do_produto, "marca":marca, "quantidade":quantidade}
        produto = str(produto)
        with open(f"Dia13_arquivos/exemplos/base//cadastro.txt", "a") as arquivo:
            arquivo.write(f"{produto}\n")
    except FileNotFoundError:
        print("não foi possivel criar o arquivo ou não foi possivel escrever no arquivo.")


def listar():
    try:
        with open(f"Dia13_arquivos/exemplos/base/cadastro.txt", "r") as arquivo:
            conteudo = arquivo.read()
    except:
        print("ERRO - Arquivo não encontrado")
    else:
        print("lista de cadastros")
        print(conteudo)


def main():
    while True:
        try:
            menu()
            op = int(input('escolha uma opção: '))
        except ValueError:
            print("Erro: escolha uma opção numerica")
        else:
            if op == 1:
                cadastrar()
            elif op ==2:
                listar()
            else:
                print("opção invalida.")
                print("tente novamente")
        




if __name__ == "__main__":
    main()