import requests
url='http://httpbin.org'
re=requests.post(url+'post',data='nbmly')
print(re.text)