from django.conf.urls.i18n import i18n_patterns
"""workers_management URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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

import debug_toolbar

from rest_framework import routers
from rest_api import views


router = routers.DefaultRouter()
router.register(r'companies', views.CompaniesViewSet)
router.register(r'managers', views.ManagersViewSet)
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)


urlpatterns = [
    path('works/', include('works.urls')),
    path('admin/', admin.site.urls),
    # path('accounts/', include('user_auth.urls', namespace='user_auth')),
    path('api/', include(router.urls)),
    path('api/', include('rest_api.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path(r'__debug', include(debug_toolbar.urls)),
]

urlpatterns += i18n_patterns(
    path('accounts/', include('user_auth.urls', namespace='user_auth')),
)
