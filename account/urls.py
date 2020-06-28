from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('request_verification/', views.request_verification, name="request_verification"),
    path('update_profile/', views.update_profile, name="update_profile"),
    path('upload_image/', views.upload_image, name='upload_image'),

    path('create_package/', views.create_package, name='create_package'),
    path('view_package/<str:pk>/', views.view_package, name="view_package"),
    path('update_package/<str:pk1>/', views.update_package, name="update_package"),
    path('delete_package/<str:pk2>/', views.delete_package, name="delete_package"),

    path('all_images/<str:pk>/', views.all_images, name="all_images"),

    path('<str:pk_test>/', views.details, name='details'),

    path('profile/<str:pk>/', views.profile, name='profile'),
]