from django.urls import path

from api import views

app_name='api'


urlpatterns=[
    path('student_list/',views.student_list),
    path('snippets/<int:pk>/',views.snippet_detail),
]