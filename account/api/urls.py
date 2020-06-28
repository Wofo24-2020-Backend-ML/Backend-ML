from django.urls import path, include
from account.api import views
from . views import *
from rest_framework.routers import DefaultRouter

app_name = 'account'
router = DefaultRouter()
router.register('users', UserViewSet)
router.register('categories', CategoryViewSet)
router.register('packages', PackageViewSet)
# router.register('uploadimageAdminView', UploadImageAdminView)   
router.register('uploadimagesViewSet', UploadImageViewSet)

urlpatterns = [
    path('', include(router.urls))
]

