

try:
    with open("Dia13_arquivos/arquivos/log.txt","a") as arquivo:
        log = input("log: ")
        arquivo.write(log + "\n")
        
except FileNotFoundError:
    print("Arquivo não encontrado.")

else:
    with open("Dia13_arquivos/arquivos/log.txt", "r") as logs:
        texto = logs.read()
        print(texto)