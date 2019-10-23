import random

#definicje
phoneNunbersList = []

#dodaje 3 powtórzenia
phoneNunbersList.append(123456789)
phoneNunbersList.append(123456789)
phoneNunbersList.append(123456789)

#dodaje 2 powtórzenia
phoneNunbersList.append(987654321)
phoneNunbersList.append(987654321)

#dodaje inne randomowe numery
for i in range(10):
    phoneNunbersList.append(random.randint(100000000, 999999999))

phoneNunbersList = set(phoneNunbersList)

#wyświetl
print(phoneNunbersList)