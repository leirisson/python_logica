from flask import Flask, request,jsonify

app = Flask(__name__)

estoque = [
    {"codigo": 101, 
     "nome": "Camiseta", 
     "categoria": "Vestuário", 
     "quantidade": 50,
     "preco": 39.90},
     
    {"codigo": 102, 
     "nome": "Calça Jeans", 
     "categoria": "Vestuário", 
     "quantidade": 30, 
     "preco": 99.90}
]

@app.route('/', methods=['GET'])
def index():
    mensagem = {"mensagem":"criando API com Flask"}
    return jsonify(estoque), 200


@app.route('/produtos', methods=['GET'])
def get_produtos():
    return estoque, 200

@app.route('/produtos', methods=['POST'])
def set_produto():
    data = request.json

    produto = {
        'codigo':data['codigo'],
        'nome':data['nome'],
        'preco':data['preco'],
        'categoria':data['categoria'],
        'quantidade':data['quantidade']
        
    }

    estoque.append(produto)

    mensagem = {
        "mensgaem": "produto cadastrado com sucesso.",
        "info": produto
    }

    return jsonify(mensagem), 201


if __name__ == "__main__":
    app.run(debug=True)
