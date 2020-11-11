from django.urls import path
from . import views         #. means from current directory

urlpatterns = [
    path('',views.index,name='index')
]