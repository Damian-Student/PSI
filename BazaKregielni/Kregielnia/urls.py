from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import *
from . import views

urlpatterns = [
    path('pracownicy/', views.PracownicyList.as_view()),
    path('pracownicy/<int:pk>/', views.PracownicyDetail.as_view()),

    path('klienci/', views.KlienciList.as_view()),
    path('klienci/<int:pk>/', views.KlienciDetail.as_view()),

    path('pensje/', views.PensjeList.as_view()),
    path('pensje/<int:pk>/', views.PensjeDetail.as_view()),

    path('tor/', views.listaTorowList.as_view()),
    path('listatorow/<int:pk>/', views.listaTorowDetail.as_view()),

    path('wynajemtoru/', views.wynajemToruList.as_view()),
    path('wynajemtoru/<int:pk>/', views.wynajemToruDetail.as_view()),

    path('users/', views.UserList.as_view()),
    path('users/<int:pk>/', views.UserDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)