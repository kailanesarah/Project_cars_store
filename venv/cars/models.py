from django.db import models

class Brand(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200, blank=True)  # Utilizando blank=True em vez de null=True
    
    def __str__(self):
        return self.name

class Car(models.Model):
    id = models.AutoField(primary_key=True)
    model = models.CharField(max_length=200, blank=True)  # Utilizando blank=True em vez de null=True
    brand = models.ForeignKey(Brand, on_delete=models.PROTECT, related_name='cars')  
    factory_year = models.IntegerField(blank=True, null=True)
    model_year = models.IntegerField(blank=True, null=True)
    value = models.FloatField(blank=True, null=True)
    photo = models.ImageField(upload_to='cars/', blank=True, null=True)  # Permitir campos em branco
    
    def __str__(self):
        return self.model 
