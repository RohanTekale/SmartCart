from django.contrib import admin
from django.urls import path, include
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions

schema_view = get_schema_view(
    openapi.Info(
        title="SmartCart API",
        default_version="v1",
        description="API documentation for the E-Commerce platform",
        terms_of_service="https://www.yourwebsite.com/terms/",
        contact=openapi.Contact(email="support@yourwebsite.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # Authentication (User Management)
    path('api/v1/auth/', include('users.urls')),  

    # E-commerce functionality
    path('api/v1/products/', include('products.urls')),  
    path('api/v1/orders/', include('orders.urls')),  
    path('api/v1/cart/', include('cart.urls')),  

    # Swagger URLs
    path("swagger/", schema_view.with_ui("swagger", cache_timeout=0), name="schema-swagger-ui"),
    path("redoc/", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"),
]
