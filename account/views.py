from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView, View
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import LoginForm, UserRegistrationFrom, UserEditForm, ProfileEditForm
from account.models import Profile

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
        return render(request, 'registration/login.html', context)




def user_register(request):
    if request.method == "POST":
        user_form = UserRegistrationFrom(request.POST) 
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(
                user_form.cleaned_data["password"]
            )
            new_user.save()
            Profile.objects.create(user=new_user)
            context = {
                "new_user" : new_user,
            }
            return render(request, 'account/register_done.html', context)
    else:
        user_form = UserRegistrationFrom()
        context = {
            "user_form" : user_form,
        }
        return render(request, 'account/register.html', context)

class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('LoginView')
    template_name = "account/register.html"

@login_required # login qilmagan anonim foydalanuvchilar uchun user sahifalariga kirishni cheklash
def edit_user(request):
    if request.method == "POST":
        user_form = UserEditForm(instance=request.user, data=request.POST)
        profile_form = ProfileEditForm(instance=request.user.profile, 
                                       data=request.POST,
                                       files=request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect('LoginView')
            

    else:
        user_form=UserEditForm(instance=request.user)
        profile_form=ProfileEditForm(instance=request.user.profile)

    return render(request, 'account/profile_edit.html', {"user_form": user_form, "profile_form": profile_form})


class EditUserView(LoginRequiredMixin, View):
    
    def get(self, request):
        user_form=UserEditForm(instance=request.user)
        profile_form=ProfileEditForm(instance=request.user.profile)

        return render(request, 'account/profile_edit.html', {"user_form": user_form, "profile_form": profile_form})

    def post(self, request):
        user_form = UserEditForm(instance=request.user, data=request.POST)
        profile_form = ProfileEditForm(instance=request.user.profile, 
                                       data=request.POST,
                                       files=request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect('LoginView')
        


def dashboard(request):
    user = request.user
    profile = Profile.objects.get(user = request.user)
    context = {
        "user": user,
        "profile": profile
    }
    
    return render(request, "pages/dashboard.html", context)