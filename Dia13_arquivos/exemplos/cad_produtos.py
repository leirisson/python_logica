import os
import csv

CAMINHO_DO_ARQUIVO = 'Dia13_arquivos/exemplos/base/cad_produtos.csv'

def menu():
    print("== Menu sistema == ")
    print("1. cadastrar produto")
    print("2. listar produto")
    print("3. editar produto")
    print("4. excluir produto")
    print("5. sair")
    
    
def cadastro():
 
    try:
        with open(CAMINHO_DO_ARQUIVO, 'a', newline="") as arquivo:
            
            escritor = csv.writer(arquivo)
            escritor.writerow(['NOME', 'MARCA', 'QUANTIDADE','PRECO'])
            
            nome_produto = input("nome do produto: ")
            marca_do_produto = input("marca: ")
            quantidade = int(input("quantidade: "))
            preco = float(input("preço do produto: "))
            
            escritor.writerow([nome_produto, marca_do_produto, quantidade, preco])
        print("Registro criado com sucesso")        
            
    except FileNotFoundError:
        print("Arquivo não existe")
    
def listar_produtos():
    try:
        with open(CAMINHO_DO_ARQUIVO, 'r') as arquivo:
            produtos = csv.reader(arquivo)
            for produto in produtos:
                print(produto)
            
    except FileNotFoundError:
        print("erro ao tentar ler arquivo com os produtos")
        

       
        
        
        
def main():
    while True:
        try:
            menu()
            op = int(input("escolha uma opção: "))
        except ValueError:
            print("Erro: escolha uma opção numerica.")
            continue
        else:
            if op == 1:
                cadastro()
            elif op == 2:
                listar_produtos()
            elif op == 5:
                print("saindo do sistema ...")
                break
            else:
                print("opção invalida, tente novamente.")
                continue


if __name__ == '__main__':
    main()