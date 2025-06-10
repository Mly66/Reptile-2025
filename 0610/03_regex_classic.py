import re

def classic_regex_demo():
    # 1. 邮箱验证
    def validate_email(email):
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return bool(re.match(pattern, email))

    # 2. 手机号验证
    def validate_phone(phone):
        pattern = r'^1[3-9]\d{9}$'
        return bool(re.match(pattern, phone))

    # 3. 身份证号验证
    def validate_id_card(id_card):
        pattern = r'^\d{17}[\dXx]$'
        return bool(re.match(pattern, id_card))

    # 4. URL验证
    def validate_url(url):
        pattern = r'^https?://(?:[\w-]+\.)+[\w-]+(?:/[\w-./?%&=]*)?$'
        return bool(re.match(pattern, url))

    # 测试示例
    test_cases = {
        '邮箱': [
            'test@example.com',
            'invalid.email@',
            'user.name@domain.co.uk'
        ],
        '手机号': [
            '13812345678',
            '12345678901',
            '1381234567'
        ],
        '身份证': [
            '110101199001011234',
            '11010119900101123X',
            '123456789'
        ],
        'URL': [
            'https://www.example.com',
            'http://sub.example.com/path',
            'invalid://url'
        ]
    }

    for category, cases in test_cases.items():
        print(f"\n{category}验证测试:")
        for case in cases:
            if category == '邮箱':
                result = validate_email(case)
            elif category == '手机号':
                result = validate_phone(case)
            elif category == '身份证':
                result = validate_id_card(case)
            else:
                result = validate_url(case)
            print(f"{case}: {'有效' if result else '无效'}")

if __name__ == '__main__':
    classic_regex_demo() 