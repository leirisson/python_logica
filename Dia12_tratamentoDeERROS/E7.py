def verificar_numero_positivo(numero):
    if numero < 0:
        # Levantando uma exceção personalizada com uma mensagem
        raise ValueError("Erro: O número não pode ser negativo.")
    return "Número válido! É positivo."

try:
    numero = float(input("digite um valor numerico: "))
    resultado =verificar_numero_positivo(numero)

except ValueError as e:
    print(e)


else:
    print(f"resultado: {resultado}")
