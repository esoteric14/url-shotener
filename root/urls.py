from django.contrib import admin
from django.urls import path
from django.http import HttpResponse
from root.views import getQuery,routeToUrl
# def 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',getQuery),
    path('<slug:key>/',routeToUrl)
]