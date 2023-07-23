from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('authentiations/', include('authentication.urls')),
    path('orders/', include('orders.urls')),

    path('auth/', include('djoser.urls.jwt')), #/auth/jwt/create/
                                               #/auth/jwt/refresh/
                                               #/auth/jwt/verify/
]
