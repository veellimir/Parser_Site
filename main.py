from bs4 import BeautifulSoup
import requests

LINK_SITE = 'https://intetix.ru/projects/'
INFO_TEXT = 'Intetix_parser.txt'

response = requests.get(LINK_SITE).text
soup = BeautifulSoup(response, 'html.parser')

description_div = soup.find_all('div', class_='description')

with open(INFO_TEXT, 'w') as file:
    for div in description_div:
        link = div.find('a')
        if link:
            href = link.get('href')
            href_link = 'https://intetix.ru/' + href
            text = link.get_text()
            print(text, href_link)
            file.write(f'{text} - {href_link}\n')




