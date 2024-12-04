from flask import Flask, request

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
    return mensagem, 200

@app.route('/produtos', methods=['POST'])
def set_produto():
    produto = request.json

    mensagem = {
        "mensgaem": "produto cadastrado com sucesso.",
        "info": produto
    }

    return mensagem, 2001


if __name__ == "__main__":
    app.run(debug=True)
