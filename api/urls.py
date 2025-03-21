
from django.urls import path
from .views import submit_sensor_data, get_sensor_data

urlpatterns = [
    path('submit-sensor-data/', submit_sensor_data, name='submit_sensor_data'),
    path('get-sensor-data/', get_sensor_data, name='get_sensor_data'),
]
