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
    
    # 选取一个标签作为起始点
    start_tag = soup.a
    print("起始标签:", start_tag)
    
    # 1. 获取父节点
    print("\n父节点:")
    print(start_tag.parent)
    
    # 2. 获取所有父节点 (遍历祖先节点)
    print("\n所有祖先节点:")
    for parent in start_tag.parents:
        if parent is None:
            print("None")
        else:
            print(parent.name)

    # 3. 使用.parent属性进行逐级上行遍历
    print("\n逐级上行遍历:")
    current = start_tag
    while current.parent:
        current = current.parent
        print(current.name) 