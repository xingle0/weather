#爬天气的接口
import urllib.request
import json
code='101110101'
code='101110501'
url='http://www.weather.com.cn/data/cityinfo/%s.html'% code
obj=urllib.request.urlopen(url)
data_b=obj.read()
data_s=data_b.decode('utf-8')
data_dict=json.loads(data_s)
rt =data_dict['weatherinfo']
my_rt=('%s,%s,%s~%s')% (rt['city'],rt['weather'],rt['temp1'],rt['temp2'])
print(my_rt)
