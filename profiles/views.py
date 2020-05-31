from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='/accounts/login/')
def index(request):
    """
    view function renders the landing page
    """
    return render(request, 'profile_templates/index.html')

def login(request):
    """
    view function renders the template that contains the login form
    """
    return render(request, 'registration/login.html')
