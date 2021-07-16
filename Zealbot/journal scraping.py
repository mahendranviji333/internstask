import sys
import requests
from bs4 import BeautifulSoup
input1 =sys.argv[1]

print(input1)   #sub domain Name

url = f'https://www.biomedcentral.com/search?query={input1}&searchType=publisherSearch'
page = requests.get(url)
soup = BeautifulSoup(page.content,'lxml')
urls_details = soup.find_all('h3',attrs={'class' : 'c-listing__title'})
keys = dict()
lists = []

# print(url)  #journal Url

for i in urls_details:
    hrefs =i.find('a')
    titles=hrefs.text
    links = 'https:'+str(hrefs['href'])
    # print(titles)
    # print(links)
    lists.append(links)
keys['Subdomain'] = input1
keys['Url links'] = lists

print(keys)