import requests
import sys
from bs4 import BeautifulSoup
from random_useragent.random_useragent import Randomize



r_agent_agent = Randomize()
rm_agent = r_agent_agent.random_agent('desktop', 'linux')
agent = {"User-Agent": rm_agent}



# url = input1

num =0
url = 'https://brill.com/view/journals/daph/daph-overview.xml?rskey=FAVN5a&result=89'
print('<><>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
print(url)
print('<><>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
page = requests.get(url, headers=agent)
soup = BeautifulSoup(page.content,'lxml')
# Article = soup.find('div',attrs={'class' : 'display-none display@xs-none display@sm-none display@md-flex flex@md-row flex@md-nowrap mr-4'})
Total_article = soup.find('div',attrs={'id' : 'container-45453-item-45472'})

sub_con = Total_article.find_all('div',attrs={'class':'configurable-layout w-1'})

for i in sub_con:
    num +=1
    # title1 = i.find('div',attrs={'class':'content-box-body null'})
    print('Artical Number ==>',num)
   
    title = i.find('h6',attrs={'class':'typography-body title mb-3 text-headline font-content'})
    if title is None :
        title1 = i.find('h6',attrs={'class':'typography-body title text-headline font-content'})
        print(title1.text)
        url = title1.find('a')
        print('https://brill.com/'+(url['href']))
    else:
        print(title.text)
        url = title.find('a')
        print('https://brill.com/'+(url['href']))

    
