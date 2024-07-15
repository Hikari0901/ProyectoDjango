from django.contrib import admin
from django.urls import path

from vista import views

app_name='vista_urls'

urlpatterns = [
    path('paginaView/',views.PaginaView.as_view(), name='pagina_urls'),
    path('destrezaView/',views.DestrezaView.as_view()),
]
