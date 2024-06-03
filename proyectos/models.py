from django.contrib.auth.models import User
from django.db import models

class Estudiante(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    matricula = models.CharField(max_length=20)

    def __str__(self):
        return self.user.username

class Profesor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    especialidad = models.CharField(max_length=100)

    def __str__(self):
        return self.user.username

class Proyecto(models.Model):
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE)
    patrocinado = models.BooleanField(default=False)
    profesor = models.ForeignKey(Profesor, null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.titulo
