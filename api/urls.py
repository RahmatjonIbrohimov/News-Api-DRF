from django.urls import path

from .views import NewsZaminUzView


urlpatterns = [
    path('', NewsZaminUzView.as_view(), name='News Api, using Zamin.uz web site'),
]
