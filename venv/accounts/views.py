from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login,logout
##Essas classes disponibilizam forms prontos do Django: UserCreationForm, AuthenticationForm
## O primeiro cria formilários próprios para cadastros e o segundo cria um form para o login do usuário 

#Registra um novo user
def register_view(request):
    
    if request.method == "POST":
        user_form = UserCreationForm(request.POST)
        
        if user_form.is_valid():
            user_form.save()
            return redirect("cars_list")
    else:
        user_form = UserCreationForm()
         
    return render(
        request,
        "register.html",
        {'user_form': user_form}
        
    )    

def login_view(request):
    
    if request.method == "POST":
       username = request.POST["username"]
       password = request.POST["password"]
       data_user = authenticate(request, username=username, password=password) 
       
       if data_user is not None:
           login(request, data_user)
           return redirect("cars_list")
       else:
           form_login = AuthenticationForm()
    
    else:
        form_login = AuthenticationForm()
        
        
    return render(
        request,
        'login.html',
        {'form_login': form_login}
    )
    
def logout_view(request):
    logout(request)
    return redirect('cars_list')
    