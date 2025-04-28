from django.urls import path
from .views import *

urlpatterns = [
    path('person_detail/<int:person_id>/', person_detail, name='person_detail'),
    path('', person_list, name='people'),
]
