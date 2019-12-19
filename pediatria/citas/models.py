from django.db import models

# Create your models here.

class Pediatra(models.Model):
    nombre = models.CharField(max_length=100, null=False, blank=False)
    apellido_paterno = models.CharField(max_length=100, null=False, blank=False)
    apellido_materno = models.CharField(max_length=100, null=False, blank=True)

    def __str__(self):
        return self.nombre + ' ' + self.apellido_paterno

class Paciente(models.Model):
    nombre = models.CharField(max_length=100, null=False, blank=False)
    apellido_paterno = models.CharField(max_length=100, null=False, blank=False)
    apellido_materno = models.CharField(max_length=100, null=False, blank=True)
    fecha_nacimiento = models.DateField()

    def __str__(self):
        return self.nombre + ' ' + self.apellido_paterno

class Cita(models.Model):
    fecha = models.DateField()
    hora = models.TimeField()
    comentario = models.CharField(max_length=250, null=False)
    pediatra = models.ForeignKey(Pediatra, on_delete=models.CASCADE)
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.fecha) + ' ' + str(self.hora) + '   ' + self.comentario
