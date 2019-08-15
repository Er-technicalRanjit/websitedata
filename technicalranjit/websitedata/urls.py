
from django.contrib import admin
from django.urls import path
from websitedata.views import *



urlpatterns = [

    path('admin/', admin.site.urls),
    path('signup',signup),
    path('signin',login,name='signin'),
    path('logout',logout),
    path('',profile,name='profile'),
    







]



