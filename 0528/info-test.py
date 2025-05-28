import requests
from bs4 import BeautifulSoup


def get_html(url):
    response = requests.get(url)
    return response.text


def get_soup(html):
    return BeautifulSoup(html, 'html.parser')


def main():
    url = 'http://python123.io/ws/demo.html'
    html = get_html(url)
    soup = get_soup(html)
    print(soup.title.string)


if __name__ == '__main__':
    main()
