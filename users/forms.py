from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User



class RegisterForm(forms.ModelForm):
    username = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'Username', 'class': 'form-control'}))
    password = forms.CharField(label='', widget=forms.PasswordInput(attrs={'placeholder': 'Password', 'class': 'form-control'}))
    password2 = forms.CharField(label='', widget=forms.PasswordInput(attrs={'placeholder': 'Repeat Password', 'class': 'form-control'}))
    email = forms.EmailField(label='', widget=forms.TextInput(attrs={'placeholder': 'Email', 'class': 'form-control'}))
    first_name = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'First name', 'class': 'form-control'}))
    last_name = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'Last name', 'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'password', 'password2', 'email']

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError("Parollar bir xil bo'lishi zarur")
        return cd['password']

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('Bunday Email bazada mavjud!!!')

        return email

class LoginForm(forms.ModelForm):
    username = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'Username', 'class': 'form-control'}))
    password = forms.CharField(label='', widget=forms.PasswordInput(attrs={'placeholder': 'Password', 'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['username', 'password']

class UpdateProfileForm(forms.ModelForm):
    username = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'Username', 'class': 'form-control'}))
    email = forms.EmailField(disabled=True, label='', widget=forms.TextInput(attrs={'placeholder': 'Email', 'class': 'form-control'}))
    first_name = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'First name', 'class': 'form-control'}))
    last_name = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'Last name', 'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']






