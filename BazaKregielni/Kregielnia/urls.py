from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import *

urlpatterns = [
    path('pracownicy/', PracownicyList.as_view()),
    path('pracownicy/<int:pk>/', PracownicyDetail.as_view()),

    path('klienci/', KlienciList.as_view()),
    path('klienci/<int:pk>/', KlienciDetail.as_view()),

    path('pensje/', PensjeList.as_view()),
    path('pensje/<int:pk>/', PensjeDetail.as_view()),

    path('tor/', listaTorowList.as_view()),
    path('listatorow/<int:pk>/', listaTorowDetail.as_view()),

    path('wynajemtoru/', wynajemToruList.as_view()),
    path('wynajemtoru/<int:pk>/', wynajemToruDetail.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)