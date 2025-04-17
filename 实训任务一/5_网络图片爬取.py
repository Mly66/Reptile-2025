import requests
import os

def download_image(url, save_path):
    """
    下载网络图片并保存
    :param url: 图片URL
    :param save_path: 保存路径
    :return: None
    """
    try:
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36"
        }
        r = requests.get(url, headers=headers, timeout=30)
        r.raise_for_status()
        
        # 方法一：使用with语句
        with open(save_path, 'wb') as f:
            f.write(r.content)
        print(f"图片已保存至 {save_path}")
        
        # 方法二：使用try...finally语句
        '''
        f = open(save_path, 'wb')
        try:
            f.write(r.content)
            print(f"图片已保存至 {save_path}")
        finally:
            f.close()
        '''
        
    except Exception as e:
        print(f"下载失败：{e}")

if __name__ == "__main__":
    # 创建保存图片的文件夹
    img_dir = "images"
    if not os.path.exists(img_dir):
        os.makedirs(img_dir)
    
    # 图片URL
    img_url = "https://www.python.org/static/img/python-logo.png"
    
    # 保存路径
    save_path = os.path.join(img_dir, "python-logo.png")
    
    # 下载并保存图片
    download_image(img_url, save_path) 