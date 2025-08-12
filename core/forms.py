from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User

# This form is used for user login, extending the AuthenticationForm
class LoginForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={
            'placeholder': 'Enter your username',
            'class': 'w-full py-4 px-6 rounded-xl border border-gray-300 shadow-sm focus:outline-none focus:ring-2 focus:ring-teal-500 focus:border-transparent transition duration-300'
        }))
    
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Enter your password',
            'class': 'w-full py-4 px-6 rounded-xl border border-gray-300 shadow-sm focus:outline-none focus:ring-2 focus:ring-teal-500 focus:border-transparent transition duration-300'
        }))


# This form is used for user signup, extending the UserCreationForm
class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
    
    username = forms.CharField(
        widget=forms.TextInput(attrs={
            'placeholder': 'Enter your username',
            'class': 'w-full py-4 px-6 rounded-xl border border-gray-300 shadow-sm focus:outline-none focus:ring-2 focus:ring-teal-500 focus:border-transparent transition duration-300'
        }))
    
    email = forms.CharField(
        widget=forms.EmailInput(attrs={
            'placeholder': 'Enter your email address',
            'class': 'w-full py-4 px-6 rounded-xl border border-gray-300 shadow-sm focus:outline-none focus:ring-2 focus:ring-teal-500 focus:border-transparent transition duration-300'
        }))
    
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Enter a secure password',
            'class': 'w-full py-4 px-6 rounded-xl border border-gray-300 shadow-sm focus:outline-none focus:ring-2 focus:ring-teal-500 focus:border-transparent transition duration-300'
        }))
    
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Confirm your password',
            'class': 'w-full py-4 px-6 rounded-xl border border-gray-300 shadow-sm focus:outline-none focus:ring-2 focus:ring-teal-500 focus:border-transparent transition duration-300'
        }))
