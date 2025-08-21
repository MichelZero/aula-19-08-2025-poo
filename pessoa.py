#
# autor: Michel
# data: 19/08/2025

# Classe pessoa
class Pessoa:
    
    nome = "Padrão"  # nome é um atributo da classe Pessoa, estático e inicializado com "Padrão"
    
    # sintaxe do método
    # def nome_do_metodo(self):
    #     pass
    
    # os nomes dos métodos devem começar com letras minúsculas
    # podem conter letras, números e underscores
    # e devem ser descritivos em relação à sua funcionalidade
    #  ex: def calcular_idade(self):
    # ex: ola_mundo ou olaMundo

    def olaMundo(self): # método da classe Pessoa, o self é a referência à instância atual
        print("olá Mundo da POO!") # exibe uma mensagem no console
