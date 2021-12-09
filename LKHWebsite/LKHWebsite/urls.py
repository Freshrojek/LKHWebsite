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
from pages import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
  path('', views.frontend),
  path('article/', views.frontend),
  path('author/', views.frontend),
  path('article/<slug:slug>/', views.frontend),
  path('author/<slug:slug>/', views.frontend),
  path('home/', views.home_view, name='home'),
  path("contact/", views.contact_view, name="contact"),
  path('about/', views.about_view, name="about"),
  # path('product/', product_detail_view),
  path('test/', views.vue_test),
  # path('api/')
  # path('vuetifyTest/', vueT_test),
  path('admin/', admin.site.urls),
  path(r'^blogs/$', views.blogView),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
