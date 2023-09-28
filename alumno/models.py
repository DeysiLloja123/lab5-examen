from django.db import models

class Alumno(models.Model):
    idAlumno = models.AutoField(primary_key=True, auto_created=True)
    nombres=models.CharField(max_length=100)
    apellidos=models.CharField(max_length=50)
    email=models.EmailField()
    dni=models.IntegerField()

    def __str__(self):
        return f"{self.nombres} {self.apellidos}"