from bs4 import BeautifulSoup
import requests

url = "http://python123.io/ws/demo.html"
response = requests.get(url)
a = response.text
b = BeautifulSoup(a, 'html.parser')

for i in b.html.children:
    if i.name is not None:
        print(i.name, end=" ")
print()

l2 = []
for j in b.descendants:
    if j.name is not None:
        l2.append(j.name)
print(l2)

print(b.title.parent.name)

for m in b.a.parents:
    if m.name is not None:
        print(m.name, end=" ")
print()

print(b.body.next_siblings)

d2 = {"a": "1", "b": "2", "c": "3", "d": "4", "e": [1, 2, 3]}
print(d2)
d3 = {"class": "nb11", "name": ["a", "b", "c", "d", "e"], "num": [1, 2, 3, 4, 5], "project": ["a", "b", "c", "d", "e"]}
print(d3["name"][1])
if d3["name"][1] == "b":
    print(d3["name"][2])
