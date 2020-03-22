import requests
from urllib import request
from bs4 import BeautifulSoup as BS

response = requests.get('https://kinokrad.co/')
html = BS(response.content, 'html.parser')


respon = request.urlopen('https://kinokrad.co/')
print(respon.headers)

for elem in html.select('date'):
    title = elem.select('date')
    # meta = elem.select('meta')
    # for met in meta:
        # print(met)
    # date_each_title = elem.select('fbq')
    # print(date_each_title[0].text)
    # print(elem)
    # print(meta[3].text)
    print(f'Title page {title[0].text}')






