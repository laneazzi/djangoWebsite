from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import NewUserForm
from django.contrib.auth import login
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm 

# Create your views here. (Request Handler/ Action/ Event)


#function to login with authentication. Also doubles as landing page

def home_view(request):
    if request.method == "POST": #check if form was posted
        form = AuthenticationForm(request, data=request.POST) #uses pre-built django Authentication form.
        if form.is_valid(): 
            username = form.cleaned_data.get('username') #stores username as dictionary with user input as value 
            password = form.cleaned_data.get('password') #same as above
            user = authenticate(username=username  , password=password) # django user authentication method
            if user is not None: # if the user was authenticated.
                login(request, user) #keeps  user logged in throughout session.
                messages.info(request, f"You are now logged in as {username}.")
                return redirect("playground:homepage")
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(request = request, template_name= "welcome.html", context = {"login_form": form}) # context enables use of crispy forms (less HTML writing)
    


#function to signup with authentication
def signup_view(request):
    if request.method == "POST":
        form = NewUserForm(request.POST) #variable of prebuilt django NewUserForm
        if form.is_valid(): # checks if form data is valid.
            user = form.save()
            login(request, user) 
            messages.success(request, "Registration successful.")
            return redirect("playground:homepage")
        messages.error(request, "Unsuccessful registration. Invalid Information." )
    form = NewUserForm()
    return render (request=request, template_name="signup.html", context={"register_form":form})
  