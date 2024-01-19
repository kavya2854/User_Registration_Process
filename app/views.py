from django.shortcuts import render
from app.forms import *
# Create your views here.
def Registration(request):
    UFO = UserForm()
    PFO = ProfileForm()
    d = {'user':UFO, 'profile':PFO}
    return render(request,'Registration.html',d)