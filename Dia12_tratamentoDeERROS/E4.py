# try, except, else, finally

# except => tratar um error 
# else => para uma condição positiva
# finally => que roda sempre, independente da situação



try:
    arquivo = open("Dia12_tratamentoDeERROS\dados.txt", "r") 
    conteudo = arquivo.read()
except FileNotFoundError:
    print("Erro: o arquivo não existe")
else:
    print('arquivo lido')
    print(conteudo)
finally:
    print("opração finalizada.")
    if "arquivo" in locals(): # fechando arquivo 
        arquivo.close()
        print("arquivo fechado !")