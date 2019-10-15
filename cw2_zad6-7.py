#zad6
#definicje
firstList = []
for i in range(10):
    firstList.append(i+1)

#edycja list
secondList = firstList[5:]
firstList = firstList[:5]

#wyświetl
print(firstList)
print(secondList)

#zad7
#definicje
list = firstList + secondList
copy = list

#dodaje 0
list.insert(0,0)

#sortuje malejąco
list.sort(reverse=True)

#wyświetl
print(list)