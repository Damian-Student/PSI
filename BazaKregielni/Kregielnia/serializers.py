from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User

###################################### PRACOWNICY ########################################
class PracownicySerializer(serializers.Serializer):
    imie = serializers.CharField(max_length=50)
    nazwisko = serializers.CharField(max_length=50)
    stanowisko = serializers.CharField(max_length=50)
#-------------------------- validate ----------------------------
    def validateImie(self, imie):
        if (len(imie) > 50):
            raise serializers.ValidationError(
                "Imie jest za długie!",
            )

    def validateNazwisko(self, nazwisko):
        if (len(nazwisko) > 50):
            raise serializers.ValidationError(
                "Nazwisko jest za długie!",
            )

    def validateStanowisko(self, stanowisko):
        if (len(stanowisko) > 50):
            raise serializers.ValidationError(
                "Nazwa stanowiska jest za długa!",
            )
#-------------------------- create / update ----------------------------
    def create(self, validated_data):
        return Pracownicy(**validated_data)

    def update(self, instance, validated_data):
        instance.imie = validated_data.get('imie', instance.imie)
        instance.nazwisko = validated_data.get('nazwisko', instance.nazwisko)
        instance.stanowisko = validated_data.get('stanowisko', instance.stanowisko)
        instance.save()
        return instance
######################################## PENSJE ######################################
class PensjeSerializer(serializers.Serializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    pensja = serializers.IntegerField

    def validatePensja(self, pensja):
        if (pensja < 0):
            raise serializers.ValidationError(
                "Pensja nie moze być mniejsza od zera!",
            )
#-------------------------- create / update ----------------------------
    def create(self, validated_data):
        return Pensje(**validated_data)

    def update(self, instance, validated_data):
        instance.pensja = validated_data.get('pensja', instance.pensja)
        instance.save()
        return instance
####################################### KLIENCI #######################################
class KlienciSerializer(serializers.Serializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    imie = serializers.CharField(max_length=50)
    nazwisko = serializers.CharField(max_length=50)
# -------------------------- validate ----------------------------
    def validateImie(self, imie):
        if (len(imie) > 50):
            raise serializers.ValidationError(
                "Imie jest za długie!",
            )

    def validateNazwisko(self, nazwisko):
        if (len(nazwisko) > 50):
            raise serializers.ValidationError(
                "Nazwisko jest za długie!",
            )
#-------------------------- create / update ----------------------------
    def create(self, validated_data):
        return Klienci(**validated_data)

    def update(self, instance, validated_data):
        instance.imie = validated_data.get('imie', instance.imie)
        instance.nazwisko = validated_data.get('nazwisko', instance.nazwisko)
        instance.save()
        return instance
###################################### LISTA TORÓW ########################################
class ListaTorowSerializer(serializers.Serializer):
    stan = serializers.CharField(max_length=45)
# -------------------------- validate ----------------------------
    def validateStan(self, stan):
        if (len(stan) > 45):
            raise serializers.ValidationError(
                "Zbyt długi stan toru!",
            )
#-------------------------- create / update ----------------------------
    def create(self, validated_data):
        return listaTorow(**validated_data)

    def update(self, instance, validated_data):
        instance.stan = validated_data.get('stan', instance.stan)
        instance.save()
        return instance
###################################### WYNAJEM TORU ########################################
class WynajemToruSerializer(serializers.Serializer):
    dataWynajecia = serializers.CharField(max_length=100, default="1.01.1970")
    czasWynajecia = serializers.CharField(max_length=40)
    cenaWynajmu = serializers.IntegerField
# -------------------------- validate ----------------------------
    def validateCzasWynajecia(self, czasWynajecia):
        if (czasWynajecia > 4): #nie znalazlem odpowiednij metody na godziny, narazie zostawie tak ze 1 to 1 godzina; tak wiec nie mozna wynajmowac toru na dluzej niz 4h
            raise serializers.ValidationError(
                "Nie mozna rezerwowac na dluzej niz cztery godziny!",
            )
        elif (czasWynajecia < 0):
            raise serializers.ValidationError(
                "Czas wynajecia musi byc dodatni!",
            )

    def validateCenaWynajmu(self, cenaWynajmu):
        if (cenaWynajmu < 0):
            raise serializers.ValidationError(
                "Cena musi byc liczba dodatnia!",
            )
#-------------------------- create / update ----------------------------
    def create(self, validated_data):
        return wynajemToru(**validated_data)

    def update(self, instance, validated_data):
        instance.dataWynajecia = validated_data.get('dataWynajecia', instance.dataWynajecia)
        instance.czasWynajecia = validated_data.get('czasWynajecia', instance.czasWynajecia)
        instance.cenaWynajmu = validated_data.get('cenaWynajmu', instance.cenaWynajmu)
        instance.save()
        return instance
##############################################################################


class UserSerializer(serializers.ModelSerializer):
    Pensje = serializers.PrimaryKeyRelatedField(many=True, queryset=Pensje.objects.all())
    Klienci = serializers.PrimaryKeyRelatedField(many=True, queryset=Klienci.objects.all())
    class Meta:
        model = User
        fields = ['id','username', 'Pensje', 'Klienci']