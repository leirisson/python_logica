while True:
    try:
        numero = int(input("numero: "))
        resultado = 100 / numero
    except ValueError:
        print("informe um valor numerico")
        continue

    except ZeroDivisionError:
        print("Erro: Não exixte divisão por zero")
        continue
        
    else:
        print(f"resultado da divisão: {resultado}")
        break
    