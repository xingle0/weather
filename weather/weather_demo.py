# -*- coding: utf-8 -*-
'''
weather_demo.py通过调用免费天气接口GET https://www.tianqiapi.com/api/　
获取实时天气信息，然后提取出关键信息调用PIL库生成图片保存在本地
'''
import requests
import json
from PIL import Image,ImageDraw,ImageFont

class Weather(object):
    
    def __init__(self):
        self.url = 'https://www.tianqiapi.com/api/'

    def get_page(self,params):
        res = requests.get(self.url,params=params)
        res.encoding = 'utf-8'
        source = res.text
        self.parse_page(source)

    def parse_page(self,source):
        wea_dic = json.loads(source)
        d = {
            'date':wea_dic['date'],
            'city':wea_dic['city'],
            'wea_img':wea_dic['wea_img'],
            'wea':wea_dic['wea'],
            'tem':wea_dic['tem'],
            'humidity':wea_dic['humidity'],
            'air_level':wea_dic['air_level'],
            'air_tips':wea_dic['air_tips'],
        }
        self.write_file(d)
        
    def write_file(self,d):
        # 创建绘画对象
        im = Image.new("RGB",(380,220),'#40E0D0')
        # 初始化画笔
        draw = ImageDraw.Draw(im)
        # 字体颜色
        font = ImageFont.truetype('/home/tarena/wea_project/weather/simhei.ttf',20)
        # 写字符
        draw.text((5,10),'日期:{0}  城市:{1}'.format(d['date'],d['city']),font=font,fill='#000')
        draw.text((5,40),'温度:{0}°C       湿度:{1}'.format(d['tem'],d['humidity']),font=font,fill='#000')
        draw.text((5,70),'空气质量等级:{}'.format(d['air_level']),font=font,fill='#000')
        draw.text((175,70),'天气:{}'.format(d['wea']),font=font,fill='#000')
        draw.text((5,110),'空气质量描述:{}'.format(d['air_tips'])[:18],font=font,fill='#000')
        draw.text((5,140),'           {}'.format(d['air_tips'])[18:36],font=font,fill='#000')
        draw.text((5,170),'           {}'.format(d['air_tips'])[36:],font=font,fill='#000')
        # 添加图片
        png_path = "/home/tarena/wea_project/weather/apple/{}".format(d['wea_img'])
        mark = Image.open(png_path)
        im.paste(mark,(300,10))
        # 回收画笔
        del draw
        # 保存图片到内存中
        im.save('wea.png')

    def work_on(self,id):
        params = {
            'version':'v6',
            'cityid':id
        }
        self.get_page(params)

if __name__ == '__main__':
    s = input('请输入要查询的城市名:')
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
    id = city_id
    spider = Weather()
    spider.work_on(id)