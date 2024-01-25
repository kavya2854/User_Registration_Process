from django.shortcuts import render
from app.forms import *
from django.http import HttpResponse,HttpResponseRedirect
from django.core.mail import send_mail
from django.urls import reverse
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from app.models import *
# Create your views here.
def Registration(request):
    UFO = UserForm()
    PFO = ProfileForm()
    d = {'user':UFO, 'profile':PFO}

    if request.method == 'POST' and request.FILES:
        UFD = UserForm(request.POST)
        PFD = ProfileForm(request.POST,request.FILES)
        if UFD.is_valid() and PFD.is_valid():
            MUFDO = UFD.save(commit = False)
            pw = UFD.cleaned_data['password']
            MUFDO.set_password(pw)
            MUFDO.save()
            MPFDO = PFD.save(commit = False)
            MPFDO.username = MUFDO
            MPFDO.save()
            send_mail('REGISTRATION','Thank you for registring',
            'gotlurukavya@gmail.com',
            [MUFDO.email],
            fail_silently = True)
            return HttpResponse('Registration is Successfully Completed....')
        else:
            return HttpResponse('Invalid Data')
    return render(request,'Registration.html',d)

def home(request):
    if request.session.get('username'):
        un = request.session.get('username')
        d ={'username':un}
        return render(request,'home.html',d)
    return render(request,'home.html')


def user_login(request):
    if request.method == 'POST':
        un = request.POST['un']
        pw = request.POST['pw']
        AUO = authenticate(username = un, password = pw)
        if AUO and AUO.is_active:
            login(request, AUO)
            request.session['username'] = un
            return HttpResponseRedirect(reverse('home'))
        else:
            return HttpResponse('Invalid Crenditials')
        
    return render(request,'user_login.html')

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('home'))

@login_required  
def display_profile(request):
    un = request.session.get('username') 
    UO = User.objects.get(username = un)
    PO = Profile.objects.get(username = UO)
    d = {'user':UO, 'profile':PO}
    return render(request,'display_profile.html',d)
