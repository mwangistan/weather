from django.urls import path
from apps.api.views import TemperatureAPIView

urlpatterns = [
    path('locations/<str:city>/', TemperatureAPIView.as_view(), name='get_temperature'),
]