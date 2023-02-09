
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from blog_app.views import StudentViewSet

router = DefaultRouter()
router.register('Student', StudentViewSet, basename='Student')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls))
]
