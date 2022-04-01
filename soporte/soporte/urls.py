"""soporte URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from argparse import Namespace
from django.contrib import admin
from django.contrib.auth.decorators import login_required
from django.urls import path,include
from django.contrib.auth.views import LoginView,logout_then_login,PasswordChangeView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',login_required(LoginView.as_view(template_name = 'index.html')), name = 'index'),
    path('accounts/login/',LoginView.as_view(template_name = 'login.html'), name = 'login'),
    path('accounts/chage_password/',PasswordChangeView.as_view(template_name = 'cuenta/change_password.html'), name = 'change_password'),
    path('logout/',logout_then_login,name='logout'),
    path('encuesta/', include('apps.encuesta.urls'),name='encuesta'),
    path('flotaEntrega/', include('apps.flotaEntrega.urls'),name='flotaEntrega'),
    path('usuario/', include('apps.usuario.urls'),name='usuario'),
]
