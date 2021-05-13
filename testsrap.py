import requests
import bs4
res = requests.get('https://www.kiss-anime.ws/Anime/id-invaded')
res.text

soup = bs4.BeautifulSoup(res.text, 'lxml')
for link in soup.find_all('a',href=True):
    print(link['href'])
