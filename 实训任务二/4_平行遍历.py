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
    start_tag = soup.find('p')  # 以p标签为起始点
    print("起始标签:", start_tag)
    
    # 1. 获取后一个兄弟节点标签
    print("\n后一个兄弟节点标签:")
    print(start_tag.next_sibling)  # 可能是空白字符
    
    # 寻找真正的后一个兄弟节点标签（跳过NavigableString）
    next_tag = start_tag.next_sibling
    while next_tag and not next_tag.name:
        next_tag = next_tag.next_sibling
    print("真正的后一个兄弟节点标签:", next_tag)
    
    # 2. 获取前一个兄弟节点标签
    print("\n前一个兄弟节点标签:")
    print(start_tag.previous_sibling)  # 可能是空白字符
    
    # 寻找真正的前一个兄弟节点标签（跳过NavigableString）
    prev_tag = start_tag.previous_sibling
    while prev_tag and not prev_tag.name:
        prev_tag = prev_tag.previous_sibling
    print("真正的前一个兄弟节点标签:", prev_tag)
    
    # 3. 获取所有后续兄弟节点标签
    print("\n所有后续兄弟节点标签:")
    for sibling in start_tag.next_siblings:
        if sibling.name:
            print(sibling.name)
    
    # 4. 获取所有前面兄弟节点标签
    print("\n所有前面兄弟节点标签:")
    for sibling in start_tag.previous_siblings:
        if sibling.name:
            print(sibling.name) 