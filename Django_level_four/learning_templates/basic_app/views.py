from django.shortcuts import render
from basic_app.forms import UserForm, UserProfileInfoForm

from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request): #for home page
    return render(request, 'basic_app/index.html')

@login_required #decorator to check if user is logged in
def special(request): #for special page
    return HttpResponse("You are logged in, Nice!") #return a response to the user


@login_required #decorator to check if user is logged in
def user_logout(request): #for logout page
    logout(request) #logout the user
    return HttpResponseRedirect(reverse('basic_app:index')) #redirect to index page

def register(request): #for registration page
    registered = False
    
    if request.method == 'POST': #check if the request is a POST request
        user_form = UserForm(data=request.POST) #bind the form to the data in the request
        profile_form = UserProfileInfoForm(data=request.POST) #bind the profile form to the data in the request

        if user_form.is_valid() and profile_form.is_valid(): #check if both forms are valid
            user = user_form.save() #save the user form to the database
            user.set_password(user.password) #hash the password
            user.save()

            profile = profile_form.save(commit=False) #don't save to db yet
            profile.user = user

            if 'profile_pic' in request.FILES: #check if there is a profile pic in the request
                profile.profile_pic = request.FILES['profile_pic'] #check if there is a profile pic in the request
            profile.save() 

            registered = True #set registered to true if both forms are valid and saved
        else: #if the forms are not valid, print the errors to the console
            print(user_form.errors, profile_form.errors)
    
    else: #if the request is not a POST request, create empty forms
        
        user_form = UserForm() #create an empty user form
        profile_form = UserProfileInfoForm()

    return render (request, 'basic_app/registration.html',{'user_form': user_form, 'profile_form': profile_form, 'registered': registered}) #render the registration template with the forms and registered status

    
def user_login(request): #for login page
    if request.method == 'POST': #check if the request is a POST request
        username = request.POST.get('username') #get the username from the request
        password = request.POST.get('password') #get the password from the request

        user = authenticate(username=username, password=password) #authenticate the user

        if user: #if the user is authenticated
            login(request, user) #login the user
            return HttpResponseRedirect(reverse('basic_app:index')) #redirect to index page
        else: #if the user is not authenticated
            print("Invalid login details: {0}, {1}".format(username, password)) #print invalid login details to console
            return render(request, 'basic_app/login.html', {}) #render the login template with empty context

    else: #if the request is not a POST request, render the login template with empty context
        return render(request, 'basic_app/login.html', {})
    

