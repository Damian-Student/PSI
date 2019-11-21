from rest_framework import serializers
import datetime

##############################################################################

class PracownicySerializer(serializers.Serializer):
    idPracownika = serializers.AutoField(primary_key=True)
    imie = serializers.CharField(max_length=50)
    nazwisko = serializers.CharField(max_length=50)
    stanowisko = serializers.CharField(max_length=50)

    def validateImie(self):
        if (len(self.imie) > 50):
            raise serializers.ValidationError(
                "Imie jest za długie!",
            )

    def validateNazwisko(self):
        if (len(self.nazwisko) > 50):
            raise serializers.ValidationError(
                "Nazwisko jest za długie!",
            )

    def validateStanowisko(self):
        if (len(self.stanowisko) > 50):
            raise serializers.ValidationError(
                "Nazwa stanowiska jest za długa!",
            )

##############################################################################

class PensjeSerializer(serializers.Serializer):
    pensja = serializers.IntegerField

    def validatePensja(self):
        if (self.pensja < 0):
            raise serializers.ValidationError(
                "Pensja nie moze być mniejsza od zera!",
            )

##############################################################################

class KlienciSerializer(serializers.Serializer):
    idKlienta = serializers.AutoField(primary_key=True)
    imie = serializers.CharField(max_length=50)
    nazwisko = serializers.CharField(max_length=50)

    def validateImie(self):
        if (len(self.imie) > 50):
            raise serializers.ValidationError(
                "Imie jest za długie!",
            )

    def validateNazwisko(self):
        if (len(self.nazwisko) > 50):
            raise serializers.ValidationError(
                "Nazwisko jest za długie!",
            )

##############################################################################

class ListaTorowSerializer(serializers.Serializer):
    stan = serializers.CharField(max_length=45)

    def validateStan(self):
        if (len(self.stan) > 45):
            raise serializers.ValidationError(
                "Zbyt długi stan toru!",
            )

##############################################################################

class WynajemToruSerializer(serializers.Serializer):
    dataWynajecia = serializers.DateField
    czasWynajecia = serializers.CharField(max_length=40)
    cenaWynajmu = serializers.IntegerField

    def validateDataWynajecia(self):
        if (self.dataWynajecia < datetime.date.today()):
            raise serializers.ValidationError(
                "Data wynajecia toru nie może byc wczesniej niz dzien dziesiejszy!",
            )
        elif (self.dataWynajecia < datetime.date.today() + datetime.timedelta(days=30)): #nie mozna rezerwowac na pozniej niz miesiac od dzis ? jak nie to mozna wywalic
            raise serializers.ValidationError(
                "Rezerwacja na zbyt późny termin!",
            )

    def validateCzasWynajecia(self):
        if (self.czasWynajecia > 2): #nie znalazlem odpowiednij metody na godziny, narazie zostawie tak ze 1 to 1 godzina; tak wiec nie mozna wynajmowac toru na dluzej niz 2h
            raise serializers.ValidationError(
                "Nie mozna rezerwowac na dluzej niz dwie godziny!",
            )
        elif (self.czasWynajecia < 0):
            raise serializers.ValidationError(
                "Czas wynajecia musi byc dodatni!",
            )

    def validateCenaWynajmu(self):
        if (self.cenaWynajmu < 0)
            raise serializers.ValidationError(
                "Cena musi byc liczba dodatnia!",
            )

##############################################################################
