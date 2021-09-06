from django.conf.urls import url
from django.urls import path

from main import views

app_name = 'encrypting'

urlpatterns = [
    url('$', views.index, name='encrypting'),
]