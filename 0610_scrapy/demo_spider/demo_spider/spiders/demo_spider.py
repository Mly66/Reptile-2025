import scrapy

class DemoSpider(scrapy.Spider):
    name = 'demo'
    allowed_domains = ['python123.io']
    start_urls = ['http://python123.io/ws/demo.html']

    def parse(self, response):
        # 提取所有p标签的文本
        p_texts = response.css('p::text').getall()
        print("p标签文本:", p_texts)
        
        # 提取所有a标签的href属性
        a_links = response.css('a::attr(href)').getall()
        print("a标签链接:", a_links)
        
        # 提取所有a标签的文本
        a_texts = response.css('a::text').getall()
        print("a标签文本:", a_texts)
        
        # 使用XPath提取
        p_texts_xpath = response.xpath('//p/text()').getall()
        print("XPath提取p标签文本:", p_texts_xpath)
        
        # 提取所有标签
        all_tags = response.css('*::text').getall()
        print("所有标签文本:", all_tags)
        
        # 返回提取的数据
        yield {
            'p_texts': p_texts,
            'a_links': a_links,
            'a_texts': a_texts,
            'all_tags': all_tags
        } 