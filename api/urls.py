from django.urls import path
from .views import RoomView

# It is saying whatever the url is point it to main (which has been imported from views)
urlpatterns = [path("room", RoomView.as_view())]
