from django.contrib import admin
from django.urls import path, include
from restaurant.views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('tables', BookingViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('restaurant/', include('restaurant.urls')),
    path('restaurant/booking/', include(router.urls)),
]
