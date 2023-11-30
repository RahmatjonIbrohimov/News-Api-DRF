from django.urls import path

from .views import NewsZaminUzView, migration, NewsFilterView


urlpatterns = [
    path('', NewsZaminUzView.as_view(), name='News Api, using Zamin.uz web site'),
    path('filter/', NewsFilterView.as_view(), name='FIlter Page'),
    path('migrations/', migration, name='do migrations'),
]
