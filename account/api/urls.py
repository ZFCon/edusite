from rest_framework import routers
from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

from . import views
from account.api.views import (

    registration_view,
    account_properties_view, 
    update_account_view,
    logout_view,
    
    )


app_name = 'account'

urlpatterns = [
    path('', obtain_auth_token, name="login"),
    path('logout', logout_view, name="logout"),
    path('profile/', account_properties_view, name="profile"),
    path('profile/update', update_account_view, name="update"),
    path('register', registration_view, name="register"),
]

