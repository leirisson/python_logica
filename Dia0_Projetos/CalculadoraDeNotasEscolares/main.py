from modulos.menusistema import menu
from modulos.tituloSistema import tituloSistema
from modulos.modNotas import lancar_notas_alunos
from modulos.modNotas import listar_notas_alunos
from modulos.modNotas import editar_alunos
def main():
    all_alunos = [{'nome':'Leirisson', 'nota1':6.5,  'nota2':6.5,  'nota3':6.5,  'diciplina':'portugues'}]
    
    while True:
        try:
            tituloSistema("Calculadora de Notas Escolares")
            menu()
            
            op_menu = int(input("Escolha uma opção: "))
            
            if op_menu == 1:
                lancar_notas_alunos(all_alunos)
            elif op_menu == 2 :
                editar_alunos(all_alunos)
      
            else:
                print("opção invalida informe, tente novamente.")
                
        except ValueError:
            print("informe um valor numero.")
    
        
    

if __name__ == "__main__":
    main()