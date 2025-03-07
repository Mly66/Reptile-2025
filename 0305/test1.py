import requests

r = requests.get("https://www.baidu.com")
print(r.status_code)
try:
    print(r.encoding)
    print(r.apparent_encoding)
    r.encoding = r.apparent_encoding
    print(r.text)
    print(r.headers)
    print(type(r.headers))
except:
    print("请求失败")
finally:
    print("程序结束")
