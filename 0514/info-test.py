from bs4 import BeautifulSoup
import requests
import os

url = "http://python123.io/ws/demo.html"
r = requests.get(url)
a = r.text
b = BeautifulSoup(a, 'html.parser')
a_tags = b.find_all('a')
# print(b.p.attrs)
for tag in a_tags:
    print(tag.get('href'))

with open("0514/0514.txt", "a") as file:
    for i in b.descendants:
        if i.name == "a" and 'href' in i.attrs:
            file.write(i.attrs['href'] + "\n") 

if not os.path.exists("0514/nbmly"):
    os.mkdir("0514/nbmly")
# if not os.path.exists("0514/nbmly/test.txt"):
#     os.mkdir("0514/nbmly/test.txt")
with open("0514/nbmly/test.txt", "w") as file:
    n = 1
    for i in b.descendants:
        if i.name == "a" and 'href' in i.attrs:
            file.write(str(n) + i.attrs['href'] + "\n")
            n = n + 1