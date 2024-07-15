from django.shortcuts import render
from django.views.generic import (
    TemplateView,
    ListView,
)

from .models import Pagina, Destrezas
# Create your views here.

class DestrezaView(ListView):
    model=Destrezas
    template_name='destrezas.html'
    context_object_name='destrezas'
    
    
    def get_context_data(self, **kwargs):
        context = super(DestrezaView, self).get_context_data(**kwargs)
        context["destreza"] = Destrezas.objects.all()
        return context
    

class PaginaView(TemplateView):
    template_name = 'inicio.html'
    model = Pagina
    
    def get_context_data(self, **kwargs):
        context = super(PaginaView, self).get_context_data(**kwargs)
        context["paginas"] = Pagina.objects.all()
        return context
