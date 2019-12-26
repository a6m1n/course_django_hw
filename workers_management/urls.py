from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.urls import path, include

import debug_toolbar

from rest_framework import routers
from works.rest_api import views


router = routers.DefaultRouter()
router.register(r'companies', views.CompaniesViewSet)
router.register(r'managers', views.ManagersViewSet)
router.register(r'workers', views.WorkerViewSet)
router.register(r'works', views.WorkViewSet)
router.register(r'workplace', views.WorkPlaceViewSet)
router.register(r'work-times', views.WorkTimeViewSet)
router.register(r'statistics', views.StatisticsViewSet)
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)


urlpatterns = [
    path('works/', include('works.urls')),
    path('admin/', admin.site.urls),
    # path('accounts/', include('user_auth.urls', namespace='user_auth')),
    path('api/', include(router.urls)),
    path('api/', include('works.rest_api.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path(r'__debug', include(debug_toolbar.urls)),
]

urlpatterns += i18n_patterns(
    path('accounts/', include('user_auth.urls', namespace='user_auth')),
)
