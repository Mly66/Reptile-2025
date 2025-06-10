import re

def ip_regex_demo():
    # IP地址匹配模式
    ip_pattern = r'^(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$'

    # 测试用例
    test_ips = [
        '192.168.1.1',
        '10.0.0.1',
        '172.16.0.1',
        '256.1.2.3',  # 无效IP
        '1.1.1.1.1',  # 无效IP
        '192.168.001.1',  # 无效IP
        '0.0.0.0',
        '255.255.255.255'
    ]

    print("IP地址验证测试:")
    for ip in test_ips:
        is_valid = bool(re.match(ip_pattern, ip))
        print(f"{ip}: {'有效' if is_valid else '无效'}")

    # 从文本中提取IP地址
    text = """
    服务器IP地址: 192.168.1.100
    备用服务器: 10.0.0.1
    测试服务器: 172.16.0.1
    无效IP: 256.1.2.3
    """
    
    # 提取IP地址的模式（不要求完全匹配）
    extract_pattern = r'\b(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\b'
    
    print("\n从文本中提取IP地址:")
    found_ips = re.findall(extract_pattern, text)
    for ip in found_ips:
        print(f"找到IP: {ip}")

if __name__ == '__main__':
    ip_regex_demo() 