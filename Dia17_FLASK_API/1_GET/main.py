from flask import Flask

app = Flask(__name__)

estoque = [
    {"codigo": 101, "nome": "Camiseta", "categoria": "Vestuário", "quantidade": 50, "preco": 39.90},
    {"codigo": 102, "nome": "Calça Jeans", "categoria": "Vestuário", "quantidade": 30, "preco": 99.90},
    {"codigo": 103, "nome": "Tênis Esportivo", "categoria": "Calçados", "quantidade": 20, "preco": 149.90},
    {"codigo": 104, "nome": "Relógio Digital", "categoria": "Acessórios", "quantidade": 15, "preco": 199.90},
    {"codigo": 105, "nome": "Mochila Escolar", "categoria": "Utilidades", "quantidade": 25, "preco": 79.90},
    {"codigo": 106, "nome": "Caderno Universitário", "categoria": "Papelaria", "quantidade": 100, "preco": 14.90},
    {"codigo": 107, "nome": "Caneta Azul", "categoria": "Papelaria", "quantidade": 200, "preco": 2.50},
    {"codigo": 108, "nome": "Fone de Ouvido", "categoria": "Eletrônicos", "quantidade": 10, "preco": 59.90},
    {"codigo": 109, "nome": "Carregador Portátil", "categoria": "Eletrônicos", "quantidade": 8, "preco": 129.90},
    {"codigo": 110, "nome": "Livro de Programação", "categoria": "Livros", "quantidade": 18, "preco": 89.90},
]


@app.route('/', methods=['GET'])
def index():
    return {"mensagem":"pagina inicial da api"}, 200

@app.route('/produtos', methods=['GET'])
def get_produtos():
    return estoque

if __name__ == '__main__':
    app.run(debug=True)