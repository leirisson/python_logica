
nome = input("nome do produto: ")
quantidade = int(input("quantidade: "))
preco = float(input("valor do produto: "))

produto = {
    'nome_produto' : nome,
    'qunatidade':quantidade,
    'preco':preco,
    'descricao': 'teste'
}

print(produto)


del produto['descricao']

print(produto)
