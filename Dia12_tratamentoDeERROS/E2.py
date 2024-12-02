# Capturando Erro de Divisão por Zero

try:
    numero1 = float(input("primeiro valor: "))
    numero2 = float(input("segundo valor: "))
    
    resultado = numero1 / numero2
    
    print(f"resultado: {resultado}")
    
except ZeroDivisionError:
    print("divisão por zero não é permitida.")