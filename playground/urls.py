from django.urls import path
from . import views

#URLConf
urlpatterns = [
    path('homepage/', views.homepageView),
    path('adresse1/', views.lieu1),
    path('adresse2/', views.lieu2)
]