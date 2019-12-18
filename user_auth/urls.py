from . import views
from django.urls import path, include
from django.contrib.auth import views as auth_views


app_name = 'user_auth'

urlpatterns = [
    # ex: /accounts/ - index page
    # ex: /accounts/login/ - login from account
    path('', views.index, name='index'),
    # ex: /accounts/logout/ - logout from company
    path('logout/',auth_views.LogoutView.as_view(template_name='user_auth/logged_out.html'),
    ),

]
