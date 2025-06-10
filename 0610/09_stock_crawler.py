import requests
import re
import time
import json
from bs4 import BeautifulSoup
import pandas as pd

class StockCrawler:
    def __init__(self):
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
        }
        # 东方财富网股票列表接口
        self.stock_list_url = 'http://quote.eastmoney.com/stocklist.html'
        # 百度股票接口
        self.stock_info_url = 'https://gupiao.baidu.com/stock/'
        
    def get_stock_list(self):
        """获取股票列表"""
        try:
            response = requests.get(self.stock_list_url, headers=self.headers)
            response.raise_for_status()
            response.encoding = 'gbk'
            
            # 使用正则表达式提取股票代码和名称
            pattern = r'<li><a target="_blank" href="http://quote.eastmoney.com/([^"]+)">([^(]+)\(([^)]+)\)</a></li>'
            matches = re.findall(pattern, response.text)
            
            stocks = []
            for _, name, code in matches:
                # 只保留上海和深圳的股票
                if code.startswith(('sh', 'sz')):
                    stocks.append({
                        'name': name.strip(),
                        'code': code
                    })
            
            return stocks
        except Exception as e:
            print(f"获取股票列表失败: {e}")
            return []

    def get_stock_info(self, stock_code):
        """获取单个股票信息"""
        try:
            url = f"{self.stock_info_url}{stock_code}.html"
            response = requests.get(url, headers=self.headers)
            response.raise_for_status()
            
            # 使用正则表达式提取股票信息
            # 注意：实际使用时需要根据百度股票页面的具体结构调整正则表达式
            price_pattern = r'<strong class="_close">([^<]+)</strong>'
            change_pattern = r'<span class="_change">([^<]+)</span>'
            
            price_match = re.search(price_pattern, response.text)
            change_match = re.search(change_pattern, response.text)
            
            return {
                'price': price_match.group(1) if price_match else 'N/A',
                'change': change_match.group(1) if change_match else 'N/A'
            }
        except Exception as e:
            print(f"获取股票 {stock_code} 信息失败: {e}")
            return {'price': 'N/A', 'change': 'N/A'}

    def crawl(self):
        """爬取所有股票信息"""
        print("开始获取股票列表...")
        stocks = self.get_stock_list()
        
        print(f"共找到 {len(stocks)} 只股票，开始获取详细信息...")
        stock_data = []
        
        for i, stock in enumerate(stocks, 1):
            print(f"正在获取第 {i}/{len(stocks)} 只股票信息: {stock['name']}({stock['code']})")
            info = self.get_stock_info(stock['code'])
            
            stock_data.append({
                'code': stock['code'],
                'name': stock['name'],
                'price': info['price'],
                'change': info['change']
            })
            
            # 添加延迟，避免被封
            time.sleep(1)
        
        return stock_data

    def save_to_file(self, stock_data, filename):
        """保存股票信息到文件"""
        df = pd.DataFrame(stock_data)
        df.to_csv(filename, index=False, encoding='utf-8-sig')

def main():
    # 创建爬虫实例
    crawler = StockCrawler()
    
    # 爬取股票信息
    stock_data = crawler.crawl()
    
    # 保存结果
    filename = 'stock_data.csv'
    crawler.save_to_file(stock_data, filename)
    
    print(f"\n爬取完成！共获取 {len(stock_data)} 只股票信息")
    print(f"结果已保存到文件: {filename}")
    
    # 显示部分结果
    print("\n部分股票信息预览:")
    for i, stock in enumerate(stock_data[:5], 1):
        print(f"{i}. {stock['name']}({stock['code']}) - 价格: {stock['price']}, 涨跌幅: {stock['change']}")

if __name__ == '__main__':
    main() 