from django.urls import path
from app2.views import *
app_name ='anything'
urlpatterns=[
    path('yadav/',yadav,name='yadav'),
    path('pythonmock/',pythonmock,name='pythonmock'),
    path('job/',job,name='job'),
]
