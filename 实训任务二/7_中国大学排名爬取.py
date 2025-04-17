import requests
from bs4 import BeautifulSoup
import bs4
import re

def getHTMLText(url):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ""

def fillUnivList(ulist, html):
    soup = BeautifulSoup(html, "html.parser")
    # 查找包含大学排名信息的表格
    table = soup.find('table', {'class': 'table-striped'})
    if not table:
        return
    
    # 查找表格中所有行
    for tr in table.find_all('tr')[1:]:  # 跳过表头
        # 查找每行中的所有列
        tds = tr.find_all('td')
        if len(tds) >= 3:  # 确保至少有三列（排名、大学名称、总分）
            try:
                rank = int(tds[0].text.strip())
                name = tds[1].text.strip()
                score = float(tds[3].text.strip())
                ulist.append([rank, name, score])
            except:
                continue

def printUnivList(ulist, num):
    # 打印表头
    print("{:^10}\t{:^20}\t{:^10}".format("排名", "学校名称", "总分"))
    print("-" * 50)
    
    # 打印大学排名信息
    for i in range(min(num, len(ulist))):
        u = ulist[i]
        print("{:^10}\t{:^20}\t{:^10.1f}".format(u[0], u[1], u[2]))

def main():
    uinfo = []
    # 中国大学排名网址
    url = 'https://www.shanghairanking.cn/rankings/bcur/2025'
    html = getHTMLText(url)
    fillUnivList(uinfo, html)
    # 打印前10名的大学
    printUnivList(uinfo, 10)

if __name__ == '__main__':
    main() 