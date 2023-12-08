"""
URL configuration for sadman project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings


from myapp import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('userwork1',views.userwork,name='userwork1'),
    path('',views.Header,name='Home'),
        path('Home',views.Header,name='Home'),

    path('header',views.about1,name='about',),
    path('basic',views.basic1,name='basic'),
    path('about',views.AboutUs,name='about'),
    path('login',views.loginpage,name='login'),
    path('contract',views.contractpage,name='contract'),
    path('footer',views.footerpage,name='footer'),
    path('cheakout',views.cheakoutpage,name='cheakout'),

]+static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
