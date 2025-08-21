#
# autor: Michel
# data: 19/08/2025

# importar as classes
# sintaxe para importação de classes
# from nome_do_arquivo import NomeDaClasse 
# o `as` permite renomear a classe importada
# o nome do arquivo deve ser o caminho relativo ao diretório atual
# ex:

from vazia import Vazia as V
from pessoa import Pessoa
from numeros import Numeros as N

# criar objetos
v1 = V()  # objeto da classe Vazia 
p1 = Pessoa()
p2 = Pessoa()
n1 = N(3,5) # objeto da classe Numeros com atributos num1 = 3 e num2 = 5

#
print(type(v1))
print(f"p1 = {p1.nome}")
print(f"p1 = {p1.nome}")
print(f"p2 = {p2.nome}")
p1.olaMundo() # chama o método olaMundo da classe Pessoa 
p2.olaMundo()

print(f"{n1.num1} + {n1.num2} = {n1.num1} + {n1.num2}")
print(f"{n1.num1} + {n1.num2} = {n1.num1 + n1.num2}")
print(f"{n1.num1} - {n1.num2} = {n1.num1 - n1.num2}")
print(f"{n1.num1} * {n1.num2} = {n1.num1 * n1.num2}")
print(f"{n1.num1} / {n1.num2} = {n1.num1 / n1.num2}")