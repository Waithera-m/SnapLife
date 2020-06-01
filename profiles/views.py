from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Profile, Image, Comments
from .forms import ProfileForm, ImageForm
from django.http import HttpResponseRedirect, Http404
from django.urls import reverse
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.
@login_required(login_url='/accounts/login/')
def index(request):
    """
    view function renders the landing page
    """
    profiles = Profile.objects.all()
    return render(request, 'profile_templates/index.html', {'profiles':profiles})



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
        return redirect('profiles:index')
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
        print(profile)
    except ObjectDoesNotExist:
        raise Http404()
        raise False
    return render(request, 'profile_templates/profile.html', {'profile':profile})

@login_required(login_url='/accounts/login/')
def upload_image(request):
    """
    view functon displays the upload image form
    """
    profiles = Profile.objects.all()
    current_user = request.user.profile
    for profile in profiles:
        if profile.user.id == request.user.id:
            if request.method == 'POST':
                form = ImageForm(request.POST, request.FILES)
                if form.is_valid():
                    image = form.save(commit=False)
                    image.profile = current_user
                    image.save()
                return redirect('profiles:user_profile', id=profile.id)
            else:
                form = ImageForm()
    return render(request, 'profile_templates/upload_image.html', {'form':form})

def search_by_username(request):
    """
    view function renders template that shows results associated with a given search term
    """
    if 'profile' in request.GET and request.GET['profile']:
        name = request.GET.get("profile")
        profiles = Profile.get_by_name(name)
        message = f'{name}'
        return render(request, 'profile_templates/results.html', {"message":message, "profiles":profiles})
    
    else:
        message = "please enter a search term"
        return render(request, 'profile_templates/results.html', {"message":message})