import requests
from bs4 import BeautifulSoup
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView


class HelloAPIView(APIView):
    def get(self, request):
        respond = {'Remember': 'Hello, This is News Api using Django Rest Framework!'}
        return Response(respond, status=status.HTTP_200_OK)
