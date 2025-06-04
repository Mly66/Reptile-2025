import requests
from bs4 import BeautifulSoup
import os
import re


def get_html(url):
    response = requests.get(url)
    return response.text


def get_soup(html):
    return BeautifulSoup(html, 'html.parser')


def save_text(path, filename, data):
    e = '{:<4}\t{:<4}\n'
    if not os.path.exists(path):
        os.makedirs(path)
    with open(os.path.join(path, filename), 'w', encoding='utf-8') as f:
        f.write(e.format("序号", "标签"))
        for i, tag in enumerate(data, start=1):
            f.write(e.format(i, tag))


def main():
    url = 'http://python123.io/ws/demo.html'
    html = get_html(url)
    soup = get_soup(html)

    print(soup.prettify())
    print(soup.title.string)

    path = './data'
    filename = 'data.txt'

    tags = [tag.name for tag in soup.find_all()]

    save_text(path, filename, tags)


if __name__ == '__main__':
    main()
