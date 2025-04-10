import requests
from bs4 import BeautifulSoup
import re


def beautifulhtml(url):
    try:
        r = requests.get(url, timeout=10)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        soup = BeautifulSoup(r.text, 'html.parser')
        # return soup.title.string if soup.title else "无标题"
        # soup.a.attrs['class']字典类型
        text = soup.get_text(strip=True)
        return text if text else "无文本"
    except requests.exceptions.RequestException as e:
        print(f"请求失败: {e}")
        return None

def testpost():
    url = 'http://httpbin.org/post'

    data = {
        'students': [
            {'name': '张三', 'age': 18, 'grade': 'A', 'major': '计算机科学'},
            {'name': '李四', 'age': 19, 'grade': 'B', 'major': '电子工程'},
            {'name': '王五', 'age': 20, 'grade': 'A', 'major': '机械工程'},
            {'name': '赵六', 'age': 18, 'grade': 'C', 'major': '数学'},
            {'name': '钱七', 'age': 21, 'grade': 'B', 'major': '物理'}
        ]
    }

    return requests.post(url, data=data)

def main():
    url = "https://python123.io/ws/demo.html"
    title = beautifulhtml(url)
    print(type(title))
    # match = re.search(r'[1-9]\d{5}', "BTI32746329874 TUS96743298756")
    # if match:
    #     print(match.group(0))
    # pat = re.compile(r'[a-z]')
    # math = pat.search(title)
    # if math:
    #     print(math.span())
    # print(f"网页标题: {title}")
    # print(testpost().text)


if __name__ == '__main__':
    main()
