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


def print_result(tags):
    regex = 'h(e|ea)?d'
    for tag in tags:
        if re.search(regex, tag):
            print(tag)
    regex = r'^h'
    for tag in tags:
        if re.search(regex, tag):
            print(tag)
    regex = 'h..l'
    for tag in tags:
        if re.search(regex, tag):
            print(tag)
    regex = '[a-c]'
    for tag in tags:
        if re.search(regex, tag):
            print(tag)
    regex = '^[^abc]'
    for tag in tags:
        if re.search(regex, tag):
            print(tag)
    regex = '^[ti|he]..'
    for tag in tags:
        if re.search(regex, tag):
            print(tag)
    regex = '\w'
    for tag in tags:
        if re.search(regex, tag):
            print(tag)
    regex = 'a$'
    for tag in tags:
        if re.search(regex, tag):
            print(tag)


def check_ip(ip):
    regex = '^(25[0-5]|2[0-4]\d|1\d{2}|[1-9]?\d)(\.(25[0-5]|2[0-4]\d|1\d{2}|[1-9]?\d)){3}$'
    if re.match(regex, ip):
        return True
    return False


def mean_re():
    a = re.search('p.*n', 'pyanbncndn')
    print(a.group())
    a = re.search('p.*?n', 'pyanbncndn')
    print(a.group())
    r = r'[1-9]\d{5}'
    mixed_list = ['100000', '12345', 'abcde', '123456', 'xyz789', '750000', 'invalid123']

    for item in mixed_list:
        if re.match(r, item):
            print(item)
    print()
    mixed = '10000012345abcde123456xyz789750000invalid123'
    a = re.search(r, mixed)
    print(a.group())
    print(a.start())
    print(a.end())
    print(a.string)
    print(a.re)
    print(a.span())
    print(a.pos)
    print(a.endpos)
    print("*" * 38)
    reg = re.compile(r'[a-z]')
    a = reg.search(mixed)
    print(a.group())
    a = reg.findall(mixed)
    print(a)
    a = reg.finditer(mixed)
    for i in a:
        print(i.group())
    a = reg.split(mixed)
    print(a)
    a = reg.sub("nb", mixed, 9)
    print(a)


def main():
    url = 'http://python123.io/ws/demo.html'
    html = get_html(url)
    soup = get_soup(html)

    print(soup.prettify())
    print(soup.title.string)

    path = './data'
    filename = 'data.txt'

    tags = [tag.name for tag in soup.find_all()]
    print_result(tags)
    save_text(path, filename, tags)

    ip = '192.168.127.552'
    if check_ip(ip):
        print("yes")
    else:
        print("no")
    mean_re()


if __name__ == '__main__':
    main()
