# Erro de Acesso a Índice em uma Lista

elementos = [10,20,30,40,50]

try:
    numero = int(input("Digite um índice para acessar a lista (0-4): "))
    print(f"{elementos[numero]}")
    
except IndexError:
    print(f"ERROR, o indice não existe.")
    
except ValueError:
    print("Erro: Por favor, digite um número inteiro válido.")
    