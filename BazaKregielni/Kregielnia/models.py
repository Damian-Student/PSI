from django.db import models

class Pracownicy(models.Model):
    idPracownika = models.AutoField(primary_key=True)
    imie = models.CharField(max_length=50)
    nazwisko = models.CharField(max_length=50)
    stanowisko = models.CharField(max_length=50)

    def __str__(self):
        return self.nazwisko

class Pensje(models.Model):
    Pracownik = models.ForeignKey(Pracownicy, on_delete=models.CASCADE)
    pensja = models.IntegerField(default=1600)

    def __str__(self):
        return self.pensja

class Klienci(models.Model):
    idKlienta = models.AutoField(primary_key=True)
    imie = models.CharField(max_length=50)
    nazwisko = models.CharField(max_length=50)

    def __str__(self):
        return self.nazwisko

class listaTorow(models.Model):
    nrToru = models.AutoField(primary_key=True)
    stan = models.CharField(max_length=45)

    def __str__(self):
        return self.stan

class wynajemToru(models.Model):
    nrToru = models.ForeignKey(listaTorow, on_delete=models.CASCADE)
    idKlienta = models.ForeignKey(Klienci, on_delete=models.CASCADE)
    dataWynajecia = models.CharField(max_length=100, default="1.01.1970")
    czasWynajecia = models.IntegerField(default=1)
    cenaWynajmu = models.IntegerField(default=50)

    def __str__(self):
        return self.nrToru