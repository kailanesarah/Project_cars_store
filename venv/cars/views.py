from django.shortcuts import redirect, render
from cars.models import Car
from cars.forms import new_car_form
from cars.forms import register_car

#Página principal de carros
def cars_view(request):
    cars = Car.objects.all().order_by('model') #trás todos os dados do banco de dados e ordena pelo campo da tabela
    search = request.GET.get('search') #pega a chave search da URL
    
    if search:
        cars = cars.filter(model__icontains = search)
        
    return render(
        request, 
        'cars.html', 
        {'cars' : cars} #o ultimo parametro trata o que o página vai renderizar
        )

#Página para adicionar um novo carro com form
def new_car_view(request):
    
    #verificando o form
    if request.method == "POST":
        
        new_car = register_car(request.POST, request.FILES)
        
        if new_car.is_valid():
            print("Dados validados com sucesso!\n")
            new_car.save() #chamando o método para salvar os dados no BD
            return redirect('cars_list') #redirecionando para a lista de carros
            
    else:
        new_car= register_car() #criando um form vazio
    
    return render(
        request,
        'new_car.html',
        {'new_car_form_view': new_car}
        )
        
    
    