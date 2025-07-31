from django.urls import path
# from test_app import  views
from test_app.views import home

urlpatterns =[ 
    path('', home , name = 'home'),
]