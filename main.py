# тестовое ПО с примером парсинга информации с сайта

from bs4 import BeautifulSoup
import requests



url = "http://quotes.toscrape.com/"
response = requests.get(url)
print(response.content)
html = response.text

soup = BeautifulSoup(html, 'html.parser')
links = soup.find_all("a")
for link in links:
    print(link.get('href'))

text = soup.find_all("span", class_="text")
print(text)

# Создадим отдельную переменную author, куда будут сохраняться все авторы
author = soup.find_all("small", class_="author")
print(author)

#С помощью функции range(len) определим общее количество цитат
for i in range(len(text)):
    print(f"Цитата номер - {i + 1}")
    print(text[i].text)
    print(f"Автор цитаты - {author[i].text}\n")

