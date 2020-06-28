"""task URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from task.settings import MEDIA_ROOT, MEDIA_URL, STATICFILES_DIRS, STATIC_URL

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('registration.urls')),
    path('account/', include('account.urls')),

    # REST_FRAMEWORKS URLS
    path('api/account/', include('rest_framework.urls')),
    path('api/account/', include('account.api.urls', 'account_api')),
]
urlpatterns += static(settings.MEDIA_URL, document_root=MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=STATICFILES_DIRS)


