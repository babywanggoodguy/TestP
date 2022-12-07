import requests#需要安装requests模块，详情百度pip安装
import json
url='https://free-api.heweather.net/s6/weather/now?location=auto_ip&key=db86a5196f304e52a4369818c5182e60'
yang=requests.get(url)#这里返回的json数据
result=open('a.json','w')

result.write(yang.text)#yang.text将yang这个json数据以字符形式使用
result.close()#这里一定要关闭文件，不然写不进去
open_json=open('a.json','r',encoding='cp936')
zd_json=json.load(open_json)#json.load()将json转为python字典
open_json.close()#到这里zd_json是一个python字典


print('你的地址是：',zd_json['HeWeather6'][0]['basic']['location'])
print('你所在市现在天气是'+zd_json['HeWeather6'][0]['now']['cond_txt'])
print('你所在城市现在温度是'+zd_json['HeWeather6'][0]['now']['tmp']+'℃')
