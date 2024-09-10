from django.db import models

class cars(models.Model):
    id = models.AutoField(primary_key= True)
    model = models.CharField(max_length=200, null=True)
    brand = models.CharField(max_length=200, null=True)
    factory_year = models.IntegerField(null=True)
    model_year = models.IntegerField(null = True)
    value = models.FloatField(null=True)
