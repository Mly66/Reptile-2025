import json
import xml.dom.minidom
import yaml
import requests
from bs4 import BeautifulSoup

# 示例数据 - 中国部分省份及其首府
china_provinces = {
    "provinces": [
        {"name": "北京", "capital": "北京市"},
        {"name": "上海", "capital": "上海市"},
        {"name": "广东", "capital": "广州市"},
        {"name": "四川", "capital": "成都市"}
    ]
}

def xml_demo():
    # 创建XML文档
    doc = xml.dom.minidom.getDOMImplementation().createDocument(None, "China", None)
    root = doc.documentElement
    
    # 添加省份信息
    for province in china_provinces["provinces"]:
        province_element = doc.createElement("Province")
        
        # 添加省份名称
        name_element = doc.createElement("Name")
        name_text = doc.createTextNode(province["name"])
        name_element.appendChild(name_text)
        
        # 将省份元素添加到根元素
        province_element.appendChild(name_element)
        
        # 将省份元素添加到根元素
        root.appendChild(province_element)
    
    return doc.toprettyxml(indent="  ")

def json_demo():
    # 转换为JSON
    return json.dumps(china_provinces, ensure_ascii=False, indent=2)

def yaml_demo():
    # 转换为YAML
    return yaml.dump(china_provinces, allow_unicode=True, sort_keys=False)

def html_to_structured_data():
    # 抓取HTML页面
    url = "http://python123.io/ws/demo.html"
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        html = r.text
    except:
        return None
    
    # 使用BeautifulSoup解析HTML
    soup = BeautifulSoup(html, "html.parser")
    
    # 提取信息并转换为结构化数据
    data = {
        "title": soup.title.string if soup.title else "",
        "links": [{"text": link.string if link.string else "", "href": link.get('href', "")} 
                 for link in soup.find_all('a')]
    }
    
    return json.dumps(data, ensure_ascii=False, indent=2)

if __name__ == "__main__":
    print(xml_demo())
    print(json_demo())
    print(yaml_demo())
    print(html_to_structured_d
    ata())