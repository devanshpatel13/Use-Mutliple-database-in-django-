from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [

    path("postgres/", PostgresView.as_view(), name="postgres"),
    path("postgresupdatedelete/<int:pk>/", PostgresUpdateDeleteView.as_view(), name = "postgresupdatedelete"),


]