import urllib.request
import json
code='101310304'
url='https://www.tianqiapi.com/api/?version=v1&cityid=%s'% code
obj=urllib.request.urlopen(url)
data_b=obj.read()
data_s=data_b.decode('utf-8')
data_dict=json.loads(data_s)
rt =data_dict['data'][0]
my_rt=('%s天气：%s,温度范围:%s~%s')% (data_dict['city'],rt['wea'],rt['tem1'],rt['tem2'])
print(my_rt)