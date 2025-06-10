import re

def greedy_non_greedy_demo():
    # 测试文本
    text = "<div>第一个div</div><div>第二个div</div><div>第三个div</div>"
    
    print("1. 贪婪匹配示例:")
    # 贪婪匹配 - 匹配最长的可能字符串
    greedy_pattern = r'<div>.*</div>'
    greedy_match = re.search(greedy_pattern, text)
    if greedy_match:
        print(f"贪婪匹配结果: {greedy_match.group()}")
    
    print("\n2. 最小匹配示例:")
    # 最小匹配 - 匹配最短的可能字符串
    non_greedy_pattern = r'<div>.*?</div>'
    non_greedy_matches = re.findall(non_greedy_pattern, text)
    print("最小匹配结果:")
    for match in non_greedy_matches:
        print(f"- {match}")
    
    print("\n3. 更多贪婪匹配示例:")
    text2 = "价格: $100, $200, $300"
    # 贪婪匹配价格
    greedy_price_pattern = r'\$.*\d'
    greedy_price = re.search(greedy_price_pattern, text2)
    if greedy_price:
        print(f"贪婪匹配价格: {greedy_price.group()}")
    
    print("\n4. 更多最小匹配示例:")
    # 最小匹配价格
    non_greedy_price_pattern = r'\$.*?\d'
    non_greedy_prices = re.findall(non_greedy_price_pattern, text2)
    print("最小匹配价格:")
    for price in non_greedy_prices:
        print(f"- {price}")
    
    print("\n5. 实际应用示例 - 提取HTML标签内容:")
    html_text = """
    <h1>标题1</h1>
    <p>段落1</p>
    <h2>标题2</h2>
    <p>段落2</p>
    """
    
    # 使用最小匹配提取所有标签内容
    tag_pattern = r'<[^>]+>(.*?)</[^>]+>'
    tag_contents = re.findall(tag_pattern, html_text)
    print("提取的标签内容:")
    for content in tag_contents:
        print(f"- {content}")

if __name__ == '__main__':
    greedy_non_greedy_demo() 