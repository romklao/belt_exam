from django.shortcuts import render, redirect
from .models import User, Item
from django.contrib import messages

# Create your views here.
import bcrypt
import md5
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

def index(request):
    
    return render(request, 'index.html')

def dashboard(request):
    context = {
        "items": Item.objects.all()
    }
    return render(request, 'dashboard.html', context)

def logout_dashboard(request):

    return redirect('/')

def add_item(request):

    return render(request, 'wish_items_created.html')

def submit_add_item(request):

    return redirect('/dashboard')

def login(request):
    user = User.objects.get(username=request.POST['username'])
    pw_hash = bcrypt.hashpw(request.POST['password'].encode(), user.password.encode())

    if pw_hash == user.password:
        request.session['userloggedin'] = user.username
        return redirect('/dashboard')

    else:
        messages.add_message(request, messages.INFO, 'Incorrect password')
        return redirect('/')

def register(request):

    valid = True
    
    if len(request.POST['name']) < 3:
        messages.add_message(request, messages.INFO, 'First name can not be less than 3 characters!')
        valid = False

    if len(request.POST['username']) < 3:
        messages.add_message(request, messages.INFO, 'username can not be less than 3 characters!')
        valid = False

    if len(request.POST['password']) < 1:
        messages.add_message(request, messages.INFO, 'Password must be more than 1 character!')
        valid = False

    if request.POST['password'] != request.POST['confirm_password']:
        messages.add_message(request, messages.INFO, 'Password and confirmation password do not match!')
        valid = False

    if valid:
        pw_hash = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt())
        user = User.objects.create(
            name=request.POST['name'], 
            username=request.POST['username'],
            password=pw_hash
        )
        print "hi"
        request.session['userloggedin'] = user.id
        return redirect('/dashboard')
    return redirect('/')
