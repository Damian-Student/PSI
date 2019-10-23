import random

#zad8
#definicje
studentList = []
indexNumbers = []

group = []

#wypełnienie danymi
for i in range(5):
    indexNumbers.append(random.randint(100000, 999999))

studentList.append("Karol Karolowski")
studentList.append("Damian Damianowski")
studentList.append("Ewa Ewolska")
studentList.append("Agnieszka Agowska")
studentList.append("Kamil Kamilowski")

#grupa
for i in range(5):
    student = studentList[i], indexNumbers[i]
    group.append(student)

#wyświetl
print(group)

#zad9
#definicje
dictionary = {}
moreData = {}
dictionary = dict([group[0], group[1], group[2], group[3], group[4]])
moreData = {"age", 26,"e-mail", "k.kulesza1993@o2.pl","birth year", 1993,"street adress", "Olsztyn, ul. Zielona 5, 10-414 Olsztyn"}

#wyświetl
print(dictionary)
print(moreData)

#zad13
result = [dictionary, moreData]
print(result)