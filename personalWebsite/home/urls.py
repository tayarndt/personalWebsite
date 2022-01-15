from django.urls import URLPattern, path
from . import views

# get home url pattern and views
urlpatterns = [
    path('', views.home, name='home'),
]
    