
from django.views.generic import ListView, TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from cars.models import Car
from cars.forms import register_car
from django.urls import reverse_lazy 




class ConfirmTemplate(TemplateView):
    template_name = "sucesso.html"
    
    
    
class ListCars(ListView):
    model= Car
    template_name = "cars.html"
    context_object_name = "cars"
    
    def get_queryset(self):
        cars = super().get_queryset().order_by('model') #acessa a classe pai e chama o método queryset e ordena
        search = self.request.GET.get('search') #pega os dados do campo pesquisa e armazena na variável
        
        if search:
            cars= cars.filter(model__icontains=search)
        
        return cars
    

class RegisterCars(CreateView):
    model = Car
    template_name = "new_car.html"
    form_class = register_car
    success_url = reverse_lazy('confirm') #name da url
  

class DetailCar(DetailView):
    model = Car
    template_name = "car_detail.html"
    
    

class UpdateCar(UpdateView):
    model = Car
    template_name = "car_update.html"
    form_class = register_car
    success_url = "cars"
    
    def get_success_url(self):
        return reverse_lazy('car_detail', kwargs={'pk': self.object.pk}) #URL personalizada com parametro
    
    
class DeleteCar(DeleteView):
    model = Car
    template_name = "car_delete.html"
    success_url = reverse_lazy('cars') #name da url
    

    





