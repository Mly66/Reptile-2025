import re

def re_functions_demo():
    text = "Python3.9 is awesome! Python is easy to learn. Python is powerful."

    # 1. re.search() - 查找第一个匹配
    print("1. re.search() 示例:")
    pattern = r'Python'
    match = re.search(pattern, text)
    if match:
        print(f"找到匹配: {match.group()}")
        print(f"匹配位置: {match.start()}-{match.end()}")

    # 2. re.findall() - 查找所有匹配
    print("\n2. re.findall() 示例:")
    matches = re.findall(pattern, text)
    print(f"所有匹配: {matches}")

    # 3. re.finditer() - 返回迭代器
    print("\n3. re.finditer() 示例:")
    for match in re.finditer(pattern, text):
        print(f"匹配: {match.group()}, 位置: {match.start()}-{match.end()}")

    # 4. re.sub() - 替换
    print("\n4. re.sub() 示例:")
    new_text = re.sub(pattern, 'Java', text)
    print(f"替换后: {new_text}")

    # 5. re.split() - 分割
    print("\n5. re.split() 示例:")
    parts = re.split(r'[.!]', text)
    print(f"分割结果: {parts}")

    # 6. re.compile() - 编译正则表达式
    print("\n6. re.compile() 示例:")
    compiled_pattern = re.compile(pattern)
    matches = compiled_pattern.findall(text)
    print(f"编译后查找所有匹配: {matches}")

    # 7. re.match() - 从字符串开始处匹配
    print("\n7. re.match() 示例:")
    match = re.match(pattern, text)
    if match:
        print(f"开头匹配: {match.group()}")
    else:
        print("开头不匹配")

if __name__ == '__main__':
    re_functions_demo() 