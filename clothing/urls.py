
from django.urls import path
from clothing.views import *
app_name ='clothing'

urlpatterns =[
    path('women/',women,name='women'),
     path('men/',men,name='men'),
]