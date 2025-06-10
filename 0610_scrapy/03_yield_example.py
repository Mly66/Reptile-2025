"""
yield关键字使用示例
"""

def fibonacci(n):
    """生成斐波那契数列"""
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

def parse_html(html):
    """模拟解析HTML，使用yield返回解析结果"""
    # 模拟HTML内容
    lines = html.split('\n')
    for line in lines:
        if '<p>' in line:
            yield line.strip()
        elif '<a href=' in line:
            yield line.strip()

def main():
    print("1. 斐波那契数列生成器示例:")
    print("前10个斐波那契数:")
    for num in fibonacci(10):
        print(num, end=' ')
    print("\n")

    print("2. HTML解析示例:")
    # 模拟HTML内容
    html = """
    <html>
        <body>
            <p>这是第一段</p>
            <a href="http://example.com">链接1</a>
            <p>这是第二段</p>
            <a href="http://example.org">链接2</a>
        </body>
    </html>
    """
    
    print("提取的标签:")
    for tag in parse_html(html):
        print(tag)

    print("\n3. 生成器表达式示例:")
    # 使用生成器表达式
    numbers = (x * x for x in range(5))
    print("平方数:", list(numbers))

if __name__ == '__main__':
    main() 