def lancar_notas_alunos(list_alunos):
    nome = input("Nome do aluno: ")
    nota1 = float(input("nota do aluno: "))
    nota2 = float(input("nota do aluno: "))
    nota3 = float(input("nota do aluno: "))
    diciplina = input("qual a diciplina: ")

    aluno_completo = {'nome': nome, 'nota1':nota1, 'nota2':nota2, 'nota3':nota3, 'diciplina':diciplina }
    
    list_alunos.append(aluno_completo)
    
    print(f"Notas do aluno: {aluno_completo['nome']} cadastradas com sucesso.")
    input("Aperte, ENTER para continuar.")

def editar_alunos(list_alunos):
    if not list_alunos:
        print("nem uma aluno cadastardo ...  ")
        return
    
    name_student = input("nome do aluno: ")
    
    for index, aluno in enumerate(list_alunos):
        if name_student in aluno['nome']:
            nome = input("novo nome do aluno: ")
            nota1 = float(input("nova nota do aluno: "))
            nota2 = float(input("nova nota do aluno: "))
            nota3 = float(input("nova nota do aluno: "))
            diciplina = input("nova diciplina: ")
            aluno_completo = {'nome': nome, 'nota1':nota1, 'nota2':nota2, 'nota3':nota3, 'diciplina':diciplina }
            list_alunos.append(aluno_completo)
            input(f"Aluno: {nome} foi atualizado com sucesso. ENTER para continuar.")
            
    
def listar_notas_alunos(list_alunos):
    if not list_alunos:
        print("Nem uma nota foi lançada ainda.")
        return
    
    for indice_aluno, aluno in enumerate(list_alunos):
        print(f"{indice_aluno}º - {aluno['nome']} - Notas: {aluno['nota1']},  {aluno['nota2']},  {aluno['nota3']} - Diciplina: {aluno['diciplina']}")

def excluir_notas(list_alunos):
    if not list_alunos:
        print("nem uma aluno cadastardo ...  ")
        return
    for index_numero, aluno in enumerate(list_alunos):
        