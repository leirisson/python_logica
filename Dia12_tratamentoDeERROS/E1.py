try:
    numero = int(input("informe um numero:  "))
    print("valor informado: ", numero)
except ValueError:
    print("Erro de dados, informe um valor numerico.")