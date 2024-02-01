from django.db import models


class Educacion(models.Model):
    instituto = models.CharField(max_length=100)
    titulo = models.CharField(max_length=100)
    anio = models.IntegerField()
    descripcion = models.TextField(blank=True, null=True)
    imagen = models.ImageField(upload_to='educacion_images/', blank=True, null=True)
    creado_en = models.DateTimeField(auto_now_add=True)
    modificado_en = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.titulo

class Experiencia(models.Model):
    empresa = models.CharField(max_length=100)
    cargo = models.CharField(max_length=100)
    mes_ingreso = models.CharField(max_length=10)
    anio_ingreso = models.IntegerField()
    mes_egreso = models.CharField(max_length=10)
    anio_egreso = models.IntegerField()
    descripcion = models.TextField()
    creado_en = models.DateTimeField(auto_now_add=True)
    modificado_en = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.cargo
class Proyectos(models.Model):
    nombre_proyecto = models.CharField(max_length=100)
    descripcion = models.TextField()
    enlace_url = models.URLField()
    imagen = models.ImageField(upload_to='proyectos_images/', blank=True, null=True)
    creado_en = models.DateTimeField(auto_now_add=True)
    modificado_en = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre_proyecto

class AcercaDe(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    cargo = models.CharField(max_length=100)
    descripcion = models.TextField()
    creado_en = models.DateTimeField(auto_now_add=True)
    modificado_en = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre