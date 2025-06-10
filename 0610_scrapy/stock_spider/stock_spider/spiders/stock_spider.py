import scrapy
from ..items import StockItem
import json

class StockSpider(scrapy.Spider):
    name = 'stock'
    allowed_domains = ['eastmoney.com']
    
    # 上海证券交易所股票列表
    sh_url = 'http://quote.eastmoney.com/stocklist.html'
    
    def start_requests(self):
        """开始请求"""
        yield scrapy.Request(
            url=self.sh_url,
            callback=self.parse_stock_list,
            headers={
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
            }
        )
    
    def parse_stock_list(self, response):
        """解析股票列表"""
        # 提取股票代码和名称
        stock_links = response.css('div.quotebody ul li a')
        for link in stock_links:
            href = link.attrib['href']
            if 'sh' in href or 'sz' in href:
                code = href.split('/')[-1].split('.')[0]
                name = link.css('::text').get().split('(')[0].strip()
                
                # 构建股票详情页URL
                detail_url = f'http://quote.eastmoney.com/{code}.html'
                
                yield scrapy.Request(
                    url=detail_url,
                    callback=self.parse_stock_detail,
                    meta={'code': code, 'name': name},
                    headers={
                        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
                    }
                )
    
    def parse_stock_detail(self, response):
        """解析股票详情"""
        item = StockItem()
        
        # 获取股票基本信息
        item['code'] = response.meta['code']
        item['name'] = response.meta['name']
        
        # 提取股票数据
        try:
            # 价格
            item['price'] = response.css('div.stock-info span.price::text').get()
            # 涨跌幅
            item['change'] = response.css('div.stock-info span.change::text').get()
            # 成交量
            item['volume'] = response.css('div.stock-info span.volume::text').get()
            # 成交额
            item['amount'] = response.css('div.stock-info span.amount::text').get()
            # 最高价
            item['high'] = response.css('div.stock-info span.high::text').get()
            # 最低价
            item['low'] = response.css('div.stock-info span.low::text').get()
            # 开盘价
            item['open'] = response.css('div.stock-info span.open::text').get()
            # 昨收价
            item['pre_close'] = response.css('div.stock-info span.pre-close::text').get()
            
            yield item
            
        except Exception as e:
            self.logger.error(f"解析股票 {item['code']} 数据失败: {str(e)}") 