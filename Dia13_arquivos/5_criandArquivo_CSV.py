import csv

try:
    with open("Dia13_arquivos/arquivos/contatos.csv", "w", newline='') as arquivo_csv:
        escrever = csv.writer(arquivo_csv)
        escrever.writerow(['Nome', 'Sobrenome','email','telefone'])
        for i in range(2):
            nome = input("nome: ")
            sobreNome = input("Sobrenome: ")
            email = input("e-mail: ")
            telefone = input("telefone: ")
            escrever.writerow([nome,sobreNome,email,telefone])
except FileNotFoundError:
    print("Erro ao tentar encontrar ou criar o arquivo.")
    
else:
    print("Arquivo criado com sucesso")
    

# precisa corrigir 
# try:
#     with open("Dia13_arquivos/arquivos/contatos.csv", "a") as data_csv:
#         conteudo = list(csv.reader(data_csv))
#         for linha in conteudo:
#             print(linha)
# except FileNotFoundError:
#     print("Arquivo  não encontrado")

# else:
#     print(conteudo)