from django.shortcuts import render
from django.shortcuts import render
from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
import datetime as dt
from .models import User,Business,Neighbourhood
from django.contrib.auth.decorators import login_required
from .forms import *
from django.db import models
from django.http import Http404
from .forms import ProjectForm,ProfileForm,ReviewForm

# Create your views here.
def index(request):
    title = 'Home'
   
    return render(request, 'index.html', {'title':title})

def search_results(request):

    if 'business' in request.GET and request.GET["business"]:
        search_term = request.GET.get("business")
        searched_businesses = Business.search_by_neighbourhood(search_term)
        message = f"{search_term}"

        return render(request, 'all-news/search.html',{"message":message,"businesses": searched_businesses})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{"message":message})

def profile(request):
    current_user = request.user
    profile = Profile.objects.get(user=current_user.id)
    # print(profile.id)
    try:
        profile_details = Profile.get_by_id(profile.id)
    except:
        profile_details = Profile.filter_by_id(profile.id)
    images = Image.get_profile_images(profile.id)
    title = f'@{profile} Instagram photos and videos'

    return render(request, 'profile/profile.html', {'title':title, 'profile':profile, 'profile_details':profile_details})

