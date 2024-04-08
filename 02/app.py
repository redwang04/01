Python 3.12.2 (tags/v3.12.2:6abddd9, Feb  6 2024, 21:26:36) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import json,urllib.request
... 
... url = 'https://opendata.cwa.gov.tw/api/v1/rest/datastore/F-C0032-001?Authorization=0000000000000
... data = urllib.request.urlopen(url).read()
... output = json.loads(data)
... location=output['records']['location']
... 
... 
... for i in location:
...     print(f'{i}')
... 
... 
... 
... for i in location:
...     city = i['locationName']    # 縣市名稱
...     wx8 = i['weatherElement'][0]['time'][0]['parameter']['parameterName']    # 天氣現象
...     maxt8 = i['weatherElement'][1]['time'][0]['parameter']['parameterName']  # 最高溫
...     mint8 = i['weatherElement'][2]['time'][0]['parameter']['parameterName']  # 最低溫
...     ci8 = i['weatherElement'][3]['time'][0]['parameter']['parameterName']    # 舒適度
...     pop8 = i['weatherElement'][4]['time'][0]['parameter']['parameterName']   # 降雨機率
