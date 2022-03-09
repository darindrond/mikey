from django.urls import path

from robert import views

urlpatterns =[
    path('',views.led),
    path('login/',views.login),
    path('logout/',views.logout),

]