from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Profile, Image
from .forms import ProfileForm
from django.http import HttpResponseRedirect, Http404
from django.urls import reverse
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.
@login_required(login_url='/accounts/login/')
def index(request):
    """
    view function renders the landing page
    """
    return render(request, 'profile_templates/index.html')



@login_required(login_url='/accounts/login/')
def new_profile(request):
    """
    view function renders form for creating new profile
    """
    current_user = request.user
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = current_user
            profile.save()
        return redirect('profiles:user_profile')
    else:
        form = ProfileForm()
    return render(request, 'profile_templates/new_profile.html', {"form":form})

@login_required(login_url='/accounts/login/')
def user_profile(request, profile_id):
    """
    view function renders profile page
    """
    try:
        profile = Profile.get_profile_by_id(id=profile_id)
    except ObjectDoesNotExist:
        raise Http404()
    return render(request, 'profile_templates/profile.html', {'profile':profile})
