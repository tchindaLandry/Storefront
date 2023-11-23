from django.urls import path
from . import views

#URLConf
urlpatterns = [
    path('location/', views.collect_location),
    path('getlocation/', views.getlocationView)
]