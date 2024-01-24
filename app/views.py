from django.shortcuts import render
from app.forms import *
from django.http import HttpResponse
from django.core.mail import send_mail
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