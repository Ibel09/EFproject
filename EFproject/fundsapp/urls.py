from django.urls import path

from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('fundsUpload/', views.upload_funds),
    path('listFunds/', views.list_funds),
]
