from django.urls import path
app_name='lil'
from lil import views

urlpatterns=[
    path('',views.lil1),
    path('login/',views.login),
    path('logout/',views.logout),
    path('register/',views.register,name='register'),
    path('display/', views.display,name='display')
]