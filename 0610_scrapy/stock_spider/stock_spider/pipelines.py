import json
import pandas as pd
from itemadapter import ItemAdapter

class StockPipeline:
    def __init__(self):
        self.file = None
        self.items = []
    
    def open_spider(self, spider):
        """爬虫启动时调用"""
        self.file = open('stock_data.json', 'w', encoding='utf-8')
        self.items = []
    
    def process_item(self, item, spider):
        """处理每个数据项"""
        # 将数据项转换为字典
        item_dict = ItemAdapter(item).asdict()
        self.items.append(item_dict)
        return item
    
    def close_spider(self, spider):
        """爬虫关闭时调用"""
        # 保存为JSON文件
        json.dump(self.items, self.file, ensure_ascii=False, indent=2)
        self.file.close()
        
        # 保存为CSV文件
        df = pd.DataFrame(self.items)
        df.to_csv('stock_data.csv', index=False, encoding='utf-8-sig')
        
        print(f"共爬取 {len(self.items)} 只股票数据")
        print("数据已保存到 stock_data.json 和 stock_data.csv") 