#  Dia13_arquivos\exemplos\base\data.txt

caminho_arquivo = "Dia13_arquivos/exemplos/base/data.txt"

try:
    with open(caminho_arquivo, 'r') as arquivo:
        conteudo_do_arquivo = arquivo.read()
except FileNotFoundError:
    print("Error: arquivo nãoencontrado no diretorio.")

else:
    print("conteudo do arquivo")
    print(conteudo_do_arquivo)