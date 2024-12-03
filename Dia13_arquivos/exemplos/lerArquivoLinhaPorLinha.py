
caminho_do_arquivo = "Dia13_arquivos/exemplos/base/data.txt"

try:
    with open(caminho_do_arquivo, 'r') as arquivo:
            for linha in arquivo:
                print(linha.strip())
        
except FileNotFoundError:
    print("ERRO: não existe esse arquivo")

        