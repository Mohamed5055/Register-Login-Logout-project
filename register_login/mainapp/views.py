from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.http import HttpResponse

# Create your views here.
def index(request):
    # Nothing much here just to show the main page
    return render(request, 'index.html')

# register function
def register(request):
    # checking if the form method is post
    if request.method == 'POST':
        # getting the credentials
        username = request.POST['username']
        password = request.POST['password']
        password2 = request.POST.get('password2') # a weird error showed up in this line because in input element i typed name="password2" so i needed to type .get('password2')
        # if the user typed the password twice right
        if password == password2:
            # if the username already exists
            if User.objects.filter(username=username).exists():
                # telling the user the username already used and redirect them to registering function again
                messages.info(request, 'Username Already Used')
                return redirect('register')
            else: # if the username doesn't exist
                # create the user and saving it then redirect the user to login function
                user = User.objects.create_user(username=username, password=password)
                user.save();
                return redirect('login')
        else: # if the password is not the same
            # telling the user the password is not the same and then redirect them to login function again
            messages.info(request, 'Password not the same')
            return redirect('register')
    else:# anyways render login.html file
        return render(request, 'register.html')

#login function
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        # authenticating the user with the username and password which are entered
        user = auth.authenticate(username=username, password=password)
        if user is not None: # if the user exists
            auth.login(request, user) # login the user and redirect them to the main page
            return redirect('/')
        else: # if they don't exist
            messages.info(request, 'Credentials Invalid')# telling the user the credentials are invalid and redirect them to login function again
            return redirect('login')
    else: # anyways render login.html page
        return render(request, 'login.html')

# logout function
def logout(request):
    # logging out any logged in user and redirect them to the main page
    auth.logout(request)
    return redirect('/')

