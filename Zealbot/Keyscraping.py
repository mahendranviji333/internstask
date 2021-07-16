import requests
import sys
from bs4 import BeautifulSoup

url = 'https://bmcproc.biomedcentral.com/articles/10.1186/1753-6561-5-S7-I13'

page = requests.get(url)

soup = BeautifulSoup(page.content,'lxml')

def abstract(soup):
    abstract = soup.find('meta',attrs = {'name' : 'citation_abstract'})['content']
    return abstract


def title(soup):
    title = soup.find('meta',attrs = {'name':'dc.title'})['content']
    return title


def artical_type(soup):
    Artical_type = soup.find("meta",attrs={'name':"citation_article_type"})['content']

    
def authors(soup): #pending
    Authors = soup.find('meta',attrs = {'name':'citation_author'})['content']
    return Authors


def address(soup): #pending
    Address=soup.find("meta",attrs = {'name':"citation_author_institution"})['content']

def doi(soup):
    doi = soup.find('meta',attrs = {'name':'citation_doi'})['content']
    return doi

def html_url(soup):
    Html_url = soup.find('meta',attrs = {'name':'citation_fulltext_html_url'})['content']


def pdf_url(soup):
    Pdf_url = soup.find('meta',attrs = {'name':'citation_pdf_url'})['content']
    return Pdf_url


def volume(soup):
    Volume = soup.find('meta',attrs = {'name':'citation_volume'})['content']
    return Volume


def keys(soup):
    Keys = soup.find_all('meta',attrs = {'class':'c-article-subject-list__subject'})
    for i in keys:
        return Keys.text


def publication_date(soup):
    publication_date = soup.find('meta',attrs = {'name' : 'prism.publicationDate'})['content']
    return publication_date


def ISSN(soup):
    ISSN = soup.find('div',attrs = {'name' : 'citation_issn'})['content']

    return ISSN


def corresponding_author(soup):#pending
    Corresponding_author = soup.find('span',attrs = {'class' : 'icon-text float-left'}).text
    Corresponding_author_out = Corresponding_author.split(': ')[1]

    return Corresponding_author_out

def journal_scrap(soup):

    Scraping_dict = {}
    # Scraping_dict['abstract'] = abstract(soup)
    # Scraping_dict['title'] = title(soup)
    # Scraping_dict['artical_type'] = "Article"
    Scraping_dict['authors_name'] = authors(soup)
    # Scraping_dict['Address'] = Address
    # Scraping_dict['Email']=""
    Scraping_dict['doi'] = doi(soup)
    # Scraping_dict['html_url'] = Html_url
    # Scraping_dict['Pdf_url'] = pdf_url(soup)
    # Scraping_dict['volume'] = volume(soup)
    # Scraping_dict['keywords'] = keys(soup)
    # Scraping_dict['publication_date'] = publication_date(soup)
    # Scraping_dict['ISSN']=ISSN(soup)
    # Scraping_dict['Corresponding_author']=Corresponding_author_out

    print(Scraping_dict)

# if __name__ == "__main__":
    
#     input_data = sys.argv[1]
#     page = requests.get(input_data)
#     soup = BeautifulSoup(page.content,'lxml')
#     journal_scrap(soup)

input_data = sys.argv[1]