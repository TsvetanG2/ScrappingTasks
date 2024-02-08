from bs4 import BeautifulSoup
import requests

URL = 'https://quotes.toscrape.com/'
html_text = requests.get('https://quotes.toscrape.com/')
soup = BeautifulSoup(html_text.text, 'html.parser')
quotes = soup.find_all('div', class_='quote')

with open("output.txt", "w") as f:
    for quote in quotes:
        author = quote.find('small', class_='author').text
        text = quote.find('span', class_='text').text
        tags = '; '.join(tag.text for tag in quote.find_all('a', class_='tag'))

        f.write("{")
        f.write("\n")
        f.write("'text'  : " + f'{text}\n')
        f.write("'author' : " + f"'{author}'\n")
        f.write("'tags'   : " + f"'{tags}'\n")
        f.write("'url'    : " + f"'{URL}'\n")
        f.write("}\n")
        f.write("\n")
