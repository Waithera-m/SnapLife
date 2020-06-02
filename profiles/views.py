from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Profile, Image, Comments, Like
from .forms import ProfileForm, ImageForm, CommentsForm
from django.http import HttpResponseRedirect, Http404, HttpResponse
from django.urls import reverse
from django.core.exceptions import ObjectDoesNotExist
from django.views import generic

# Create your views here.
@login_required(login_url='/accounts/login/')
def index(request):
    """
    view function renders the landing page
    """
    profiles = Profile.objects.all()
    images = Image.objects.all()
    comments = Comments.objects.all()
    return render(request, 'profile_templates/index.html', {'profiles':profiles, 'images':images, 'comments':comments})

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
                return redirect('profiles:user_profile', profile_id=profile.id)
            else:
                form = ImageForm()
    return render(request, 'profile_templates/upload_image.html', {'form':form, 'profiles':profiles})

@login_required(login_url='/accounts/login/')
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

@login_required(login_url='/accounts/login/')
def all_images(request, profile_id):
    """
    function gets and displays all images uploaded by a user
    """
    current_user = request.user.profile
    user = current_user
    images = Image.objects.filter(profile_id=profile_id)
    return render(request, 'profile_templates/user_posts.html', {'images':images})

@login_required(login_url='/accounts/login/')
def comment(request, image_id):
    """
    view function allows users to comment and like a post
    """
    image = get_object_or_404(Image, id=image_id)
    current_user = request.user
    if request.method == 'POST':
        form = CommentsForm(request.POST, request.FILES)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = current_user
            comment.image = image
            comment.save()
        return redirect('profiles:index')
    else:
        form = CommentsForm
    return render(request, 'profile_templates/new_comment.html', {"form":form, "image_id":image_id})

@login_required(login_url='/accounts/login/')
def like_image(request, image_id):
    """
    view function allows users to like images
    """
    try:
        image = get_object_or_404(Image, id=image_id)

        obj, created = Like.objects.get_or_create(image=image, user=request.user)
    except ObjectDoesNotExist:
        raise Http404()
        raise False
    
    return redirect('profiles:index')



