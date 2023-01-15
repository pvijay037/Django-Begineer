'''
from django.urls import path
from .views import homePageView
urlpatterns = [
path('', homePageView, name='home'),
]'''
from django.urls import path
from .views import HomePageView
urlpatterns = [
path('', HomePageView.as_view(), name='home'),
]
