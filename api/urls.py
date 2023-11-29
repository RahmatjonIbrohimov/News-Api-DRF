from django.urls import path

from .views import NewsZaminUzView, migration


urlpatterns = [
    path('', NewsZaminUzView.as_view(), name='News Api, using Zamin.uz web site'),
    path('migrations/', migration, name='do migrations'),
]
