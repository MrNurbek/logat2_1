"""djangodictionary URL Configuration

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
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from main.views import *
from djangodictionary import settings

urlpatterns = [

                  # path('', HomePageView.as_view(), name="home"),
                  # path("", HomePageView2.as_view(), name="home2"),
                  path("", HomePageView3.as_view(), name="home"),
                  path("loyiha", HomePageView0.as_view(), name="loyiha"),
                  path("foydalanish", HomePageView01.as_view(), name="foydalanish"),
                  path("index/<int:id>", homePageView2, name="index"),
                  path('contact', contact_view, name='contact'),
                  path('about', about_view, name='about'),
                  path("search/", SearchResultsView.as_view(), name="search_results"),
                  path("search2/", SearchResultsView2.as_view(), name="search_results2"),
                  path("search3/", SearchResultsView3.as_view(), name="search_results3"),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL,
                                                                                         document_root=settings.STATIC_ROOT)
