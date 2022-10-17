from django.urls import path

from . import views
from .views import gameView

urlpatterns = [
    path('', gameView.as_view(), name='gameView'),
]