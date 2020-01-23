from django.contrib import admin

from .models import wynajemToru, Pensje, listaTorow, Klienci, Pracownicy, Pensje

admin.site.register(Pracownicy)
admin.site.register(Pensje)
admin.site.register(Klienci)
admin.site.register(listaTorow)
admin.site.register(wynajemToru)