"""pastelprogrammer URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.contrib.auth import views as auth_views
from kostumerbase.views import dashboard,tambah_kostumer
from .views import logout_views,home,perusahaan
urlpatterns = [
    path('', home,name='home'),
  	path('rancapari/', include('kostumerbase.urls')),
    path('pprg/', include('pprg.urls')),
    path('kannada/', include('kannada.urls')),
    path('sindanglaya/', include('sindanglaya.urls')),
    path('perusahaan/', perusahaan,name='perusahaan'),


   
    path('adm/', admin.site.urls),
    path('logout/', logout_views,name='logout'),
    # path('tentang_kami/',tentang_kami,name='tentang_kami'),
    # path('gallery/',gallery,name='gallery'),
    # path('contact/',contact,name='contact'),
    # path('login/',login,name='login'),
    
    # path('dashboard/', include('admin_rjf.urls')),

    path('login/', auth_views.LoginView.as_view(template_name="dashboard_rancapari/login.html"), name='login'),

]
