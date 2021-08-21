"""LKHWebsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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

from pages.views import blogView, home_view, contact_view, about_view, vue_test
from products.views import product_detail_view, product_create_view, contact
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [

    path('home/', home_view, name='home'),
    path("contact/", contact_view, name="contact"),
    path('about/', about_view, name="about"),
    path('product/', product_detail_view),
    path('create/', product_create_view),
    path('test/', vue_test),
    # path('api/')
    # path('vuetifyTest/', vueT_test),
    path('admin/', admin.site.urls),
    path(r'^blogs/$', blogView),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
