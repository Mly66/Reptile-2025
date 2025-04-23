from bs4 import BeautifulSoup
import requests


def get_soup(url):
    response = requests.get(url)
    return BeautifulSoup(response.text, 'html.parser')


def main():
    url = 'https://python123.io/ws/demo.html'
    soup = get_soup(url)
    # print(soup.prettify())
    # print(soup.title)
    # print(soup.title.string)
    # print(soup.title.parent.name)
    # print(soup.p.attrs)
    # print(soup.p.attrs['class'])
    # print(soup.p.attrs['class'][-1])
    # print(soup.contents)
    # print(type(soup.contents))
    for content in soup.children:
        print(content)
    print(type(soup.children))
    list = []
    list2 = []
    for child in soup.descendants:
        if child.name is not None:
            print(child.name, end=' ')
            list.append(child.name)
            list2.insert(0, child.name)
            print(type(child))

    print(list)
    print(list2)
    list2.reverse()
    print(list2)


if __name__ == '__main__':
    main()
