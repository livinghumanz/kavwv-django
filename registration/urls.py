from django.urls.conf import include
from . import views
from django.urls import path
from django.urls.resolvers import URLPattern
urlpatterns = [
    path("",views.regStudent,name="register"),
    
]