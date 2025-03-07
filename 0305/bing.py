import requests
import json
import os
from datetime import datetime

# 设置请求头
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36",
    "Connection": "close",
    'Content-Type': "application/json",
}

# 获取图片信息
def get_image_info():
    # Bing 的每日图片 API
    api_url = "https://www.bing.com/HPImageArchive.aspx?format=js&idx=0&n=1&mkt=zh-CN"
    response = requests.get(api_url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        image_info = data['images'][0]
        image_url = "https://www.bing.com/" + image_info['url']
        image_title = image_info['title']
        return image_url, image_title
    else:
        print("获取图片信息失败")
        return None, None

# 下载图片
def download_image(url, save_path):
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        with open(save_path, 'wb') as f:
            f.write(response.content)
        print(f"图片已保存至 {save_path}")
    else:
        print("下载图片失败")

# 主函数
def main():
    image_url, image_title = get_image_info()
    if image_url and image_title:
        # 创建保存目录
        folder_name = 'bing_images'
        if not os.path.exists(folder_name):
            os.makedirs(folder_name)
        # 设置保存路径和文件名
        date_str = datetime.now().strftime("%Y-%m-%d")
        file_name = f"{date_str}_{image_title}.jpg"
        save_path = os.path.join(folder_name, file_name)
        # 下载图片
        download_image(image_url, save_path)
    else:
        print("未能获取图片信息")

if __name__ == "__main__":
    main()