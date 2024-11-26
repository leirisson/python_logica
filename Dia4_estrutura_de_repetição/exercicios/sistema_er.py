# =================================
#            NIVEL BASICO
# =================================


def Contador_de_Produtos():
   total_produtos = 0

   while True:
        try:
            n_produtos = int(input("quantos produtos deseja cadastrar: "))
            if n_produtos <= 0:
                print("Por favor, insira um número positivo.")
                continue
        except ValueError:
            print("Entrada inválida! Por favor, insira um número inteiro.")
            continue
        for i in range(n_produtos):
            nome_produto = input("digite o nome do produto: ")
            total_produtos += 1
          
        print(f"Total de produtos cadastrados até agora: {total_produtos}")

        try:
            op = int(input("Deseja cadastrar mais produtos? 1 - SIM | 2 - NÃO: "))
            if op == 2:
                print(f"Cadastro finalizado. Total de produtos cadastrados: {total_produtos}")
                break
            elif op != 1:
                print("opção invalida. Finalizzando cadastro.")
                break
           
        except ValueError:
            print("Entrada inválida! Finalizando cadastro.")
            break

def Tabuada_de_Multiplicacao(numero):
    
    for i in range(1,11):
        resultado  = i * numero
        print(f"{i} x {numero} = {resultado}")

def Calculo_de_Total_de_Compras():
    total = 0
    total_compras = 0
    while True:
        try:
            valoir_compra = int(input(f"qual o valor da {total_compras + 1} compra: "))
            total += valoir_compra
            total_compras +=1
        except ValueError:
            print("O valor da compra deve ser valores numericos")
            continue
        try:
            op = int(input("Deseja cadastrar ooutra conta: 1 - SIM | 2 - NÂO "))
            if op == 2:
                print(f"Quantidade de compras: {total_compras} | Valor toal: {total}")
                break
            elif op !=1:
                print("opção invalida. encerrando !")
                break

        except ValueError:
            print("opção invalida, escilha os valores 1 ou 2. Encerrando o programa.")
            break


            
# =================================
#            NIVEL MEDIO
# =================================

def Login():
    cont_senha = 3

    senha = '123456'
    
    while True:
        print(f"Quantidade de tentativas restantes: {cont_senha}")
        senha_user = input("Digite a senha de login: ")
        if cont_senha >= 1:
            if senha != senha_user:
                cont_senha -= 1
                if cont_senha == 0:
                    print("tentaivas esgotadas.")
                    print("finalizando o sistema...")
                    break
                print("Senha incorreta, tente novamente.")
                continue
            else:
                print("Logado no sistema com sucesso.")
                break
  


            
def Soma_de_Numeros_Pares():
    print("Precisa informar o inicio e fim do intervalo")
    inicio = int(input("inicio: "))
    fim = int(input("fim: "))

    soma_pares = 0
    
    for i in range(inicio, fim):
        