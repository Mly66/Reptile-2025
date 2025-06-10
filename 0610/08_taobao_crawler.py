import requests
import re
import time
import random
from bs4 import BeautifulSoup

class TaobaoCrawler:
    def __init__(self):
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
        }
        self.base_url = 'https://s.taobao.com/search'
        
    def get_page(self, keyword, page=1):
        """获取搜索页面内容"""
        params = {
            'q': keyword,
            's': (page - 1) * 44  # 淘宝每页44个商品
        }
        
        try:
            response = requests.get(self.base_url, params=params, headers=self.headers)
            response.raise_for_status()
            return response.text
        except Exception as e:
            print(f"获取页面失败: {e}")
            return None

    def parse_product(self, html):
        """解析商品信息"""
        if not html:
            return []
        
        # 使用正则表达式提取商品信息
        # 注意：实际使用时需要根据淘宝页面的具体结构调整正则表达式
        pattern = r'"raw_title":"([^"]+)","view_price":"([^"]+)"'
        matches = re.findall(pattern, html)
        
        products = []
        for title, price in matches:
            products.append({
                'title': title,
                'price': price
            })
        
        return products

    def crawl(self, keyword, pages=3):
        """爬取指定页数的商品信息"""
        all_products = []
        
        for page in range(1, pages + 1):
            print(f"正在爬取第 {page} 页...")
            html = self.get_page(keyword, page)
            products = self.parse_product(html)
            all_products.extend(products)
            
            # 添加随机延迟，避免被封
            time.sleep(random.uniform(1, 3))
        
        return all_products

    def save_to_file(self, products, filename):
        """保存商品信息到文件"""
        with open(filename, 'w', encoding='utf-8') as f:
            f.write("商品名称,价格\n")
            for product in products:
                f.write(f"{product['title']},{product['price']}\n")

def main():
    # 创建爬虫实例
    crawler = TaobaoCrawler()
    
    # 设置搜索关键词
    keyword = input("请输入要搜索的商品关键词: ")
    
    # 爬取商品信息
    print(f"开始爬取 {keyword} 的商品信息...")
    products = crawler.crawl(keyword)
    
    # 保存结果
    filename = f"{keyword}_products.csv"
    crawler.save_to_file(products, filename)
    
    print(f"\n爬取完成！共获取 {len(products)} 个商品信息")
    print(f"结果已保存到文件: {filename}")
    
    # 显示部分结果
    print("\n部分商品信息预览:")
    for i, product in enumerate(products[:5], 1):
        print(f"{i}. {product['title']} - ¥{product['price']}")

if __name__ == '__main__':
    main() 