import re

def match_object_demo():
    # 准备测试文本
    text = "姓名: 张三, 年龄: 25, 邮箱: zhangsan@example.com"
    
    # 使用命名分组创建模式
    pattern = r'姓名: (?P<name>\w+), 年龄: (?P<age>\d+), 邮箱: (?P<email>[\w.]+@[\w.]+)'
    
    # 执行匹配
    match = re.search(pattern, text)
    
    if match:
        print("1. 基本属性:")
        print(f"匹配的字符串: {match.group()}")
        print(f"匹配的起始位置: {match.start()}")
        print(f"匹配的结束位置: {match.end()}")
        print(f"匹配的跨度: {match.span()}")
        
        print("\n2. 分组访问:")
        print(f"第一个分组: {match.group(1)}")
        print(f"第二个分组: {match.group(2)}")
        print(f"第三个分组: {match.group(3)}")
        
        print("\n3. 命名分组访问:")
        print(f"姓名: {match.group('name')}")
        print(f"年龄: {match.group('age')}")
        print(f"邮箱: {match.group('email')}")
        
        print("\n4. 分组位置信息:")
        print(f"第一个分组位置: {match.start(1)}-{match.end(1)}")
        print(f"第二个分组位置: {match.start(2)}-{match.end(2)}")
        print(f"第三个分组位置: {match.start(3)}-{match.end(3)}")
        
        print("\n5. 所有分组:")
        print(f"所有分组: {match.groups()}")
        
        print("\n6. 分组字典:")
        print(f"分组字典: {match.groupdict()}")
        
        print("\n7. 正则表达式对象:")
        print(f"使用的模式: {match.re.pattern}")
        
        print("\n8. 原始字符串:")
        print(f"原始字符串: {match.string}")
    else:
        print("未找到匹配")

if __name__ == '__main__':
    match_object_demo() 