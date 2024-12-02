# Validação de Entrada de Data

from datetime import datetime

data_aniversario = input("qual a data do seu aniversario: ")

try:
    # formatando data
    data_formatada = datetime.strptime(data_aniversario, "%d/%m/%Y")    

except ValueError:
    print("formato de data, invalida ")

else:
    print(f"data de nacimento: {data_formatada}")

finally:
    print("processo finalizado")