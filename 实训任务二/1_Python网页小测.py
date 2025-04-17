import requests
from bs4 import BeautifulSoup

def getHTMLText(url):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return "产生异常"

if __name__ == "__main__":
    url = "http://python123.io/ws/demo.html"
    html = getHTMLText(url)
    
    # 使用BeautifulSoup解析HTML
    soup = BeautifulSoup(html, "html.parser")
    
    # 打印解析后的HTML
    print(soup.prettify())
    
    # 获取所有标签
    print("\n所有标签:")
    for tag in soup.find_all():
        print(tag.name)
    
    # 获取title标签
    print("\nTitle标签:")
    print(soup.title)
    
    # 获取a标签
    print("\nA标签:")
    print(soup.a)
    
    # 获取a标签的属性
    print("\nA标签的属性:")
    print(soup.a.attrs)
    
    # 获取a标签的内容
    print("\nA标签的内容:")
    print(soup.a.string)
    
    # 获取a标签的父标签
    print("\nA标签的父标签:")
    print(soup.a.parent.name)
    
    # 获取所有a标签的链接
    print("\n所有A标签的链接:")
    for link in soup.find_all('a'):
        print(link.get('href')) 