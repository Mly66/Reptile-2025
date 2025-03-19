import os

import requests
from bs4 import BeautifulSoup


def gethtml(url, key):
    try:
        r = requests.get(url, params=key)
        print(r.status_code)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return str(len(r.text))
    except:
        print("errot")
        return None
    finally:
        print("sucess")


def writetxt(txt, filename):
    if os.path.exists(filename):
        print(filename + "已经存在")
    else:
        os.makedirs(filename)
    with open(filename, 'w', encoding="utf-8") as f:
        print("正在写入" + filename)
        f.write("获取网页内容如下" + '\n')
        f.write(txt)
        f.close()
        print("sucess")
        return filename


def getpic(url, root):
    path = root + url.split('/')[-1]
    try:
        if not os.path.exists(root):
            os.mkdir(root)
        if not os.path.exists(path):
            r = requests.get(url)
            with open(path, 'wb') as f:
                f.write(r.content)
                f.close()
                print("sucess")
        else:
            print("文件已存在")
    except:
        print("error")
    finally:
        print("nb")


def getip(ip):
    url = "https://www.ipshudi.com/"
    print(url + ip + ".htm")
    r = requests.get(url + ip + ".htm")
    r.encoding = r.apparent_encoding
    return r.text


def reip(ip):
    url = "https://www.ipshudi.com/"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"
    }  # 伪造头文件请求

    try:
        r = requests.get(url + ip + ".htm", headers=headers, timeout=10)
        r.raise_for_status()  # 检查 HTTP 响应状态码
        r.encoding = r.apparent_encoding
        return r.text
    except requests.exceptions.RequestException as e:
        print(f"请求失败: {e}")
        return None


def beautifulhtml(url):
    try:
        r = requests.get(url)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        soup = BeautifulSoup(r.text, 'html.parser')
        return soup.a.attrs.get('id')
    except requests.exceptions.RequestException as e:
        print(f"请求失败: {e}")
        return None



def main():
    # url = "https://www.baidu.com"
    # key = {"wd": "vscode"}
    # url = "http://www.so.com/s"
    # key = {"q": "vscode"}
    # html = gethtml(url, key)
    # writetxt(html, "b19.txt")
    # picurl = "https://h2.gifposter.com/bingImages/BeckettBridge_1920x1080.jpg"
    # path = "./pics//"
    # getpic(picurl, path)
    url = "https://python123.io/ws/demo.html"
    print(beautifulhtml(url))
    # ip = "111.22.39.255"
    # print(reip(ip))
    print("sucess")


if __name__ == '__main__':
    main()
