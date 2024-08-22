# TUPLA
# sequencia de itens
# estrutura imutável - não pode ser modificada

tupla = (3, 6, 2, 10, 30)

print(tupla[0])   # da pra ver o valores dos indices indicados

for item in tupla: # é possível percorrer a tupla
    print(item)

# tupla vazia
tupla = ()
print(tupla)

# tupla com 1 único elemento
tupla = (10,)
print(tupla)

tupla = (4, 6, 10, 3, 1)  # da pra esses recursos:
print(max(tupla))
print(min(tupla))
print(sum(tupla))
print(len(tupla))

print(tupla.count(6))
print(tupla.index(6))


ufs = ('AC', 'SP', 'RJ')

coordenadas = [(23.555, 10.888), (45.489, 34.989)]
print(coordenadas[0][1])

coordenadas[0] = 3
print(coordenadas)

tupla = ([3, 5, 6], [1, 2, 3])
tupla[0][0] = 999
print(tupla)

# list - converte uma tupla em lista
tupla = (6, 5, 4)
lista = list(tupla)
print(lista)

# tuple - converte uma lista em tupla
lista = [4, 7, 10]
tupla = tuple(lista)
print(tupla)


tupla = (4, 1, 70, 3, 2)
print(tupla)
lista = list(tupla)
lista.sort()
tupla = tuple(lista)
print(tupla)