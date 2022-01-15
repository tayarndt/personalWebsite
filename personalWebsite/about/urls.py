from django.urls import URLPattern, path, include
from . import views

# make about url showing the about page
urlpatterns = [
    path('', views.about, name='about'),
]
