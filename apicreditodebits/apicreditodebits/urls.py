from django.contrib import admin
from django.urls import path, include
from core.views import PersonViewSet, DebtsViewSet
from rest_framework import routers
from rest_framework_jwt.views import obtain_jwt_token
from rest_framework_jwt.views import refresh_jwt_token


router = routers.DefaultRouter()
router.register(r'persons', PersonViewSet)
router.register(r'debits', DebtsViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('login/', obtain_jwt_token),
    path('refresh-token/', refresh_jwt_token),
]
