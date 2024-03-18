from bs4 import BeautifulSoup
import requests
import pandas as pd


headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
data_dict={'title':[],'description':[]}
    
def extract_page():
    with open('links','r') as file:
        for link in file:
            link=link.strip()
            parse(link)

def parse(url):
    r=requests.get(url,headers=headers)
    soup=BeautifulSoup(r.text,'html.parser')
    extract_content(soup)
    

def extract_content(sou):
    if sou.title:
        data_dict['title'].append(sou.title.string)
    else:
        data_dict['title'].append('no title')
    meta_tags =sou.find_all("meta")
    i=0
    for tag in meta_tags:
        if tag.get('name') == 'description':
            data_dict['description'].append(tag.get('content'))
            i+=1
            #print('coming inside if stmt.')
    if i==0:
        data_dict['description'].append('no description')
        #print('coming inside  else stmt.')
        #print(tag.get('name'),'\n\n')
    print(len(data_dict['description']))
    print(len(data_dict['title']))
# def print_dict(dic):
#     print('Title               Description')
#     for key,val in dic.items():
#         print(f'{key} -> {val}')



extract_page()

df = pd.DataFrame.from_dict(data_dict)
df.to_csv('data.csv')






