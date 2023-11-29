import requests
from bs4 import BeautifulSoup
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import NewsKeeperModel


class NewsZaminUzView(APIView):
    def get(self, request):
        url = 'https://zamin.uz/uz/'
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        short_items = soup.find_all('div', class_='short-item')
        data_zamin = [] 

        for item in short_items:
            photo = f"https://zamin.uz/{item.find('a', class_='short-img').find('img')['src']}"
            link = item.find('a', class_='short-img')['href']
            title = item.find('a', class_='short-title').text.strip()

            # Berilgan Linkga kirib u yerdan 'Description'ni olib keladi
            link_response = requests.get(link)
            link_soup = BeautifulSoup(link_response.text, 'html.parser')
            p_tags = link_soup.find_all('p')
            date_description = link_soup.find('div', class_='fcat').text

            testval = []
            for p in p_tags:
                p_tag = p.text.strip()
                if len(p_tag) > 2:
                    testval.append(p_tag)
                content = ''.join(testval)[0:123]

            if not NewsKeeperModel.objects.filter(title=title).exists():
                news_data = NewsKeeperModel(
                    photo=photo,
                    title=title,
                    url=link,
                    description=content,
                    date=date_description[9:]
                )
                news_data.save()

            item_data = {'Photo': photo, 'Title': title, 'Url': link, 'Description': content, 'Date': date_description[9:]}
            data_zamin.append(item_data)

        return Response(data_zamin)
    