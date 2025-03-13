import requests


def getHTMLText(url):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        print(r.headers)
        return r.text[:50]
    except requests.exceptions.RequestException     as e:
        return f"产生异常: {e}"


def sum100(n):
    s = 0
    for i in range(1, n + 1):
        s = s + i
    return s


def testPost(key):
    url = 'http://python123.io/ws'
    r = requests.post(url, data={'key': key})
    return r.text



def testPost1(key):
    url = 'http://python123.io/ws'
    r = requests.post(url, data=key)
    return r.text


def requestdemo(base_url):
    response = requests.request('GET', f'{base_url}/request')
    print("REQUEST:", response.status_code, response.json())

    response = requests.get(f'{base_url}/get', params={'key': 'value'})
    print("GET:", response.json())

    response = requests.head(f'{base_url}/head')
    print("HEAD:", response.headers)

    response = requests.post(f'{base_url}/post', data={'data': 'post_data'})
    print("POST:", response.json())

    response = requests.request('PUT', f'{base_url}/put', json={'key': 'new_value'})
    print("PUT:", response.json())

    response = requests.patch(f'{base_url}/patch', data='partial update')
    print("PATCH:", response.json())

    response = requests.delete(f'{base_url}/delete')
    print("DELETE:", response.json())


if __name__ == "__main__":
    url = "https://www.baidu.com"
    print(getHTMLText(url))
    a = 100
    print(f'{"1+2+3+...+"} {a}{"="}', end='')
    print(sum100(a))
    data = {'key': 'key', 'a': 'a', 'b': 'b', 'c': 'c'}
    print(testPost(data))
    data = "test"
    print(testPost1(data))
    # requestdemo("http://127.0.0.1:5000")

    url = "https://www.jd.com"
    print(getHTMLText(url))
