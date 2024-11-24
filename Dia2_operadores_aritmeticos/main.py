from exercicios import exercicios

soma = exercicios.soma_de_valores(5,8)
sub = exercicios.subtracao_de_valores(100,19)
multi = exercicios.multi(2,48)
div = exercicios.divisao(64,12)
div_inteiro = exercicios.divisao_por_inteiro(50,4)
rest_div = exercicios.resto_da_divisao(10,3)
potencia = exercicios.potenciacao(2,5)

print(exercicios.msg())
print(f"resultado da soma: {soma}")
print(f"resultado da subtração: {sub}")
print(f"resuoltado da multiplicação: {multi}")
print(f"resultado da divisão: {div:.2f}")
print(f"divisão por inteiro: {div_inteiro}")
print(f"resto da divisão: {rest_div}")
print(f"potenciação: {potencia}")
