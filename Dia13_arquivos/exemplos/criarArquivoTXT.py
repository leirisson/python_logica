
nome_arquivo = input("nome do arquivo: ")
conteudo_arquivo = input("digite o texto: ")

caminho = f"Dia13_arquivos/exemplos/base/{nome_arquivo}.txt"

try:
    with open(caminho, 'w') as arquivo_base:
        arquivo_base.write(conteudo_arquivo)
        
except FileNotFoundError:
    print("ERRO: não foi possivel criar ou escrever no arquivo.")
    
else:
    try:
        with open(caminho, 'r') as arquivo:
            conteudo =  arquivo.read()
    except FileNotFoundError:
        print("Erro: Arquivo não exite")
    else:
        print("conteudo do arquivo")
        print(conteudo)