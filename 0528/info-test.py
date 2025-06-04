import os
import re

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
    # for i in soup.descendants:
    #     if i.name is not None and i.attrs != {}:
    #         l2.append(i.attrs['class'][-1])
    for i in soup.find_all(True):
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


def get_csv(path):
    data = []
    with open(path, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        next(reader)
        for row in reader:
            data.append(row)
    return data


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
    csv_path = path + "/info.csv"
    data = get_csv(csv_path)
    print(data)
    print(soup.find_all(['a', 'b']))
    for i in soup.find_all(True):
        if i.name is not None: print(i.name, end=' ')
    print()
    for i in soup.find_all(re.compile('b')):
        print(i.name)
    href_list = []
    for i in soup.find_all(id=re.compile('link')):
        print(i.get('href'))
        href_list.append(i.get('href'))
    write_csv(href_list, path)

    e = '{:4}\t{:4}'
    j = 1
    with open('./text/info.txt', 'a', encoding='utf-8') as f:
        for i in soup.find_all(True):
            if not i.name is None:
                print(e.format(j, i.name))
                f.write(e.format(j, i.name))
                f.write('\n')
                j += 1


if __name__ == '__main__':
    main()
