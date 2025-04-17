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
    
    # 使用prettify()方法格式化输出整个HTML文档
    print("格式化输出整个HTML文档:")
    print(soup.prettify())
    
    # 使用prettify()方法格式化输出特定标签
    print("\n格式化输出body标签:")
    print(soup.body.prettify())
    
    # 使用prettify()方法格式化输出自定义HTML片段
    custom_html = BeautifulSoup("<p>这是<b>一个</b>示例</p>", "html.parser")
    print("\n格式化输出自定义HTML片段:")
    print(custom_html.prettify())
    
    # 创建一个新标签并格式化输出
    new_tag = soup.new_tag("div")
    new_tag.string = "这是一个新的div标签"
    
    print("\n格式化输出新创建的标签:")
    print(new_tag.prettify()) 