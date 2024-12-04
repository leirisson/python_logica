
clientes     = [{"nome": "Leirisson", "sobrenome":"souza", "cpf":"123456789", "email":"leirisson@souza.com"}]
emprestimos =  [{"nome": "Leirisson", "sobrenome":"souza", "cpf":"123456789", "email":"leirisson@souza.com", "juros":30 ,"valor":1000, "valor_pagamento":1300}]
pagamentos = []
def menu():
    print("== MENU ===")
    print("1. cadastrar cliente")
    print("2. Listar clientes")
    print("3. realizar emprestimo")
    print("4. receber pagamento")
    print("5. listar devedores")
    print("6 -sair")



def main():
    while True:
        menu()
        op = input("escolha uma opção: ")
        if op == '1':
            nome = input("nome do cliente: ")
            sobrenome = input("sobre nome do cliente: ")
            cpf = input("cpf do cliente: ")
            email = input("email do cliente: ")

            emprestimo = {"nome": nome, "sobrenome":sobrenome, "cpf":cpf, "email":email}

            clientes.append(emprestimo)
            print("cliente cadastrado com sucesso")

        elif op == '2':
            for emprestimo in emprestimos:
                print(f"NOME: {emprestimo['nome']} {emprestimo['sobrenome'] } | CPF: {emprestimo['cpf']} | e-mail: {emprestimo['email']}")

        elif op == '3':
            emprestimo = {}
            cpf_cliente = input("qual o CPF do cliente: ")
            for cliente in clientes:
                if cpf_cliente == cliente['cpf']:
                    emprestimo['nome'] = cliente['nome']
                    emprestimo["sobrenome"] = cliente['sobrenome']
                    emprestimo["cpf"] = cliente['cpf']
                    emprestimo["email"] = cliente['email']
                    valor_emprestimo = float(input("qual o valor do emprestimo: "))
                    juros_emprestimo = int(input("qual a % de juros: "))
                    emprestimo['juros'] = juros_emprestimo
                    emprestimo['valor'] = valor_emprestimo
                    emprestimo['valor_a_pagar'] = ((juros_emprestimo /100) * valor_emprestimo) + valor_emprestimo
                    emprestimos.append(emprestimo)
                    print("emprestimo realizado com sucesso.")

        elif op == '4':
            try:
                print("== SUB MENU ==")
                print("1. Pagamento TOTAL")
                print("2. Pagamento Parcial")
                print("3. Pagar somente o juros: ")
                op = input("escolha um metodo de pagamento: ")
            except ValueError:
                print("informe um valor numerico")
            else: 
                if op == '1':
                    pagamento = {}
                    cpf_cliente = input("qual o CPF do cliente: ")
                    for emprestimo in emprestimos:
                        if cpf_cliente == emprestimo['cpf']:
                            recebe_pagamento = float(input("informe o valor do pagamento: "))
                            pagamento['nome'] = emprestimo['nome']
                            pagamento["sobrenome"] = emprestimo['sobrenome']
                            pagamento["cpf"] = emprestimo['cpf']
                            pagamento["email"] = emprestimo['email']
                            pagamento['juros'] = emprestimo['juros']
                            pagamento['valor'] = emprestimo['valor']
                            if recebe_pagamento == emprestimo['valor_a_pagar']:
                                pagamento['valor_a_pagar'] = emprestimo['valor_a_pagar']
                                pagamentos.append(pagamento)
                                print("pagamento realizado com sucesso.")
                            else:
                                print("Valor de pagamento incorreto.")


        elif op == '5':
            for devedor in emprestimos:
                print(devedor)
            input("enter para continuar")

        elif op == '6':
            print("saindo")
            break
        else:
            print("Valor invalido.")

    

if __name__ == "__main__":
    main()