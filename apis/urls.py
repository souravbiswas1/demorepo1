from django.contrib import admin
from django.urls import path,include
from rest_framework.authtoken.views import obtain_auth_token
from django.contrib import admin
# from django.conf.urls import url
from django.urls import include, path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework.routers import SimpleRouter

from . import sum_mean

urlpatterns = [
    path('calculate_sum_mean', sum_mean.calculate_sum_mean),
]
