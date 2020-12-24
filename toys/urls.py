from django.urls import path
<<<<<<< HEAD
from . import views
=======
from toys import views
>>>>>>> origin/master

urlpatterns = [
    path('', views.dashboard, name="dashboard"),
]
