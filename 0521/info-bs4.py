import requests
from bs4 import BeautifulSoup
import os
import csv


def get_html(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.text
    except requests.RequestException as e:
        print(f"请求失败: {e}")
        return ""


def bs4_html(html):
    return BeautifulSoup(html, 'html.parser')


def create_dir(directory):
    if not os.path.exists(directory):
        os.mkdir(directory)


def get_elements(soup):
    class_list = []
    for element in soup.descendants:
        if element.name is not None and 'class' in element.attrs:
            print(element.attrs['class'][-1], end="   ")
            class_list.append(element.attrs['class'][-1])
    return class_list


def list_txt(class_list, directory):
    if not os.path.exists(directory):
        os.mkdir(directory)
    with open(f"{directory}/test521.txt", 'w', encoding='utf-8') as f:
        for item in class_list:
            f.write(item + '\n')


def list_csv(class_list, directory):
    if not os.path.exists(directory):
        os.mkdir(directory)
    with open(f"{directory}/test521.csv", 'w', encoding='utf-8', newline='') as f:
        csv_writer = csv.writer(f)
        csv_writer.writerow(["num", "info"])
        i = 0
        for item in class_list:
            print(item)
            i += 1
            csv_writer.writerow([i, item])


def get_csv(directory):
    with open(f"{directory}/test521.csv", 'r', encoding='utf-8', newline='') as f:
        csv_reader = csv.reader(f)
        for row in csv_reader:
            for i in row:
                print(i.ljust(10), end="   ")
            print()


def main():
    url = 'http://python123.io/ws/demo.html'
    html_content = get_html(url)
    if not html_content:
        return

    soup = bs4_html(html_content)
    print(soup.prettify())

    directory = "./nbnb"
    create_dir(directory)
    class_list = get_elements(soup)
    list_txt(class_list, directory)
    list_info = [
        ["name", "age", "gender"],
        ["Alice", 25, "Female"],
        ["Bob", 30, "Male"],
        ["Charlie", 22, "Male"],
        ["Daisy", 28, "Female"],
        ["Ethan", 35, "Male"],
        ["Fiona", 27, "Female"],
        ["George", 29, "Male"],
        ["Hannah", 24, "Female"],
        ["Isaac", 31, "Male"],
        ["Jackie", 26, "Female"]
    ]
    list_csv(class_list, directory)
    # get_csv(directory)


if __name__ == '__main__':
    main()
