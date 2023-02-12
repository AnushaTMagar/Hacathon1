from telnetlib import LOGOUT
from pyreadline import Readline
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from .forms import RegistrationForm
from django.contrib.sessions.backends.signed_cookies import SessionStore
import os
import uuid
from django.contrib.auth import get_user_model
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import send_mail
from .models import UserManager, Admin
from django.http import JsonResponse


from .forms import RegistrationForm 
# Create your views here.

def index(request):
    return render(request, 'kitab/index.html')

def create_token(request, user):
    token = str(uuid.uuid4())
    request.session['token'] = token
    request.session.save()
    return token

def send_verification(request, user):
    current_site = Readline.get_current_history_length(request)
    token = create_token(request, user)
    email_subject = 'Activate Your Account'
    email_body = 'Please click on the following link to verify your email: ' \
                 'http://{}/verify_email/{}'.format(current_site, token)
    send_mail(email_subject, email_body, 'from@example.com', [user.email])

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            send_verification(request, user)
            return redirect('verification_sent')
    else:
        form = RegistrationForm()
    return render(request, 'kitab/register.html', {'form': form})

def verify_email(request, token):
    User = get_user_model()
    try:
        user = User.objects.get(pk=request.session['user_id'])
    except User.DoesNotExist:
        return redirect('invalid_verification')
    if user.email_verified:
        return redirect('already_verified')
    if request.session.get('token') == token:
        user.email_verified = True
        user.save()
        return redirect('email_verified')
    return redirect('invalid_verification')

def logout_view(request):
    logout(request)
    return redirect('kitab/account/html')    
