import json


dados = {
    'nome':'Francisco',
    'idade':45
}

try:
    with open("Dia13_arquivos/arquivos/db.json", 'w') as db_json:
        json.dump(dados, db_json, indent=3)
except FileNotFoundError:
    print("Erro ao tentar criar arquivo")

else: 
    print("Arquivo criado")