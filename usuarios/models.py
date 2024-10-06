from django.db import models

# Create your models here.
# Los atributos se convierte en una tabla en la base de datos

class Usuario(models.Model):
    genero_eleccion = (
        ('M', 'Masculino'),
        ('F', 'Femenino'),
    )
    
    codigo = models.IntegerField()
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/')    # Le pasamos al ubicación el directorio donde queremos que se almacenen las photos y se almacena dentro de una estructura de dia año y mes
    nombre = models.CharField(max_length=100)
    profesion = models.CharField(max_length=100)
    genero = models.CharField(choices=genero_eleccion, max_length=100)
    ciudad = models.CharField(max_length=100)
    
    def __str__(self):
        return self.nombre