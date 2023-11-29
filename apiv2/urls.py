from django.urls import path
from rest_framework.routers import SimpleRouter

from .views import NewsZaminUzView, ProductList


urlpatterns = [
    path('', NewsZaminUzView.as_view(), name='News Api, using Zamin.uz web site'),
    path('filter/', ProductList.as_view()),
]
