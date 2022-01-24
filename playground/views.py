from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import NewUserForm
from django.contrib.auth import login
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm 

# Create your views here. (Request Handler/ Action/ Event)

def home_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username , password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect("playground:homepage")
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(request = request, template_name= "welcome.html", context = {"login_form": form})
    



def signup_view(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful.")
            return redirect("playground:homepage")
        messages.error(request, "Unsuccessful registration. Invalid Information." )
    form = NewUserForm()
    return render (request=request, template_name="signup.html", context={"register_form":form})
  