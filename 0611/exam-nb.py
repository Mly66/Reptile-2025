import requests
import re

r = requests.get('http://python123.io/ws/demo.html')
a = r.text
print(a)
b = re.compile('[1-9]\d{5}')
print(b.findall(a))
