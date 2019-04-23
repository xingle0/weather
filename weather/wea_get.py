import requests
import json

def main(s):
    #　打开json文件 
    with open("/home/tarena/wea_project/weather/weather_id.json") as f:
        # 读取json文件内容
        city_list = json.load(f)
        #　关闭json文件
        f.close()
    # 根据城市名获取城市id
    for i in city_list:
        if s == i['cityZh'] or s == i['provinceZh']:
            city_id = i['id']
            break   
    code = city_id

    # 2.调用天气接口查询天气
    # 将城市id拼接到查询天气的url上
    url='https://www.tianqiapi.com/api/?version=v6&cityid=%s'% code
    # 获取url请求对象
    res=requests.get(url)
    res.encoding = 'utf-8'
    # 读取url请求内容
    html=res.text
    # 把json格式的字符串转为python数据类型
    wea = json.loads(html)
    s = '城市:{0}\n天气:{1}\n建议:{2}'.format(wea['city'],wea['wea'],wea['air_tips'])
    dic = {'城市':wea['city'],'天气':wea['wea'],'建议':wea['air_tips']}
    print(s)
    print(dic)
    return s

if __name__ == '__main__': 
    s = "碑林"
    main(s)