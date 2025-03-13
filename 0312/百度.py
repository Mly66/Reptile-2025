import requests

url = "https://www.baidu.com"
r = requests.get(url)
print(r.status_code)
try:
    print(r.encoding)
    print(r.apparent_encoding)
    r.encoding = r.apparent_encoding
    print(r.content)
    print(r.cookies)
    print(r.text)
    with open("test.txt", "w+", encoding="utf-8") as f:
        print(1)
        f.write("r.text")
        f.seek(0)
        print(f.read())
        print(2)
        f.write(r.text)

finally:
    f.close()
    print("success")
