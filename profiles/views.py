from django.shortcuts import render

# Create your views here.
def index(request):
    """
    view function renders the landing page
    """
    return render(request, 'profile_templates/index.html')