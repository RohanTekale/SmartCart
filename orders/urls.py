from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import OrderViewSet

# Create a router for OrderViewSet
router = DefaultRouter()
router.register(r'orders', OrderViewSet, basename='order')

# Include router URLs in urlpatterns
urlpatterns = [
    path('', include(router.urls)),  # Includes all order-related API routes
]
