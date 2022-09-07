from bs4 import BeautifulSoup
import requests
from csv import writer

url = "https://www.pararius.com/apartments/amsterdam?ac=1"
source = requests.get(url)

soup = BeautifulSoup(source.content, 'html.parser')
lists = soup.find_all('section', class_="listing-search-item")

with open('Apartments.csv', 'w', encoding='utf8', newline='') as f:
    thewriter = writer(f)
    header = ['Apartments in Amsterdam', 'Price']
    thewriter.writerow(header)

    for x in lists:
        title = x.find('a', class_="listing-search-item__link--title").text.replace('\n', '')
        price = x.find('div', class_="listing-search-item__price").text.replace('\n', '')

        info = (title, price)

        print(info)
        thewriter.writerow(info)