from cProfile import Profile

from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.contrib.auth import authenticate, login, logout
from django.views.generic import UpdateView

from .forms import RegisterForm, LoginForm, UpdateProfileForm


def register_user(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            return HttpResponseRedirect(reverse('users:login'))
    form = RegisterForm()

    data = {
        'form': form,
    }
    return render(request, 'users/register.html', context=data)


def login_user(request):
    if request.method == "POST":
        user = authenticate(username=request.POST['username'], password=request.POST['password'])
        if user is not None and user.is_active:
            login(request, user)
            return HttpResponseRedirect(reverse('home'))
    form = LoginForm()

    return render(request, 'users/login.html', context={'form':form})

def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse('home'))

class ProfileUpdate(UpdateView):
    model = User
    form_class = UpdateProfileForm
    template_name = 'myapp/profile.html'

    def get_success_url(self):
        return reverse_lazy('home')

    def get_object(self):
        return self.request.user