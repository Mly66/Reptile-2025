import re

def basic_regex_demo():
    # 1. 基本匹配
    pattern = r'hello'
    text = 'hello world'
    match = re.search(pattern, text)
    print(f"基本匹配结果: {match.group() if match else '未匹配'}")

    # 2. 字符集
    pattern = r'[a-z]+'
    text = 'Hello123World'
    matches = re.findall(pattern, text)
    print(f"字符集匹配结果: {matches}")

    # 3. 数量词
    pattern = r'\d{3,4}'
    text = '电话：1234-5678'
    matches = re.findall(pattern, text)
    print(f"数量词匹配结果: {matches}")

    # 4. 边界匹配
    pattern = r'^hello'
    text = 'hello world'
    match = re.search(pattern, text)
    print(f"边界匹配结果: {match.group() if match else '未匹配'}")

if __name__ == '__main__':
    basic_regex_demo() 