"""
URL configuration for management_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.urls import path,include
from rest_framework.routers import DefaultRouter
from api_app import views


router = DefaultRouter()
router.register(r'GetData',views.GetData)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(router.urls)),
    path('listData/',views.listData.as_view()),
    path('loginPage/',views.loginPage.as_view()),
    path('list_view/',views.list_view.as_view()),
    path('dele/',views.dele.as_view())
]
