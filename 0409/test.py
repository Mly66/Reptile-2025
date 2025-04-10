import requests

f2 = {"file": open("./pics/mJRWj5T.jpg", 'rb')}
r = requests.post("http://httpbin.org/post", data=f2)
print(r.text)

r2 = requests.post("https://mly66.github.io/blog/", timeout=200)
print(r2.text)
