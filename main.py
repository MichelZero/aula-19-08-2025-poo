#
# autor: Michel
# data: 19/08/2025

# importar as classes
from vazia import Vazia as V
from pessoa import Pessoa
from numeros import Numeros as N

# criar objetos
v1 = V()
p1 = Pessoa()
p2 = Pessoa()
n1 = N(3,5)

#
print(type(v1))
print(f"p1 = {p1.nome}")
p1.nome = "Davi"
print(f"p1 = {p1.nome}")
print(f"p2 = {p2.nome}")
p1.olaMundo()
p2.olaMundo()

print(f"{n1.num1} + {n1.num2} = {n1.num1} + {n1.num2}")
print(f"{n1.num1} + {n1.num2} = {n1.num1 + n1.num2}")
print(f"{n1.num1} - {n1.num2} = {n1.num1 - n1.num2}")
print(f"{n1.num1} * {n1.num2} = {n1.num1 * n1.num2}")
print(f"{n1.num1} / {n1.num2} = {n1.num1 / n1.num2}")