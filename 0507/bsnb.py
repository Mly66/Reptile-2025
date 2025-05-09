import requests
import re


def get_js_code(url):
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36'
        }
        response = requests.get(url.strip(), headers=headers, timeout=10)
        response.raise_for_status()
        return response.text
    except Exception as e:
        print(f"获取JS文件失败: {str(e)}")
        return None


def extract_webpack_module(js_code, module_id):
    try:
        # 使用双花括号转义正则中的特殊符号
        pattern = re.compile(
            rf"{module_id}\s*:\s*\([a-z,\s]*\)\s*=>\s*\{{(.*?)\}}\s*[,}}]",
            re.DOTALL | re.IGNORECASE
        )

        match = pattern.search(js_code)
        if not match:
            # 压缩格式的匹配也需要转义
            pattern = re.compile(rf"{re.escape(module_id)}:\([a-z,]+\)=>\{{(.*?)\}}[,}}]", re.DOTALL)
            match = pattern.search(js_code)


        if match:
            content = match.group(0)

            # 精确截取模块边界
            start = content.find('{')
            end = content.rfind('}') + 1
            clean_content = content[start:end]

            # 保留原始缩进格式
            return clean_content.strip()
        return None

    except Exception as e:
        print(f"解析出错: {str(e)}")
        return None


if __name__ == "__main__":
    js_url = "https://mly66.github.io/blog/assets/js/app.5fce592d.js"
    module_id = "7877"

    js_content = get_js_code(js_url)
    # print(js_content)
    if js_content:
        module_code = extract_webpack_module(js_content, module_id)
        if module_code:
            print("成功提取模块内容：")
            print(module_code)
        else:
            print("未找到指定模块")