import requests
from bs4 import BeautifulSoup
import bs4
import re

def getHTMLText(url):
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        r = requests.get(url, headers=headers, timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        print("成功获取网页内容")
        return r.text
    except Exception as e:
        print(f"获取网页失败: {str(e)}")
        return ""

def fillUnivList(ulist, html):
    if not html:
        print("HTML内容为空")
        return
        
    soup = BeautifulSoup(html, "html.parser")
    print("开始解析网页...")
    
    # 尝试不同的表格选择器
    table = soup.find('table', {'class': 'table-striped'})
    if not table:
        print("未找到表格，尝试其他选择器...")
        table = soup.find('table')
    
    if not table:
        print("未找到任何表格")
        return
    
    print("找到表格，开始提取数据...")
    rows = table.find_all('tr')[1:]  # 跳过表头
    print(f"找到 {len(rows)} 行数据")
    
    for tr in rows:
        tds = tr.find_all('td')
        if len(tds) >= 3:
            try:
                rank = int(tds[0].text.strip())
                name = tds[1].text.strip()
                score = float(tds[3].text.strip())
                ulist.append([rank, name, score])
            except Exception as e:
                print(f"处理行数据时出错: {str(e)}")
                continue

def printUnivList(ulist, num):
    if not ulist:
        print("没有获取到任何大学数据")
        return
        
    print("\n中国大学排名（前{}名）".format(num))
    print("{:^10}\t{:^20}\t{:^10}".format("排名", "学校名称", "总分"))
    print("-" * 50)
    
    for i in range(min(num, len(ulist))):
        u = ulist[i]
        print("{:^10}\t{:^20}\t{:^10.1f}".format(u[0], u[1], u[2]))

def main():
    uinfo = []
    url = 'https://www.shanghairanking.cn/rankings/bcur/2025'
    print(f"正在访问: {url}")
    html = getHTMLText(url)
    fillUnivList(uinfo, html)
    printUnivList(uinfo, 10)

if __name__ == '__main__':
    main() 