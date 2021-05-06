lista = list()

lista.append(1)
lista.append(2)
lista.append(3)
lista.append(4)
lista.append(5)
lista.append(6)
lista.append(7)
lista.append(8)

while len(lista) > 0:
	first_item, last_item = lista[0], lista[-1]
	print("primero: ", first_item, "ultimo: ", last_item)
	lista = lista[1:len(lista) - 1]
	print(lista)
