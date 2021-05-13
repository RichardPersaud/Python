print("Webscraping...")


from bs4 import BeautifulSoup
import requests

url= "...." #url of the site you  want

content = requests.get(url).text

# print(soup)

soup = BeautifulSoup(content, "lxml")
h1_text = soup.find('h1', id="firstHeading")

print(h1_text)