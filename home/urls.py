from django.urls.conf import include
from . import views
from django.urls import path
from django.urls.resolvers import URLPattern
urlpatterns = [
    path("",views.homeIndex,name="home"),
    path("challenge/",views.challenge,name='challenge'),
    path("challenge/validation/",views.chalval,name='chalval'),
]