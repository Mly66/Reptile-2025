"""
Scrapy爬虫常用命令示例

1. 创建项目
scrapy startproject project_name

2. 创建爬虫
scrapy genspider spider_name domain.com

3. 运行爬虫
scrapy crawl spider_name

4. 检查爬虫
scrapy check spider_name

5. 列出所有爬虫
scrapy list

6. 使用shell调试
scrapy shell url

7. 查看可用命令
scrapy -h

8. 导出数据
scrapy crawl spider_name -o output.json
scrapy crawl spider_name -o output.csv

9. 设置日志级别
scrapy crawl spider_name --loglevel=INFO

10. 设置并发请求数
scrapy crawl spider_name -s CONCURRENT_REQUESTS=16

11. 设置下载延迟
scrapy crawl spider_name -s DOWNLOAD_DELAY=1

12. 使用自定义设置文件
scrapy crawl spider_name -s settings_file=my_settings.py

13. 运行爬虫并保存日志
scrapy crawl spider_name --logfile=spider.log

14. 使用代理
scrapy crawl spider_name -s HTTP_PROXY=http://proxy.example.com:8080

15. 设置User-Agent
scrapy crawl spider_name -s USER_AGENT='Mozilla/5.0 ...'
"""

def print_commands():
    """打印常用命令说明"""
    commands = {
        "创建项目": "scrapy startproject project_name",
        "创建爬虫": "scrapy genspider spider_name domain.com",
        "运行爬虫": "scrapy crawl spider_name",
        "检查爬虫": "scrapy check spider_name",
        "列出爬虫": "scrapy list",
        "调试shell": "scrapy shell url",
        "查看帮助": "scrapy -h",
        "导出数据": "scrapy crawl spider_name -o output.json",
        "设置日志": "scrapy crawl spider_name --loglevel=INFO",
        "并发请求": "scrapy crawl spider_name -s CONCURRENT_REQUESTS=16",
        "下载延迟": "scrapy crawl spider_name -s DOWNLOAD_DELAY=1",
        "自定义设置": "scrapy crawl spider_name -s settings_file=my_settings.py",
        "保存日志": "scrapy crawl spider_name --logfile=spider.log",
        "使用代理": "scrapy crawl spider_name -s HTTP_PROXY=http://proxy.example.com:8080",
        "设置UA": "scrapy crawl spider_name -s USER_AGENT='Mozilla/5.0 ...'"
    }
    
    print("Scrapy爬虫常用命令：\n")
    for desc, cmd in commands.items():
        print(f"{desc}:")
        print(f"  {cmd}\n")

if __name__ == '__main__':
    print_commands() 