import os
import requests

def gethtml(url, key):
    try:
        r = requests.get(url, params=key)
        print(r.status_code)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        print("error")
        return None
    finally:
        print("success")

def getTxt(txt, filename):
    if os.path.exists(filename):
        print(f"{filename} 已经存在，将会被覆盖")

    folder = os.path.dirname(filename)
    if folder and not os.path.exists(folder):
        os.makedirs(folder)

    with open(filename, 'w', encoding="utf-8") as f:
        print(f"正在写入 {filename}")
        f.write("获取网页内容如下\n")
        f.write(txt)
    print("success")
    return filename


def getpic(url, root):
    path = os.path.join(root, url.split('/')[-1])

    try:
        if not os.path.exists(root):
            os.mkdir(root)
        if not os.path.exists(path):
            r = requests.get(url)
            with open(path, 'wb') as f:
                f.write(r.content)
            print("success")
        else:
            print("文件已存在")
    except:
        print("error")
    finally:
        print("nb")

def getnames(url, key):
    try:
        r = requests.get(url, params=key)
        print(r.status_code)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return str(len(r.text))
    except:
        print("error")
        return None
    finally:
        print("success")

def main():
    url = "http://www.baidu.com/s"
    key = {"wd": "马璐瑶"}
    html = gethtml(url, key)
    getTxt(html, "./output/test.txt")

    picurl = "https://wallpapercave.com/wp/mJRWj5T.jpg"
    path = "./pics/"
    getpic(picurl, path)

    url = "http://www.so.com/s"
    key = {"q": "马璐瑶"}
    getnames(url, key)

if __name__ == '__main__':
    main()
