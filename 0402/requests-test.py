import requests
def test():
    # url = 'http://httpbin.org/'
    # re = requests.post(url + 'post', data='nbmly')
    # url = "https://www.baidu.com/s"
    url = "http://www.so.com/s"
    key = {"q": "vscode"}
    r = requests.get(url, params=key)
    print(r.status_code)
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    print(str(len(r.text)))

def reip(ip):
    url = "https://www.ipshudi.com/"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"
    }

    try:
        r = requests.get(url + ip + ".htm", headers=headers, timeout=10)
        r.raise_for_status() 
        r.encoding = r.apparent_encoding
        return r.text
    except requests.exceptions.RequestException as e:
        print(f"请求失败: {e}")
        return None

def jd():
    url = "http://www.amzon.com"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"
    }
    r = requests.get(url,headers=headers)
    print(r.status_code)
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    return r.text[:500]
def main():
    ip = "121.26.132.5"
    # print(reip(ip))
    print(jd())
if __name__ == '__main__':
    main()