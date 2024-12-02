
nome_livro = input("qual o nome do livro: ")
quantidade = int(input("qual a quantidade do livro: "))

livro = {
    'titulo': nome_livro,
    'quantidade': quantidade
}

atualizacao = input("atualizar a quantidade: ")

livro['quantidade'] = atualizacao

print(livro)