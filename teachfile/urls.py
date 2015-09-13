"""techfile URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from django.views.generic import TemplateView

from .views import IndexView, CourseListView, CourseView

urlpatterns = [
    url(r'^$', IndexView.as_view(), name='home'),
    url(r'^page/(?P<page>[0-9]+)/$', IndexView.as_view(), name='list'),
    url(r'^courses/$', CourseListView.as_view(), name='courses'),
    url(r'^course/(?P<id>[0-9]+)/$', CourseView.as_view(), name='course'),
    url(r'^admin/', include(admin.site.urls)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
