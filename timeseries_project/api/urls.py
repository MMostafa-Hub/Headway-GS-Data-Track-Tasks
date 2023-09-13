from django.urls import path
from .views import views

urlpatterns = [
    path("use_case", views.add_use_case),
    path("list_simulators", views.list_simulators),
    path("run_simulator", views.restart_simulator),
    path("stop_simulator", views.stop_simulator),
]
