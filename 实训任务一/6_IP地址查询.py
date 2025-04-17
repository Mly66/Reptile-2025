import requests

def get_ip_info(ip):
    """
    查询IP地址的归属地信息
    :param ip: IP地址
    :return: IP归属地信息
    """
    url = f"https://ip.taobao.com/outGetIpInfo"
    params = {
        "ip": ip,
        "accessKey": "alibaba-inc"
    }
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36"
    }
    try:
        r = requests.get(url, params=params, headers=headers, timeout=30)
        r.raise_for_status()
        result = r.json()
        
        if result["data"]:
            data = result["data"]
            return {
                "ip": data["ip"],
                "country": data["country"],
                "region": data["region"],
                "city": data["city"],
                "isp": data["isp"]
            }
        else:
            return "未查询到IP信息"
    except Exception as e:
        return f"查询失败：{e}"

if __name__ == "__main__":
    # 要查询的IP地址
    ip_address = "8.8.8.8"  # 谷歌DNS服务器IP
    
    # 获取IP信息
    ip_info = get_ip_info(ip_address)
    
    # 显示结果
    if isinstance(ip_info, dict):
        print(f"IP: {ip_info['ip']}")
        print(f"国家: {ip_info['country']}")
        print(f"地区: {ip_info['region']}")
        print(f"城市: {ip_info['city']}")
        print(f"ISP: {ip_info['isp']}")
    else:
        print(ip_info) 