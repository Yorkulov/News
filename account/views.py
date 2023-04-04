from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from django.urls import reverse_lazy
from .forms import LoginForm, UserRegistrationFrom

def userLogin(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(request, 
                                username=data['username'],
                                password=data['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse('Muvaffaqiyatli login amalga oshirildi!')
                else:
                    return HttpResponse("Sizning profilingiz faol holatda emas!")
                
            else:
                return HttpResponse('Login yoki Parol xato!')
            
    else:
        form = LoginForm()
        context = {
            "form" : form
        }
        return render(request, 'account/login.html', context)


def dashboard(request):
    user = request.user
    context = {
        "user": user
    }
    
    return render(request, "pages/dashboard.html", context)


def user_register(request):
    if request.method == "POST":
        user_form = UserRegistrationFrom(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(
                user_form.cleaned_data["password"]
            )
            new_user.save()
            context = {
                "new_user" : new_user
            }
            return render(request, 'account/register_done.html', context)
    else:
        user_form = UserRegistrationFrom()
        context = {
            "user_form" : user_form
        }
        return render(request, 'account/register.html', context)

class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('LoginView')
    template_name = "account/register.html"
