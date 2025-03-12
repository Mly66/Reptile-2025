import requests

r = requests.get('https://www.baidu.com')
print(r.status_code)
try:
    print(r.encoding)
    print(r.apparent_encoding)
    r.encoding = r.apparent_encoding
    print(r.content)
    print(r.cookies)
    print(r.text)
except:
    print("error")
finally:
    print("success")
