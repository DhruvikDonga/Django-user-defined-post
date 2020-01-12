from django.urls import path

from . import views
urlpatterns = [
    
    path("snippet_detail", views.snippet_detail),
    path('',views.usblog,name='usblog')
]