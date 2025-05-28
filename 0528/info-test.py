import os
import csv
import requests
from bs4 import BeautifulSoup


def get_html(url):
    response = requests.get(url)
    return response.text


def get_soup(html):
    return BeautifulSoup(html, 'html.parser')


def get_info(soup):
    l2 = []
    for i in soup.descendants:
        if i.name is not None and i.attrs != {}:
            l2.append(i.attrs['class'][-1])
    return l2


def write_txt(l, path):
    if not os.path.exists(path):
        os.makedirs(path)
    info_path = os.path.join(path, 'info.txt')
    with open(info_path, 'w') as f:
        for i in l:
            f.write(i + '\n')


def write_csv(l, path):
    if not os.path.exists(path):
        os.makedirs(path)
    info_path = os.path.join(path, 'info.csv')
    with open(info_path, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['编号', '类名'])
        for num, item in enumerate(l, start=1):
            writer.writerow([num, item])


def main():
    url = 'http://python123.io/ws/demo.html'
    html = get_html(url)
    soup = get_soup(html)
    list_info = get_info(soup)
    print()
    path = "./text"
    write_txt(list_info, path)
    path = "./csv"
    write_csv(list_info, path)
    print(soup.title.string)


if __name__ == '__main__':
    main()
