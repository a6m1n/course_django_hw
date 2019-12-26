from django.urls import path
from . import views
from rest_framework.authtoken import views
from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='Pastebin API')

urlpatterns = [
    path(r'docs/', schema_view), 
    path(r'api-token-auth/', views.obtain_auth_token)
]
