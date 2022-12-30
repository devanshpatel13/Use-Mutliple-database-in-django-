from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('', MongoView.as_view(), name= "mongo"),
    path('login/', UserView.as_view(), name ="user_create")

]