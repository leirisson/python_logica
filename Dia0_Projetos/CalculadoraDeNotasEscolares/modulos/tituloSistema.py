import os 
def tituloSistema(titulo):
    os.system('cls')
    tamanho_titulo = len(titulo)
    print(tamanho_titulo * "=")
    print(titulo.upper())
    print(tamanho_titulo * "=")