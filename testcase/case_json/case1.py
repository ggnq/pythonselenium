import json

fp = open('case.json')   #打开文件
data = json.load(fp)   #加载文件
print(data['login'])   #取出login的数据