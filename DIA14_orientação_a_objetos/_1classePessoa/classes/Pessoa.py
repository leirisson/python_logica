class Pessoa:
    def __init__(self, nome, idade, nacimento, peso):
        self.nome = nome
        self.idade = idade
        self.nacimento = nacimento 
        self.peso = peso
        
    def apresentar(self):
        print(f"olá, meu nome é {self.nome} e eu tenho idade {self.idade} anos.")
    
    
    
    
pessoa = Pessoa('leirisson',25,'20/0/2/199',70)
pessoa.apresentar()