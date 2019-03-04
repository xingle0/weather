import json
#　打开json文件 
fb = open("/home/tarena/wea_project/weather/weather_id.json")
# 加载并获取js对象
city_list = json.load(fb)
print(len(city_list))
# for i in city_list:
#     print(i['cityZh'],i['leaderZh'],i['provinceZh'])
#　打开json文件
fb.close()
