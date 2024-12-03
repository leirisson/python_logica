
# lendo um arquivo de texto 

try:
    arquivo = open("Dia12_tratamentoDeERROS\data\daos.txt", "r")
    conteudo = arquivo.read()
    
except FileNotFoundError:
    print("erro ao tentar encontrar arquivos !")
    
else:
    print(f"Conteudo do arquivo")
    print(f"{conteudo}")