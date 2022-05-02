from django.db import models

# Create your models here.
class Campo(models.Model):
    nome = models.CharField('Nome', max_length=60)
    latitude = models.FloatField('Latitude', max_length=25)
    longitude = models.FloatField('Longitude', max_length=25)
    data_expiracao = models.DateField('Data de expiração')

    def __str__(self):
        return self.nome