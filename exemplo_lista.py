# Listas 

# lista vazia
lista = []


# exemplo de lista
lista = [4, 10, 59, 2]


# estrutura heterogenea
lista = [4, 6, "Texto", 3.6, True, False, 8]

# estrutura mutável (pode ser mudada)
lista = [5, 6, 7, 10]
lista[0] = 9090909090909009
print(lista)


# percorrer os itens da lista (Apenas consulta os itens da lista)
for item in lista:
    print(item)


# contar os numeros pares
lista = [5, 6, 10, 30, 7]
cont = 0
for item in lista:
    if item % 2 == 0:
        cont += 1
    print(f"A quantidade de pares: {cont}")


# percorrer os indices da lista (consegue consultar e pode alterar os valores da lista)
for i in range(len(lista)):
    print(lista[i])


# alterar os numeros pares para zero
for i in range(len(lista)):
    if lista[i] % 2 == 0:
        lista[i] = 0
print(lista)


# len - retornar o tamanho da lista
lista = [4, 50, 2, 5, 10]
n = len(lista)   # ou print(len(lista))
print(n)


# append - insere um item no fianl da lista
lista = [4, 50, 2, 5, 10]
lista.append(100)
print(lista)


# insert - insere um item em um indise especifico da lista (indice, valor)
lista.insert(0, 200)
print(lista)


# pop - remove o ultimo item da lista
lista.pop()
print(lista)

# pop(indice) - remove o item de um indice
lista.pop(2)
print(lista)


# remove - remove um item da lista de acordo com o valor indicado, esse remove apenas o primeiro 200
lista = [3, 200, 40, 6, 200, 5, 200, 200]
lista.remove(200)
print(lista)

while 200 in lista:  # isso faz remover todos os 200 da lista
    lista.remove(200)
print(lista)


# count - conta a quatidade de vezes que um item ocorre na lista
lista = [2, 5, 6, 7, 6, 10, 6]
print(lista.count(6))

# index - retorna o indice de um item
#lista = [2, 5, 6, 7, 6, 10, 6]
#valor = int(input("Digite um numero: "))
#if valor in lista:
#    print(lista.index(valor))
#else: 
#    print("O valor não está na lista")


# exibe todos os indice onde um item se enocontra
print("-----------------")
lista = [3, 200, 5, 6, 7, 200]
for i in range(len(lista)):
    if lista[i] == 20:
        print(i)

# sort - ordena uma lista em ordem crescente
lista = [3, 200, 5, 6, 7, 200]
lista.sort()
print(lista)    

lista = ['maça', 'laranja', 'abacaxi', 'abc', 'teste', 'Abacaxi']
lista.sort()
print(lista)

# sort(reverse=True) - ordena uma lista em ordem decrescente
lista = ['maça', 'laranja', 'abacaxi', 'abc', 'teste', 'Abacaxi']
lista.sort(reverse=True)
print(lista)

# sorted - retorna uma cópia da lista ordenada
lista = [4, 8, 1, 3, 19, 2]
print(lista)
listaordenada = sorted(lista)
print(listaordenada)

# min - menor item da lista
lista = [4, 8, 1, 3, 19, 2]
print(min(lista))

# max - maior item da lista
print(max(lista))

# sum - somatótio de uma lista
print(sum(lista))

# media dos itens da lista
media = sum(lista) / len(lista)
print(media)

# preencher uma lista com entradas do usuário
lista = []
for i in range(5):
    n = int(input("Digite um numero: "))
    lista.append(n)
print(lista)


lista = []
while True:                                   # quantidade indeterminada (até digitar zero)
    n = int(input("Digite um numero: "))
    if n == 0:
        break
    lista.append(n)
print(lista)