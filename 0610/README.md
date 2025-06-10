# 正则表达式实训项目

本项目包含了多个正则表达式相关的示例和实战练习，涵盖了从基础到高级的各种应用场景。

## 项目结构

1. `01_regex_basic.py` - 正则表达式基本使用示例
2. `02_regex_syntax.py` - 正则表达式语法实例
3. `03_regex_classic.py` - 经典正则表达式实例
4. `04_regex_ip.py` - IP地址匹配示例
5. `05_re_functions.py` - Re库主要函数实例
6. `06_match_object.py` - Match对象属性和方法示例
7. `07_greedy_non_greedy.py` - 贪婪匹配和最小匹配示例
8. `08_taobao_crawler.py` - 淘宝商品比价定向爬虫
9. `09_stock_crawler.py` - 股票数据定向爬虫

## 环境要求

- Python 3.7+
- 依赖包：见 requirements.txt

## 安装依赖

```bash
pip install -r requirements.txt
```

## 使用说明

1. 基础示例（1-7）：
   - 直接运行对应的Python文件即可查看示例效果
   - 例如：`python 01_regex_basic.py`

2. 淘宝商品爬虫：
   - 运行：`python 08_taobao_crawler.py`
   - 输入要搜索的商品关键词
   - 结果将保存为CSV文件

3. 股票数据爬虫：
   - 运行：`python 09_stock_crawler.py`
   - 自动爬取股票数据
   - 结果将保存为CSV文件

## 注意事项

1. 爬虫程序使用时请注意：
   - 遵守网站的robots.txt规则
   - 控制爬取频率，避免对目标网站造成压力
   - 仅用于学习和研究目的

2. 正则表达式示例：
   - 每个示例都包含详细的注释
   - 可以根据需要修改示例代码进行测试

## 学习建议

1. 按顺序学习，从基础示例开始
2. 动手实践，修改示例代码
3. 理解每个正则表达式的含义
4. 注意观察贪婪匹配和最小匹配的区别
5. 结合实际应用场景进行练习 