import re

def regex_syntax_demo():
    # 1. 元字符示例
    text = "Python3.9 is awesome!"
    pattern = r'\w+'  # 匹配单词字符
    matches = re.findall(pattern, text)
    print(f"元字符匹配结果: {matches}")

    # 2. 特殊序列
    text = "价格: $99.99"
    pattern = r'\$\d+\.\d+'  # 匹配价格
    match = re.search(pattern, text)
    print(f"特殊序列匹配结果: {match.group() if match else '未匹配'}")

    # 3. 分组
    text = "姓名: 张三, 年龄: 25"
    pattern = r'姓名: (\w+), 年龄: (\d+)'
    match = re.search(pattern, text)
    if match:
        print(f"分组匹配结果: 姓名={match.group(1)}, 年龄={match.group(2)}")

    # 4. 命名分组
    text = "邮箱: example@domain.com"
    pattern = r'(?P<username>\w+)@(?P<domain>\w+\.\w+)'
    match = re.search(pattern, text)
    if match:
        print(f"命名分组匹配结果: 用户名={match.group('username')}, 域名={match.group('domain')}")

if __name__ == '__main__':
    regex_syntax_demo() 