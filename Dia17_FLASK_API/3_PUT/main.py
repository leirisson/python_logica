from flask import Flask, jsonify, request


emprestimos = [
    {
        "id": 1,
        "nome": "Leirisson",
        "sobrenome": "Souza",
        "emprestimo": 1000,
        "juros": 30,
        "valor_a_pagar": 1300
    },
    {
        "id": 2,
        "nome": "Ana",
        "sobrenome": "Silva",
        "emprestimo": 1500,
        "juros": 25,
        "valor_a_pagar": 1875
    },
    {
        "id": 3,
        "nome": "Carlos",
        "sobrenome": "Santos",
        "emprestimo": 800,
        "juros": 20,
        "valor_a_pagar": 960
    },
    {
        "id": 4,
        "nome": "Mariana",
        "sobrenome": "Alves",
        "emprestimo": 2000,
        "juros": 35,
        "valor_a_pagar": 2700
    },
    {
        "id": 5,
        "nome": "João",
        "sobrenome": "Ferreira",
        "emprestimo": 1200,
        "juros": 28,
        "valor_a_pagar": 1536
    },
    {
        "id": 6,
        "nome": "Fernanda",
        "sobrenome": "Oliveira",
        "emprestimo": 500,
        "juros": 18,
        "valor_a_pagar": 590
    },
    {
        "id": 7,
        "nome": "Ricardo",
        "sobrenome": "Lima",
        "emprestimo": 2500,
        "juros": 40,
        "valor_a_pagar": 3500
    },
    {
        "id": 8,
        "nome": "Beatriz",
        "sobrenome": "Nascimento",
        "emprestimo": 1700,
        "juros": 22,
        "valor_a_pagar": 2074
    },
    {
        "id": 9,
        "nome": "Lucas",
        "sobrenome": "Costa",
        "emprestimo": 900,
        "juros": 15,
        "valor_a_pagar": 1035
    },
    {
        "id": 10,
        "nome": "Patrícia",
        "sobrenome": "Mendes",
        "emprestimo": 3000,
        "juros": 50,
        "valor_a_pagar": 4500
    }
]





app = Flask(__name__)


@app.route("/api/v1/", methods=['GET'])
def home():
    return jsonify({"mensagem":"hello api flask"})

@app.route("/api/v1/emprestimos", methods=['GET'])
def get_emprestimos():
    todos_os_emprestimos = jsonify(emprestimos)
    return todos_os_emprestimos

@app.route('/api/v1/emprestimos/<int:id_emprestimo>', methods=['GET'])
def get_emprestimo_id(id_emprestimo):

    for emprestimo in emprestimos:
        if emprestimo['id'] == id_emprestimo:
            emprestimo_convertido = jsonify(emprestimo)
            return emprestimo_convertido, 200
    return jsonify({"error":"emprestimos não encontrado"})

@app.route('/api/v1/emprestimos', methods=['POST'])
def criar_emprestimo():
    data = request.json
    emprestimo = {
        'nome': data['nome'],
        'sobrenome':data['sobrenome'],
        'emprestimo':data['emprestimo'],
        'juros':data['juros'],
        'valor_a_pagar': data['valor_a_pagar']
    }

    emprestimos.append(emprestimo)
    emprestimo_convertido = jsonify(emprestimo)
    
    return { "mensagem":"emprestimo realizado com sucesso"}, 201


@app.route("/api/v1/emprestimos/<int:id_emprestimo>", methods=['PUT'])
def get_emprestimo_por_id(id_emprestimo):
    data = request.json
    for emprestimo in emprestimos:
        if emprestimo['id'] == id_emprestimo:
            emprestimo['nome'] = data['nome']
            emprestimo['sobrenome'] = data['sobrenome']
            emprestimo['juros'] = data['juros']
            emprestimo['emprestimo'] = data['emprestimo']
            emprestimo['valor_a_pagar'] = data['valor_a_pagar']
    return {"mensagem":"emprestimo atualizado com sucesso"}, 200


if __name__ == "__main__":
    app.run(debug=True)
    # print('rodando em => http://127.0.0.1:5000/api/v1/')