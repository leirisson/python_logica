

def div(a,b):
   divisor = a /b
   return divisor
        
try:
    resultado_div = div(2,0)
except ZeroDivisionError:
    print("erro ao dividir numero por zero !")

except ValueError:
    print("Valor informado invalido !")
        
else:
    print(f"O resultado da divisão é: {resultado_div:.2f}")
        
finally:
    print("Fim do processo.")

