#map urls to views

from django.urls import path
from playground import views
from django.contrib import admin

app_name = "playground"

urlpatterns =[

   # path("", views.homep, name="homepage"),
    path ('admin/', admin.site.urls),
    path('welcome/', views.home_view, name ="homepage"),
    path('signup/', views.signup_view)

]