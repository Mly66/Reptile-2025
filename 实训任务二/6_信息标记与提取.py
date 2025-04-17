import json
import xml.dom.minidom
import yaml
import requests
from bs4 import BeautifulSoup

# 示例数据 - 中国部分省份及其首府
china_provinces = {
    "provinces": [
        {"name": "北京", "capital": "北京市", "population": 21893095},
        {"name": "上海", "capital": "上海市", "population": 24870895},
        {"name": "广东", "capital": "广州市", "population": 126010000},
        {"name": "四川", "capital": "成都市", "population": 83410000}
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
        
        # 添加省会
        capital_element = doc.createElement("Capital")
        capital_text = doc.createTextNode(province["capital"])
        capital_element.appendChild(capital_text)
        
        # 添加人口
        population_element = doc.createElement("Population")
        population_text = doc.createTextNode(str(province["population"]))
        population_element.appendChild(population_text)
        
        # 将所有元素添加到省份元素
        province_element.appendChild(name_element)
        province_element.appendChild(capital_element)
        province_element.appendChild(population_element)
        
        # 将省份元素添加到根元素
        root.appendChild(province_element)
    
    # 打印XML
    print("XML格式:")
    print(doc.toprettyxml(indent="  "))
    
    # XML解析示例
    print("\nXML解析示例:")
    provinces = doc.getElementsByTagName("Province")
    for province in provinces:
        name = province.getElementsByTagName("Name")[0].firstChild.data
        capital = province.getElementsByTagName("Capital")[0].firstChild.data
        print(f"{name}的省会是{capital}")

def json_demo():
    # 转换为JSON
    json_str = json.dumps(china_provinces, ensure_ascii=False, indent=2)
    
    # 打印JSON
    print("\nJSON格式:")
    print(json_str)
    
    # JSON解析示例
    print("\nJSON解析示例:")
    parsed_data = json.loads(json_str)
    for province in parsed_data["provinces"]:
        print(f"{province['name']}的省会是{province['capital']}")

def yaml_demo():
    # 转换为YAML
    yaml_str = yaml.dump(china_provinces, allow_unicode=True, sort_keys=False)
    
    # 打印YAML
    print("\nYAML格式:")
    print(yaml_str)
    
    # YAML解析示例
    print("\nYAML解析示例:")
    parsed_data = yaml.safe_load(yaml_str)
    for province in parsed_data["provinces"]:
        print(f"{province['name']}的省会是{province['capital']}")

def html_to_structured_data():
    # 抓取HTML页面
    url = "http://python123.io/ws/demo.html"
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        html = r.text
    except:
        print("获取HTML页面失败")
        return
    
    # 使用BeautifulSoup解析HTML
    soup = BeautifulSoup(html, "html.parser")
    
    # 提取信息并转换为结构化数据
    data = {
        "title": soup.title.string if soup.title else "",
        "links": []
    }
    
    # 获取所有链接
    for link in soup.find_all('a'):
        link_data = {
            "text": link.string if link.string else "",
            "href": link.get('href', "")
        }
        data["links"].append(link_data)
    
    # 转换为JSON
    json_str = json.dumps(data, ensure_ascii=False, indent=2)
    print("\nHTML转换为JSON:")
    print(json_str)

if __name__ == "__main__":
    xml_demo()
    json_demo()
    yaml_demo()
    html_to_structured_data() 