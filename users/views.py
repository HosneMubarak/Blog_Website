from django.shortcuts import render
from django.views.generic import *
from .forms import CustomUserCreationForm
from .models import CustomUser
from django.urls import reverse_lazy


class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'signup.html'
    success_url = reverse_lazy('login')
