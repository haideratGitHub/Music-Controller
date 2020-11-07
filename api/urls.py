from django.urls import path
from .views import main

# It is saying whatever the url is point it to main (which has been imported from views)
urlpatterns = [path("", main)]
