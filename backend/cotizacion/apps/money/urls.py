from django.urls import include, path
from rest_framework import routers

from .views import money, all_currency
router = routers.DefaultRouter()


urlpatterns = [
    path('<str:currency>/', money),
    path('all', all_currency)
]
