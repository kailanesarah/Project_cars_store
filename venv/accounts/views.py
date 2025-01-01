from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.views import LoginView
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect
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

class loginView(LoginView):
    template_name = 'login.html'  # Nome do template personalizado
   
    
    def form_valid(self, form):
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        
        user = authenticate(username=username, password=password)
        
        if user is not None:
            login(self.request, user)
            print(f"Usuário autenticado {username}")
            return redirect('cars')
        else:
            return self.form_invalid(form)

    
def logout_view(request):
    logout(request)
    return redirect('cars')
    