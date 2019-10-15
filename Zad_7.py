lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lista_nowa = lista[5:]
lista = lista[:5]
lista.extend(lista_nowa)
print(lista)
lista.insert(0,0)
print(lista)
kopia = lista
kopia.reverse()
print(kopia)