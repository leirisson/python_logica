#CRIANDO UM ARQUIVO CSV
import csv

caminho = "Dia13_arquivos/exemplos/base/base_contatos.csv"
# 1 = um array para o cabecalho das colunas


try:
    with open(caminho, 'w', newline='') as base_contatos:
        # cabecalho 
        escritor = csv.writer(base_contatos)
        escritor.writerow(['Nome', 'profissao', 'Idade'])
        escritor.writerow(['Leirisson', 'tecnico', 25])
        
except FileNotFoundError:
    print("Não foi possivel escrever ou o arquivo não existe.")
