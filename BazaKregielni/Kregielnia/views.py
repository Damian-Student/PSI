from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from rest_framework import permissions

#import klas i serializerow
from .models import Pracownicy
from .serializers import PracownicySerializer

from .models import Klienci
from .serializers import KlienciSerializer

from .models import wynajemToru
from .serializers import WynajemToruSerializer

from .models import listaTorow
from .serializers import ListaTorowSerializer

from .models import Pensje
from .serializers import PensjeSerializer

from django.contrib.auth.models import User
from .serializers import UserSerializer

##################################### PRACOWNICY #####################################
class PracownicyList(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get(self, request, format=None):
        pracownicy = Pracownicy.objects.all()
        serializer = PracownicySerializer(pracownicy, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = PracownicySerializer(data=request.user)
        if serializer.is_valid():
            serializer.save(owner=self.request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PracownicyDetail(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_object(self, pk):
        try:
            return Pracownicy.objects.get(pk=pk)
        except Pracownicy.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        pracownicy = self.get_object(pk)
        serializer = PracownicySerializer(pracownicy)
        return Response(serializer.data)

    def put (self, request, pk, format=None):
        pracownicy = self.get_object(pk)
        serializer = PracownicySerializer(pracownicy, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        pracownicy=self.get_object(pk)
        pracownicy.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

##################################### KLIENCI #####################################
class KlienciList(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          permissions.DjangoModelPermissionsOrAnonReadOnly]
    queryset = Klienci.objects.all()
    serializer_class = KlienciSerializer


    def get(self, request, format=None):
        serializer = KlienciSerializer
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = KlienciSerializer(data=request.user)
        if serializer.is_valid():
            serializer.save(owner=self.request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class KlienciDetail(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_object(self, pk):
        try:
            return Klienci.objects.get(pk=pk)
        except Klienci.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        klienci = self.get_object(pk)
        serializer = KlienciSerializer(klienci)
        return Response(serializer.data)

    def put (self, request, pk, format=None):
        klienci = self.get_object(pk)
        serializer = KlienciSerializer(klienci, data=request.data)
        if (serializer.is_valid()):
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        klienci=self.get_object(pk)
        klienci.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

##################################### WYNAJEM TORU #####################################
class wynajemToruList(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get(self, request, format=None):
        wynajem = wynajemToru.objects.all()
        serializer = PracownicySerializer(wynajem, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = WynajemToruSerializer(data=request.user)
        if serializer.is_valid():
            serializer.save(owner=self.request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class wynajemToruDetail(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_object(self, pk):
        try:
            return wynajemToru.objects.get(pk=pk)
        except wynajemToru.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        wynajem = self.get_object(pk)
        serializer = WynajemToruSerializer(wynajem)
        return Response(serializer.data)

    def put (self, request, pk, format=None):
        wynajem = self.get_object(pk)
        serializer = WynajemToruSerializer(wynajem, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        wynajem=self.get_object(pk)
        wynajem.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

##################################### LISTA TOROW // TOR#####################################
class listaTorowList(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get(self, request, format=None):
        tor = listaTorow.objects.all()
        serializer = ListaTorowSerializer(tor, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ListaTorowSerializer(data=request.user)
        if serializer.is_valid():
            serializer.save(owner=self.request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class listaTorowDetail(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_object(self, pk):
        try:
            return listaTorow.objects.get(pk=pk)
        except listaTorow.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        tor = self.get_object(pk)
        serializer = ListaTorowSerializer(tor)
        return Response(serializer.data)

    def put (self, request, pk, format=None):
        tor = self.get_object(pk)
        serializer = ListaTorowSerializer(tor, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        tor=self.get_object(pk)
        tor.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

##################################### PENSJE #####################################
class PensjeList(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get(self, request, format=None):
        pensja = Pensje.objects.all()
        serializer = PensjeSerializer(pensja, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = PensjeSerializer(data=request.user)
        if serializer.is_valid():
            serializer.save(owner=self.request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PensjeDetail(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_object(self, pk):
        try:
            return Pensje.objects.get(pk=pk)
        except Pensje.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        pensja = self.get_object(pk)
        serializer = PensjeSerializer(pensja)
        return Response(serializer.data)

    def put (self, request, pk, format=None):
        pensja = self.get_object(pk)
        serializer = PensjeSerializer(pensja, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        pensja=self.get_object(pk)
        pensja.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer