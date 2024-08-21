
from SparkQuery import Query

# Set up the SPARQL endpoint URL
sparql_endpoint = "http://localhost:8010/sparql/"

# Create a SPARQLWrapper instance and set the endpoint
sparql = Query(sparql_endpoint)
query="元胡止痛片的原料有哪些"
result =sparql.all_query(query)
print(result)


import re

# 假设这是您的JSON数据
data = {
    'results': {
        'bindings': [
            {'Ingredient': {'type': 'uri', 'value': 'http://example.org/延胡索'}},
            {'Ingredient': {'type': 'uri', 'value': 'http://example.org/明胶'}},
            {'Ingredient': {'type': 'uri', 'value': 'http://example.org/淀粉'}},
            {'Ingredient': {'type': 'uri', 'value': 'http://example.org/滑石粉'}},
            {'Ingredient': {'type': 'uri', 'value': 'http://example.org/白芷'}},
            {'Ingredient': {'type': 'uri', 'value': 'http://example.org/白醋'}},
            {'Ingredient': {'type': 'uri', 'value': 'http://example.org/硬脂酸镁'}},
            {'Ingredient': {'type': 'uri', 'value': 'http://example.org/羟丙基甲基纤维素'}},
            {'Ingredient': {'type': 'uri', 'value': 'http://example.org/羟丙甲纤维素'}},
            {'Ingredient': {'type': 'uri', 'value': 'http://example.org/色素'}},
            {'Ingredient': {'type': 'uri', 'value': 'http://example.org/蔗糖'}},
            {'Ingredient': {'type': 'uri', 'value': 'http://example.org/薄膜包衣预混剂'}},
            {'Ingredient': {'type': 'uri', 'value': 'http://example.org/食用色素'}},
            {'Ingredient': {'type': 'uri', 'value': 'http://example.org/马钱子'}},
            {'Ingredient': {'type': 'uri', 'value': 'http://example.org/麦芽糊精'}}
        ]
    }
}

# 提取汉字部分的正则表达式
chinese_pattern = re.compile(r'[\u4e00-\u9fa5]+')

# 遍历JSON数据中的每个元素，提取含有汉字的部分
for item in data['results']['bindings']:
    uri = item['Ingredient']['value']  # 获取URI
    match = chinese_pattern.search(uri)  # 在URI中寻找第一个匹配的汉字部分
    if match:
        chinese_part = match.group()  # 获取匹配的汉字部分
        print(chinese_part)

