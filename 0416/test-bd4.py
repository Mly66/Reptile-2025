import requests
from bs4 import BeautifulSoup
import os


def getdata(url):
    r = requests.get(url)
    r.encoding = r.apparent_encoding
    return r.text


def getsoup(url):
    return BeautifulSoup(getdata(url), 'html.parser')


def printdata(data):
    for i in data:
        print(i.get("id"))


def savedata(data, file, path):
    if not os.path.isdir(path):
        os.makedirs(path)
    with open(file, 'w', encoding='utf-8') as f:
        for tag in data:
            content = tag.get("href")
            if content:
                f.write(content + '\n')



def main():
    url = "http://python123.io/ws/demo.html"
    data = getsoup(url)
    print("解析前")
    print(data)
    soup = getsoup(url)
    print("解析后")
    printdata(soup.find_all("a"))
    path = os.path.join(os.getcwd(), "data")
    file = os.path.join(path, "new.txt")
    savedata(soup.find_all("a"), file, path)


if __name__ == '__main__':
    main()
