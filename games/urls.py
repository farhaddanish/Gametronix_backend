from django.urls import path
from . import views




urlpatterns = [
    path("games/<uuid:id>",views.details,name="game_details")
]
