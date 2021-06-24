
from django.contrib import admin
from django.urls import path,include
from apps.cars.api.views import CarListAPIView

from apps.users.views import Login

urlpatterns = [
    path('admin/', admin.site.urls),
    path( 'usuario/', include('apps.users.api.urls')),
    path( 'cars/', include('apps.cars.api.urls')),
    path( '',Login.as_view(),name='Login')
]
