#definicje
imie = "Karol"
nazwisko = "Kulesza"

#odwrócenie
revesrseImie = slice(-1, -6, -1)
revNazwisko = slice(-1, -8, -1)

#wyświetl
print((imie[revesrseImie].capitalize()), (nazwisko[revNazwisko].capitalize()))