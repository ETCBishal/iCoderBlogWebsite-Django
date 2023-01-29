from django.urls import path
from Home import views

urlpatterns = [
    path('',views.index,name="index"),
    path('about/',views.about,name="about"),
    path('contact/',views.contact,name="contact"),
    path('search/',views.search,name="search"),
    path('signup/',views.userSignup,name="userSignup"),
    path('login/',views.userLogin,name="userLogin"),
    path('logout/',views.logoutUser,name="logoutUser"),
]