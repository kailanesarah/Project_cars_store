from django.contrib import admin
from cars.models import Car, Brand

class CarBrandAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)  # Corrigido para pesquisar apenas pelo campo 'name'

class CarAdmin(admin.ModelAdmin):
    list_display = ('id', 'model', 'brand', 'factory_year', 'model_year', 'value', 'photo')
    search_fields = ('model', 'brand__name')  # Adicionando a pesquisa por nome da marca se necessário

admin.site.register(Car, CarAdmin)
admin.site.register(Brand, CarBrandAdmin)
