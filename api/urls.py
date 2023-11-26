from django.urls import path

from .views import HelloAPIView, NewsZaminUzView


urlpatterns = [
    path('hello/', HelloAPIView.as_view(), name='hello_api_view'),
    path('', NewsZaminUzView.as_view(), name='News Api, using Zamin.uz web site'),
]
