"""trafficjam URL Configuration

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
from django.conf.urls import url
from . import views


#from django.contrib.auth.views import
urlpatterns = [
    url(r'^home/', views.home, name='home'),
    url(r'^traffic/', views.traffic_jam, name='traffic_jam'),
    url(r'^signup/',views.signup_view, name="signup"),
    url(r'^signin/', views.signin_view, name="signin"),
    url(r'^signout/', views.signout_view, name='signout'),
    url(r'^profile/', views.profile, name='View_profile'),
    url(r'^editprofile/', views.edit_profile, name='Edit_profile'),
    url(r'changepassword/',views.Change_password, name='Change_password'),
    url(r'post/', views.create_post, name='post_create'),
    url(r'^edit/(?P<id>\w{0,50})/$',views.edit_post, name='edit'),
   # url(r'^(?P<id>[0-9]+)/$',views.edit_post, name='edit'),
    #url(r'update/(?P<id>\w{0,50})/$',views.update_post, name='update'),
    url(r'delete/(?P<id>\w{0,50})/$',views.delete_post, name='delete'),
    url(r'search/',views.search, name='search'),
    url(r'map_location/',views.current_location, name='map_location'),
    url(r'trafficmap/',views.trafficmap_location, name='trafficmap_location'),
    url(r'satellitemap/',views.satellitemap_location, name='satellitemap_location'),
    url(r'weather_c/',views.weather_c, name='weather_c'),
    url(r'weather_f/',views.weather_f, name='weather_f'),
    #url(r'weather_f/',views.weather_city, name='weather_f'),
    url(r'about/',views.about_us, name='about_us'),
    url(r'contact/',views.contact_us, name='contact_us'),
    url(r'comment/',views.comment, name='comment'),
    url(r'comments/',views.comment_view, name='comment'),

]
