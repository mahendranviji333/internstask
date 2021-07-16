import sys
import requests
from bs4 import BeautifulSoup
input1 =sys.argv[1]

print(input1)   #sub domain Name
keys = dict()
lists = []

url = f'https://www.biomedcentral.com/search?query={input1}&searchType=publisherSearch'




def journalscrap(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content,'lxml')
    urls_details = soup.find_all('h3',attrs={'class' : 'c-listing__title'})

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
    next_page = soup.find('a',attrs={'class' : 'c-pagination__link','data-test':'next-page','rel':'next'})['href']
   
    nexturl = 'https://www.biomedcentral.com'+str(next_page)
    print(nexturl)
    journalscrap(nexturl)
    # if next_page is None:
    #     pass
    # else:
    #     journalscrap(nexturl)

journalscrap(url)


# print(keys)