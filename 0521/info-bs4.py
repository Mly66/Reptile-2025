import requests
from bs4 import BeautifulSoup
import os


def get_html(url):
    response = requests.get(url)
    return response.text


def bs4_html(html):
    return BeautifulSoup(html, 'html.parser')


def create_dir(directory):
    if not os.path.exists(directory):
        os.mkdir(directory)


def get_elements(soup):
    with open("./nbnb/test521.txt", 'w') as f:
        for element in soup.descendants:
            if element.name is not None and element.attrs:
                if 'class' in element.attrs:
                    print(element.attrs['class'][-1], end="")
                    f.write(element.attrs['class'][-1] + "\n")
    f.close()


def main():
    url = 'http://python123.io/ws/demo.html'
    html_content = get_html(url)
    soup = bs4_html(html_content)
    print(soup.prettify())

    directory = "./nbnb"
    create_dir(directory)
    get_elements(soup)


if __name__ == '__main__':
    main()
