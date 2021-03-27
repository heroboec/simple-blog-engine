from django.shortcuts import render
from django.views.generic import CreateView

from .forms import CustomUserCreationForm
from django.urls import reverse_lazy


from django.contrib.auth import get_user_model
User = get_user_model()

# Create your views here.

class SignupView(CreateView):
    model = User
    # form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'singup.html'