from django.contrib import admin
from django.urls import path, include
from core.views import ConsumerViewSet, AssetsViewSet
from rest_framework import routers
from rest_framework_jwt.views import obtain_jwt_token
from rest_framework_jwt.views import refresh_jwt_token


router = routers.DefaultRouter()
router.register(r'consumer', ConsumerViewSet)
router.register(r'assets', AssetsViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('login/', obtain_jwt_token),
    path('refresh-token/', refresh_jwt_token),
]