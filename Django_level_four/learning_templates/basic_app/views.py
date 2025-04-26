from django.shortcuts import render
from basic_app.forms import UserForm, UserProfileInfoForm

# Create your views here.
def index(request): #for home page
    return render(request, 'basic_app/index.html')

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

    


