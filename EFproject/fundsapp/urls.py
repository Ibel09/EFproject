from django.urls import path, include

from . import views

from rest_framework import routers
from fundsapp.views import FundViewSet

router = routers.DefaultRouter()
router.register(r'fund', FundViewSet, basename='')
   
urlpatterns = [
    path('', views.index, name='index'),
    path('',  include(router.urls)), 
    path('fundsUpload/', views.upload_funds)
]
