# in python variables store values or work as pointers to objects

#value
number = 1
value = 3.5

#string or sequence of characters
text = 'this is a text'

print(value)

#for simple types, python performs a copy of the value to the new variable
a = 3
b = a
b = b-1
print(a, b)

#for complex types, python performs a copy of the reference to the object
x = [1, 2, 3]
y = x
y[0] = 5
print(x)

#thus to replicate an entire object you need to use copy
import copy
y = copy.copy(x)

#now to create logic is essecial to work with conditions
if 2 > 1:
    print('looks like this is true')
    
    
if value > 5:
    print("retornou true e passou na condicao - valor maior que 5")
elif value > 3:
    print("retornou true e passou na condicao - valor maior que 3")
else:
    print("nao passou na condicao")
    
#for repeting processes you can create functions - blocks of code you can execute again
def myfunction(x):
    return x+1

result = myfunction(4)
print(result)

# math quadratic function
import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return x**2

x = np.linspace(-4, 4, 100)
plt.plot(x,f(x))

# lets create a simple calculator

def calc(val1, val2, operation):
    if(operation == '+'):
        return val1+val2
    elif(operation == '-'):
        return val1-val2
    elif(operation == '*'):
        return val1*val2
    elif(operation == '/'):
        return val1/val2
    else:
        return 'sorry i wasnt able to compute this'
    
resultado_conta = calc(2,5,'+')
print(resultado_conta)

#you can also store list like this:

lista = ["andre", "lola", "baru"]
lista2 = [5, 2, 3]
print('lista2:', lista2)
print(len(lista))
print("verificando o tipo da objetivo guardado em lista2:", type(lista2))

#lets start with an empity list and add elements
queue = []
print(queue)

queue.append("Joao")
print(queue)
queue.append("maria")
print(queue)
print("the next one in the line is: "+str(queue[0]))

#now lets remove joao
queue.pop(0)
print("the next one in the line is: "+str(queue[0]))

#you can also use functions like reverse() or sort()
#you can also represent a matrix like this:


minha_matriz = [
                [5, 66, 7, 8, 55, 40],
                [7, 22, 8, 10, 1, 4],
                [1, 15, 22, 40, 35, 7]
              ]

print("minha matriz:")
print(minha_matriz)

#also you can represent more complex structures with directionaries
exemplo_dicionario = {
    "nome": "Joao",
    "idade": 31,
    "plano_saude": "Sulamerica"
}

print("exibindo o cadastro do joao: "+str(exemplo_dicionario))

#alterando a idado do joao
exemplo_dicionario["idade"] = 32

print("exibindo a atualizacao cadastral: "+str(exemplo_dicionario))

#another example:
pacientes = dict()
pacientes = {"andre": 32, "lola": 27, "baru": 4}
pacientes["andre"] += 1
print(pacientes["andre"])
nomes = pacientes.keys()
print("extraindo as chaves do dicionario", type(nomes))
print(nomes)

#tuples
x = 10.25
y = 20.30

coordinate = (x, y)

print(coordinate)
print(type(coordinate))

#set is a non sorted list with no repetition
ids = set([1, 5, 7, 11, 13])
ids.add(15)
conjunto2 = set([5, 7])
print("diferenca conjuntos", ids-conjunto2)

#loops are structures of repetition - for
for x in range(6):
  print("executando o indice: "+str(x))

print(range(6))
print(list(range(6)))

lista = ["Andre", "Lola", "Baru"]

for x in lista:
  print(x)
  
#outros exemplos de loop mais complexos

print('loop em uma lista de nomes')
names = ['andre', 'lola', 'baru']
for name in names:
    print(name)

print('\nloop em dicionario com nome e idade')#lembre-se que dicionarios nao sao ordenaveis
names = {'andre':32, 'lola':27, 'baru':4}
for name in names.keys():
    print(name, names[name])

print('\nloop em dicionario com nome e idade - da pra fazer sem usar keys tbm e ordenando a lista de nomes')
names = {'andre':32, 'lola':27, 'baru':4}
for name in sorted(names):
    print(name, names[name])

print('\nloop for em lista com ordem contraria')
names = {'andre':32, 'lola':27, 'baru':4}
for name in sorted(names, reverse=True):
    print(name, names[name])

print('\nverifica se o numero n eh primo')
n = 5
is_prime = True
for i in range(2,n):
    if n%i == 0:
        is_prime = False
print(is_prime)

print('\ndigamos que vc tem uma lista de numeros e quer pegar o quadrado dela')
numeros = range(10)

#jeito ruim
quadrados = []
for n in numeros:
    quadrados.append(n**2)
print(quadrados)

#jeito pythonico - bem mais clean - o nome disso no python é list comprehensions
quadrados2 = [n**2 for n in numeros]
print(quadrados2)

#inner loop
for x in range(5):
    for y in range(5):
        print("x:", x, "Y:", y)
        
#while

valor = 5

while valor > 0:
  print("o valor agora eh: "+str(valor))
  valor = valor - 1
  
count = 0

while True:
  print("vai executando toda a vida...")
  count += 1
  if count == 5:
    print('opa, vou parar o loop por aqui')
    break

#STRINGS - como manipular sequencias de caracteres no python
exemplo_palavra = "Mariotti"
exemplo_frase = "Mariotti eh meu professor esse semestre"
print(exemplo_palavra, type(exemplo_palavra))
print("o nome Mariotti possui", len(exemplo_palavra), "letras")
print("valor retornado quando o que vc esta buscando nao existe:", str(exemplo_frase.find('python')))
if exemplo_frase.find('professor') != -1:
  print('existe a palavra professor na frase e comeca no indice', exemplo_frase.find('professor'))
print(exemplo_palavra.upper())
print(exemplo_palavra.lower())
print(exemplo_frase.replace('esse semestre', 'de python'))
print(exemplo_frase.split())
print(exemplo_palavra[0:3])

#try
def calc(x, y):
  try:
    print(x/y)
  except ZeroDivisionError:
    print("tentou dividir por zero neh seu danado")
  except:
    print("pelo jeito vc nao colocou um numero ne rapaz... usuarios...")
    
calc(4, 2)
calc(4, 0)
calc('andre', 2)