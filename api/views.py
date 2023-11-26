import requests
from bs4 import BeautifulSoup
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView


class NewsZaminUzView(APIView):
    def get(self, request):

        url = 'https://zamin.uz/uz/'
        response = requests.get(url)

        soup = BeautifulSoup(response.text, 'html.parser')
        short_items = soup.find_all('div', class_='short-item')

        data_zamin = [] 

        for item in short_items:
            photo = f" https://zamin.uz/{item.find('a', class_='short-img').find('img')['src']}"
            link = item.find('a', class_='short-img')['href']
            title = item.find('a', class_='short-title').text.strip()
            # content = item.find('div', class_='short-description')


            item_data = {'Photo':photo, 'Title': title, 'Url': link}
            data_zamin.append(item_data)

        return Response(data_zamin)
    