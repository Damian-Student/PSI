a= 'Lorem Ipsum jest tekstem stosowanym jako przykładowy wypełniacz w przemyśle poligraficznym. Został po raz pierwszy użyty w XV w. przez nieznanego drukarza do wypełnienia tekstem próbnej książki. Pięć wieków później zaczął być używany przemyśle elektronicznym, pozostając praktycznie niezmienionym. Spopularyzował się w latach 60. XX w. wraz z publikacją arkuszy Letrasetu, zawierających fragmenty Lorem Ipsum, a ostatnio z zawierającym różne wersje Lorem Ipsum oprogramowaniem przeznaczonym do realizacji druków na komputerach osobistych, jak Aldus PageMaker'
print(a)
imie = 'Damian'
nazwisko = 'Monikowski'

liczbaLiter_1 = 0
liczbaLiter_2 = 0

for i in a:
    if i == imie[2]:
        liczbaLiter_1+=1
    elif i == nazwisko[3]:
        liczbaLiter_2+=1

print("W tekście jest "+str(liczbaLiter_1)+" liter m oraz "+str(liczbaLiter_2)+" liter i.")
