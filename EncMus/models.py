from django.db import models

# Create your models here.

class Musicos(models.Model):
    nombre=models.CharField(max_length=50)
    apellido=models.CharField(max_length=50)
    instrumento=models.CharField(max_length=50)
    email=models.EmailField()
    tel=models.CharField(max_length=50)
    edad=models.IntegerField()
    dni=models.CharField(max_length=50)

    def __str__(self):
        return f'{self.nombre} - {self.apellido} - {self.instrumento} - {self.email} - {self.tel} - {self.nombre} - {self.edad} - {self.dni}'

class Bandas(models.Model):
    nombre_ba=models.CharField(max_length=50)
    Contacto=models.CharField(max_length=50)
    email_b=models.EmailField()
   
    def __str__(self):
        return f'{self.nombre_ba} - {self.Contacto} - {self.email_b}'

class Barandpubs(models.Model):
    nombre_bar=models.CharField(max_length=50)
    Contacto_bar=models.CharField(max_length=50)
    email_bar=models.EmailField()
    tel_bar=models.CharField(max_length=50)
    Estilo_bar=models.CharField(max_length=50)
    dir_bar=models.CharField(max_length=50)
    Sonidopropio=models.BooleanField()

    def __str__(self):
        return f'{self.nombre_bar} - {self.Contacto_bar} - {self.email_bar} - {self.tel_bar} - {self.Estilo_bar} - {self.dir_bar} - {self.Sonidopropio}'

class Salasensayo(models.Model):
    nombre_sala=models.CharField(max_length=50)
    Contacto_sala=models.CharField(max_length=50)
    email_sala=models.EmailField()
    tel_sala=models.CharField(max_length=50)
    Estilo_sala=models.CharField(max_length=50)
    dir_sala=models.CharField(max_length=50)
    cantsalas=models.IntegerField()

    def __str__(self):
        return f'{self.nombre_sala} - {self.Contacto_sala} - {self.email_sala} - {self.tel_sala} - {self.Estilo_sala} - {self.dir_sala} - {self.cantsalas}'

class Productores(models.Model):
    nombre_prod=models.CharField(max_length=50)
    apellido_prod=models.CharField(max_length=50)
    email_prod=models.EmailField()
    tel_prod=models.CharField(max_length=50)
    
    def __str__(self):
        return f'{self.nombre_prod} - {self.apellido_prod} - {self.email_prod} - {self.tel_prod}'
