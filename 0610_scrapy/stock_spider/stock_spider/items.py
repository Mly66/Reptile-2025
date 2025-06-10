import scrapy

class StockItem(scrapy.Item):
    # 股票代码
    code = scrapy.Field()
    # 股票名称
    name = scrapy.Field()
    # 当前价格
    price = scrapy.Field()
    # 涨跌幅
    change = scrapy.Field()
    # 成交量
    volume = scrapy.Field()
    # 成交额
    amount = scrapy.Field()
    # 最高价
    high = scrapy.Field()
    # 最低价
    low = scrapy.Field()
    # 开盘价
    open = scrapy.Field()
    # 昨收价
    pre_close = scrapy.Field() 