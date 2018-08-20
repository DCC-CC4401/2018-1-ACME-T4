from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing_articles, name='landing'),
    path('articles/', views.landing_articles, name='landing_articles'),
    path('spaces/', views.landing_spaces, name='landing_spaces'),
    path('search/', views.search, name='search'),
    path('space_request/',views.space_request, name='space_request'),
    path('check_user/',views.check_user, name='check_user')
]
