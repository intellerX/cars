from django.urls import path
from apps.cars.api.api import car_detail_api_view
from apps.cars.api.views import CarListAPIView

urlpatterns = [
    path( 'cars/', CarListAPIView.as_view() ,name = 'cars'),
    path('cars/<int:pk>/',car_detail_api_view, name = 'car_detail_api_view')
]