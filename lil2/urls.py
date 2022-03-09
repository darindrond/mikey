from django.contrib import admin
from django.urls import path
from. import views

urlpatterns=[
    path('',views.lil2),
    path('getin/',views.getin),
    path('getout/',views.getout),

]