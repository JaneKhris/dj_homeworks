from django.contrib import admin
from django.urls import path

from measurement.views import SensorsAPI, SensorAPI, MeasurementAPI

urlpatterns = [
    path('sensors/', SensorsAPI.as_view()),
    path('sensors/<pk>/', SensorAPI.as_view()),
    path('measurements/', MeasurementAPI.as_view()),

]
