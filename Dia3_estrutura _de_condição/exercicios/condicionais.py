
# ================
#   Nível Básico
# ================

def SistemaDeComprasOnline(valorRotalDaCompra):
    if valorRotalDaCompra > 100:
        return "Você ganhou vale de frete gratis, parabens."
    else:
        return "Você não possui um vale de frete gratis, compras acima de 100R$ ganham frete gratis."


def HorariosDeFuncionamento(horario):
    if horario < 8 or horario > 18:
        return "Loja fechada, Horários de Funcionamento é de 08:00 as 18:00"
    else:
        return "Loja aberta, fecha as 18:00"


def ClassificacaoDeIdade(idade_pessoa):
    if idade_pessoa <= 12:
        return f"Idade: {idade_pessoa} é de uma criança"
    elif idade_pessoa > 12 and idade_pessoa <= 17:
        return f"Idade: {idade_pessoa} é de um(a) adolecente."
    elif idade_pessoa >= 18 and idade_pessoa <= 64:
         return f"Idade: {idade_pessoa} é de um(a) adulto."
    else:
         return f"Idade: {idade_pessoa} é de um(a) idoso(a)"


# ================
#   Nível Médio
# ================

def SistemaDeMultasDeTransito(velocidade_carro):
    if velocidade_carro > 80:
        multa = (velocidade_carro - 80) * 5
        return f"valor da multa a ser paga: {multa} R$"
    else:
        return "Sem multas."


def CalculadoraDeImpostos(fat_anual):
    if fat_anual > 20.000 and fat_anual <= 50000:
        imposto_anual = fat_anual * 0.05
        return f"impostoa pagar: {imposto_anual:.2f}"
    elif fat_anual > 50000:
        imposto_anual = fat_anual * 0.1
        return f"impostoa pagar: {imposto_anual:.2f}"
    else:
        return "status imposto anual: ISENTO"


def SistemaDeVotacao(nacionalidade, idade):
    nacionalidade = nacionalidade.lower()
    
    if nacionalidade == 'brasileira' and idade >= 16:
        return f"Pessoa com a nacionalidade: {nacionalidade} e idade: {idade} estão aptas a votar na proxima eleição"
    
    elif nacionalidade != 'brasileira':
        return f"Pessoa da nacionalidade: {nacionalidade}, não estão aptas a votar no Brasil."
    
    elif nacionalidade == 'brasileira' and idade < 16:
        return f"Pessoas da idade {idade}, não estão aptas a votar no Brasil"
    


def PromocaoProgressiva(valor_compra):
    if valor_compra > 50 and valor_compra <= 100:
        desconto = valor_compra * 0.05
        valor_a_pagar = valor_compra - desconto

        texto_imprimir = f"""
Desconto: 5%
Valor desconto: {desconto:.2f}
Valor a pagar: {valor_a_pagar}
        
"""
        return texto_imprimir
    
    elif valor_compra > 100:
        desconto = valor_compra * 0.1
        valor_a_pagar = valor_compra - desconto
        texto_imprimir = f"""
Desconto: 10%
Valor desconto: {desconto}
Valor a pagar: {valor_a_pagar}       
"""
        return texto_imprimir

    else:
        return f"Compras no valor de  R${valor_compra}: Sem desconto"

        


# ==================
#   Nível Difícil
# ==================

def Classificacao_de_risc_de_credito(salario, quantidade_de_parcelas):
    if salario >= 1500 and salario <= 5000 and quantidade_de_parcelas <=12:
        return f"Risco de emprestimo: médio risco"
    elif salario > 5000:
         return f"Risco de emprestimo: baixo risco"
    else:
        return f"Risco de emprestimo: alto risco"
    
def Sistema_de_avaliacao_de_Alunos(nota_porva1, nota_porva2, nota_porva3):
    media_das_notas = (nota_porva1 + nota_porva2 + nota_porva3) / 3

    if media_das_notas < 5:
        msg = f"""
Nota primeira prova: {nota_porva1}
Nota segunda  prova: {nota_porva2}
Nota terceira prova: {nota_porva3}
Média das provas: {media_das_notas:.2f}
Status aluno: reprovado
"""
        return msg
    elif media_das_notas >= 5 and media_das_notas <= 6.9:
        msg = f"""
Nota primeira prova: {nota_porva1}
Nota segunda  prova: {nota_porva2}
Nota terceira prova: {nota_porva3}
Média das provas: {media_das_notas:.2f}
Status aluno: recuperação
"""
        return msg
    else:
        msg = f"""
Nota primeira prova: {nota_porva1}
Nota segunda  prova: {nota_porva2}
Nota terceira prova: {nota_porva3}
Média das provas: {media_das_notas:.2f}
Status aluno: aprovado
"""
        return msg

def Gestao_de_Estoque_em_Restaurante(nome_produto: str, quantidade_produto):
    if quantidade_produto >= 5 and quantidade_produto <= 20:
        mensagem = f"""
nome do produto: {nome_produto}
quantidade em estoque: {quantidade_produto}
status estoque: Estoque regular
"""
        return mensagem
    elif quantidade_produto > 20:
        mensagem = f"""
nome do produto: {nome_produto}
quantidade em estoque: {quantidade_produto}
status estoque: Estoque cheio
"""
        return mensagem
    else:
        mensagem = f"""
nome do produto: {nome_produto}
quantidade em estoque: {quantidade_produto}
status estoque: Produto em falta
"""
        return mensagem