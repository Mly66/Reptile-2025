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
    start_tag = soup.body
    print("起始标签:", start_tag.name)
    
    # 1. 获取直接子节点 - 只获取Tag类型
    print("\n直接子节点（仅Tag类型）:")
    for child in start_tag.children:
        if child.name:  # 过滤掉NavigableString类型
            print(child.name)
    
    # 2. 获取所有子孙节点
    print("\n所有子孙节点:")
    for descendant in start_tag.descendants:
        if descendant.name:  # 过滤掉NavigableString类型
            print(descendant.name)
    
    # 3. 获取直接子节点（包括文本节点）
    print("\n直接子节点（包括文本节点）:")
    for child in start_tag.children:
        if child.name:
            print(f"Tag: {child.name}")
        else:
            # 如果是文本节点且不只是空白
            text = child.strip()
            if text:
                print(f"Text: {text}") 