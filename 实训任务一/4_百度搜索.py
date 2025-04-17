import requests

def getHTMLText(url, params=None, headers=None):
    try:
        r = requests.get(url, params=params, headers=headers, timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return "产生异常"

if __name__ == "__main__":
    keyword = "Python"
    url = "https://www.baidu.com/s"
    params = {
        'wd': keyword
    }
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36"
    }
    html = getHTMLText(url, params, headers)
    print(len(html))
    print(html[:1000])  # 打印前1000个字符 