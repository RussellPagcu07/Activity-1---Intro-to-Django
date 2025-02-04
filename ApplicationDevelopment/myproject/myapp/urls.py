from django.urls import path
from . import views  # Import views from the same app

urlpatterns = [
    path('', views.home, name='base'),  # When visiting /myapp/, show home view
]