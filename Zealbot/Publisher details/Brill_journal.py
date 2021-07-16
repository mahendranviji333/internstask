import requests
from bs4 import BeautifulSoup

from random_useragent.random_useragent import Randomize

r_agent_agent = Randomize()
rm_agent = r_agent_agent.random_agent('desktop', 'linux')
agent = {"User-Agent": rm_agent}
pageno=1
o = 1
list1 = []

while pageno <= 9:
    url = f'https://brill.com/browse?et=journal&level=parent&page={pageno}&pageSize=10&pubschedule_1=upcoming&pubschedule_2=new&pubschedule_3=published&sort=datedescending'
    page = requests.get(url, headers=agent)
    # print(page)
    soup = BeautifulSoup(page.content,'lxml')
    # print(soup)
    find_div = soup.find_all('div',attrs={'class' : 'display-flex flex-col flex-nowrap'})   #c-Button--link
    # print(urls)
    pageno +=1
    for i in find_div:

        urls = i.find('a',attrs={'class' : 'c-Button--link'})
        if urls is None:
            pass
        else:
            # dict1 = dict()
            # dict1['journal No'] = o
            # dict1 ['journal name'] = urls.text
            urls_val = 'https://brill.com'+str(urls['href'])
            print(urls_val)
            # dict1 ['journal Url'] = urls_val
            # print('Journal No :',o)
            # print('Journal name :',urls.text)
            # print('Url :','https://brill.com'+str(urls['href']))
            o +=1
        # list1.append(dict1)
    #<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>..
    # print(list1)