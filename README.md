# README: Manipulação de Listas e Tuplas em Python

Este README fornece uma visão geral do código que demonstra a utilização de listas e tuplas em Python. Tuplas e listas são dois tipos de coleções usadas para armazenar múltiplos itens. Tuplas são imutáveis, o que significa que não podem ser alteradas depois de criadas, enquanto listas são mutáveis e podem ser modificadas.

Tuplas
As tuplas são sequências de itens que são imutáveis. Aqui estão alguns exemplos e operações básicas com tuplas:

Exemplos e Operações
python
Copiar código
# Criar uma tupla
tupla = (3, 6, 2, 10, 30)

# Acessar um valor pelo índice
print(tupla[0])   # Saída: 3

# Percorrer a tupla
for item in tupla:
    print(item)

# Tupla vazia
tupla = ()
print(tupla)     # Saída: ()

# Tupla com um único elemento
tupla = (10,)
print(tupla)     # Saída: (10,)

# Operações com tuplas
tupla = (4, 6, 10, 3, 1)
print(max(tupla))   # Maior valor
print(min(tupla))   # Menor valor
print(sum(tupla))   # Soma dos valores
print(len(tupla))   # Comprimento da tupla

print(tupla.count(6))  # Contar ocorrências do valor 6
print(tupla.index(6))  # Índice da primeira ocorrência do valor 6

# Tuplas aninhadas e imutáveis
ufs = ('AC', 'SP', 'RJ')
coordenadas = [(23.555, 10.888), (45.489, 34.989)]
print(coordenadas[0][1])  # Acessa o segundo valor da primeira tupla

# Tupla com listas internas (a lista é mutável, mas a tupla não)
tupla = ([3, 5, 6], [1, 2, 3])
tupla[0][0] = 999
print(tupla)  # A primeira lista dentro da tupla é modificada

# Conversão entre tupla e lista
tupla = (6, 5, 4)
lista = list(tupla)
print(lista)  # Convertendo tupla para lista

lista = [4, 7, 10]
tupla = tuple(lista)
print(tupla)  # Convertendo lista para tupla

# Ordenar uma tupla
tupla = (4, 1, 70, 3, 2)
lista = list(tupla)
lista.sort()
tupla = tuple(lista)
print(tupla)
Listas
As listas são coleções mutáveis que podem conter diferentes tipos de itens. Aqui estão alguns exemplos e operações básicas com listas:

Exemplos e Operações
python
Copiar código
# Lista vazia
lista = []

# Exemplo de lista
lista = [4, 10, 59, 2]

# Estrutura heterogênea
lista = [4, 6, "Texto", 3.6, True, False, 8]

# Estrutura mutável
lista = [5, 6, 7, 10]
lista[0] = 9090909090909009
print(lista)

# Percorrer itens da lista
for item in lista:
    print(item)

# Contar números pares
lista = [5, 6, 10, 30, 7]
cont = 0
for item in lista:
    if item % 2 == 0:
        cont += 1
print(f"A quantidade de pares: {cont}")

# Percorrer índices da lista
for i in range(len(lista)):
    print(lista[i])

# Alterar números pares para zero
for i in range(len(lista)):
    if lista[i] % 2 == 0:
        lista[i] = 0
print(lista)

# len - tamanho da lista
lista = [4, 50, 2, 5, 10]
n = len(lista)
print(n)

# append - adicionar item ao final da lista
lista = [4, 50, 2, 5, 10]
lista.append(100)
print(lista)

# insert - adicionar item em um índice específico
lista.insert(0, 200)
print(lista)

# pop - remover o último item ou item em um índice específico
lista.pop()
print(lista)
lista.pop(2)
print(lista)

# remove - remover item pelo valor
lista = [3, 200, 40, 6, 200, 5, 200, 200]
lista.remove(200)
print(lista)

# Remover todas as ocorrências de um valor
while 200 in lista:
    lista.remove(200)
print(lista)

# count - contar ocorrências de um item
lista = [2, 5, 6, 7, 6, 10, 6]
print(lista.count(6))

# index - encontrar índice de um item
# valor = int(input("Digite um número: "))
# if valor in lista:
#     print(lista.index(valor))
# else: 
#     print("O valor não está na lista")

# Exibir todos os índices onde um item está presente
print("-----------------")
lista = [3, 200, 5, 6, 7, 200]
for i in range(len(lista)):
    if lista[i] == 200:
        print(i)

# sort - ordenar lista em ordem crescente
lista = [3, 200, 5, 6, 7, 200]
lista.sort()
print(lista)

# Ordenação alfabética e sensível a maiúsculas/minúsculas
lista = ['maça', 'laranja', 'abacaxi', 'abc', 'teste', 'Abacaxi']
lista.sort()
print(lista)

# Ordenação em ordem decrescente
lista.sort(reverse=True)
print(lista)

# sorted - retornar cópia da lista ordenada
lista = [4, 8, 1, 3, 19, 2]
listaordenada = sorted(lista)
print(listaordenada)

# min - menor item da lista
lista = [4, 8, 1, 3, 19, 2]
print(min(lista))

# max - maior item da lista
print(max(lista))

# sum - soma dos itens da lista
print(sum(lista))

# Média dos itens da lista
media = sum(lista) / len(lista)
print(media)

# Preencher uma lista com entradas do usuário
lista = []
for i in range(5):
    n = int(input("Digite um número: "))
    lista.append(n)
print(lista)

# Lista com quantidade indeterminada (até digitar zero)
lista = []
while True:
    n = int(input("Digite um número: "))
    if n == 0:
        break
    lista.append(n)
print(lista)
Observações
Tuplas são úteis para armazenar dados que não devem ser alterados. Elas são mais rápidas e seguras para acesso de dados constantes.
Listas são versáteis e podem ser modificadas conforme necessário. Elas oferecem mais funcionalidades, como adicionar e remover itens.
Para mais informações sobre manipulação de listas e tuplas, consulte a documentação oficial do Python.
