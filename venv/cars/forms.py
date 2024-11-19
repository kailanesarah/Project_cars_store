#Declarando um novo modelo de formulário para o django

from django import forms
from cars.models import Brand, Car

#Novo formulário que coleta dados dos carros e salva no banco de dados.
class new_car_form(forms.Form): 
    model = forms.CharField(max_length=200)
    brand = forms.ModelChoiceField(Brand.objects.all())
    factory_year = forms.IntegerField()
    model_year = forms.IntegerField()
    value = forms.FloatField()
    photo = forms.ImageField()
    
    def save_car (self):
        car = Car( #Instanciando um obj do model Cars
            model = self.cleaned_data['model'],
            brand = self.cleaned_data['brand'],
            factory_year = self.cleaned_data['factory_year'],
            model_year = self.cleaned_data['model_year'],
            value = self.cleaned_data['value'],
            photo = self.cleaned_data['photo'],
            
        )
        car.save() #salvando os dados do form no banco
        return car

class register_car(forms.ModelForm):
    
    class Meta:
        model = Car 
        fields = '__all__'
        
        
    def clean_year(self):
        factory_year = self.cleaned_data.get('factory_year')
        model_year = self.cleaned_data.get('model_year')
        
        if factory_year < 2005 and model_year < 2005:
            self.add_error('Não permitimos carros com \n Model year:'
                           + model_year + "\nFactory year:" + factory_year)
            
        return factory_year, model_year
            
        