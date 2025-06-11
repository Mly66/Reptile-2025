import requests
import re
import os
import csv

r = requests.get('http://python123.io/ws/demo.html')
a = r.text
print(a)
b = re.compile('[1-9]\d{5}')
c = b.findall(a)
print(c)
d = b.finditer(a)
print(d)
if not os.path.exists("./exam-nb"):
    os.mkdir("./exam-nb")
l2 = [["序号", "数据"]]
with open('./exam-nb/exam-nb.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerows(l2)
    num = 0
    for i in c:
        writer.writerow([num, i])
        num += 1
    for match in d:
        writer.writerow([num, match.group()])
        num += 1

