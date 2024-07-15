from django.db import models

# Create your models here.

class Destrezas(models.Model):
    destreza = models.CharField('destreza', max_length=50)
    def __str__(self):
        return self.destreza
    
    class Meta:
        verbose_name_plural = 'Destrezas'
        verbose_name= 'Destreza'
    

class Pagina(models.Model):
    nombre = models.CharField('nombre', max_length=50)
    nombresC= models.CharField('nombresC', max_length=50)
    cargo = models.CharField('cargo', max_length=50)
    edad = models.CharField('edad', max_length=50)
    destrezas = models.ManyToManyField(Destrezas)
    def __str__(self):
        return f'{self.nombre} {self.cargo}' 
    
    
    class Meta:
        verbose_name_plural='Vista Paginas'
        verbose_name='Vista Pagina'
        
    
        
    