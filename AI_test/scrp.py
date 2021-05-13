# import requests
# from bs4 import BeautifulSoup
# from csv import writer
# import datetime


# response = requests.get('https://9anime.to/watch/black-clover-dub.2y44/6mq179')

# soup = BeautifulSoup(response.text, 'html.parser')

# posts = soup.find_all(class_='player')

# with open('posts.csv', 'w') as csv_file:
#     csv_writer = writer(csv_file)
#     headers = ['Title', 'Link', 'Date']
#     csv_writer.writerow(headers)

#     for post in posts:
#         title = post.find(class_='title').get_text().replace('\n', '')
#         link = post.select("a[href]")

#         date = datetime.datetime.now()
#         #  post.select('.meta col-sm-12')[0].get_text()

#         csv_writer.writerow([title, link, date])
#         print([title, link, date])


import csv
from bs4 import BeautifulSoup
import requests

resp = requests.get('http://gogoanimee.io/black-clover-tv-episode-75')
soup = BeautifulSoup(resp.text, 'lxml')
type(soup)

posts = str(soup.find_all('iframe'))

with open("Output.txt", "w") as txt_file:
    for line in posts:
        # works with any number of elements in a line
        txt_file.write(" ".join(line))

fileHandle = open('Output.txt', 'r')

for line in fileHandle:
    fields = line.split(' ')
    tep = fields[6].split('"></iframe>]')

    temp = tep[0].split('src="')

with open("links.txt", "w") as txt_file:
    txt_file.write(temp[1])


fileHandle.close()
