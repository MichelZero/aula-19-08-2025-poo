#
# autor: Michel
# data: 19/08/2025

# Classe números

# sintaxe da classe
# aqui é um exemplo de classe em Python com inicialização de atributos
# o construtor __init__ é utilizado para inicializar os atributos da classe
# os parâmetros do construtor são passados durante a criação do objeto
# exemplo: objeto = NomeDaClasse(param1, param2)
# no caso da classe Numeros, os parâmetros são num1 e num2
# os atributos são inicializados com os valores passados pelo construtor 
# o self é a referência à instância atual da classe
# o self.num1 não é o mesmo que num1, pois self.num1 se refere ao atributo da instância
# enquanto num1 é o parâmetro do construtor


class Numeros:
    
    def __init__(self, num1, num2): # construtor da classe Numeros 
        self.num1 = num1
        self.num2 = num2