import os

import requests


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


def main():
    # url = "http://www.baidu.com/s"
    # key = {"wd": "vscode"}
    # url = "http://www.so.com/s"
    # key = {"q": "vscode"}
    # html = gethtml(url, key)
    # writetxt(html, "b19.txt")
    picurl = "https://h2.gifposter.com/bingImages/BeckettBridge_1920x1080.jpg"
    path = "./pics//"
    getpic(picurl, path)
    print("sucess")


if __name__ == '__main__':
    main()
