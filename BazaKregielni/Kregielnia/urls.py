from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from BazaKregielni.Kregielnia import views

urlpatterns = [
    path('pracownicy/', views.PracownicyList.as_view()),
    path('pracownicy/<int:pk>', views.PracownicyDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)