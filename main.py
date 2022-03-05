from bs4 import BeautifulSoup
import requests

with open('simple.html') as html_file:
    soup = BeautifulSoup(html_file, 'lxml')

for article in soup.find_all('div' , class_='article'):
    print(article.h2.a.text)
    print(article.p.text)