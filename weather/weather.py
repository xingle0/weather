# coding=utf-8
import urllib.request
import json
from pymysql import *
import sys
import re
from pypinyin import *
from PIL import Image,ImageDraw,ImageFont
# # 利用正则获取目标字符串中的地点和时间
# pattern="(?P<市>\w+市)(?P<区>\w+[区,县])(?P<时间>\w天)天气"
# s = '西安市碑林区今天天气'
# regex = re.compile(pattern)
# it = regex.findall(s)
# print(it)
# localtion1=it[0][0]
# localtion2=it[0][1]

# #利用mysql查询获得城市代码code
# s1=localtion1
# s2=localtion2
# host = '127.0.0.1'
# # port = 3306
# user = 'root'
# password = '123456'
# dbname = 'cityinfo'
# # 将汉字转化成拼音
# test1=pinyin(s1,style=NORMAL)
# print(test1)
# test1=test1[0]+test1[1]
# s1=''.join(test1)
# test2=pinyin(s2,style=NORMAL)
# print(test2)
# test2=test2[0]+test2[1]
# s2=''.join(test2)

def main():
    # try:
    #     conn = connect(host,user,password,dbname)
    # except Exception as e:
    #     print(e)
    # cursor = conn.cursor()
    # sql = 'select id from city where leaderEn = "%s" and cityEn = "%s"'%(s1,s2)
    # print(sql)
    # # sql = 'select id from city where cityEn = "beijing"'
    # try:
    #     cursor.execute(sql)
    # except Exception as e:
    #     print(e)
    #     return
    # result = cursor.fetchone()
    # print(result)
    # cursor.close()
    # conn.close()
    
    #　打开json文件 
    s = "碑林"
    fb = open("/home/tarena/wea_project/weather/weather_id.json")
    # 加载python json格式文件
    city_list = json.load(fb)
    #　打开json文件
    fb.close()
    for i in city_list:
        if s == i['cityZh'] or s == i['provinceZh']:
            city_id = i['id']
            break

    code = city_id
    # code = result[0]
    url='https://www.tianqiapi.com/api/?version=v1&cityid=%s'% code
    print(url)
    obj=urllib.request.urlopen(url)
    data_b=obj.read()
    data_s=data_b.decode('utf-8')
    # json.loads()解码python json格式
    data_dict=json.loads(data_s)
    print(len(data_dict))
    print(type(data_dict))
    print()
    for k,v in data_dict['data'][0].items():
        print(k,v)
    rt =data_dict['data'][0]
    my_rt=('%s天气：%s,温度范围:%s~%s，当前温度:%s')% (data_dict['city'],rt['wea'],rt['tem2'],rt['tem1'],rt['tem'])
    print(my_rt)

    # 添加背景图片
    im = Image.open("/home/tarena/project/WxRobot/utils/weather/background.jpg")
    # 创建一个新的图片
    txt = Image.new('RGBA',im.size,(0,0,0,0))
    # 新建绘图对象
    draw = ImageDraw.Draw(txt)
    # 获取图像的宽和高
    width,height = txt.size
    # 选择文字的字体和大小
    setFont = ImageFont.truetype('/home/tarena/project/WxRobot/utils/weather/本墨悠圆.ttf',20)
    # 设置文字颜色
    fillColor = (255,0,0,255)
    # 写入文字
    draw.text((40,30),'地点:'+data_dict['city'],font=setFont,fill=fillColor)
    draw.text((40,70),'时间:'+rt['date'],font=setFont,fill=fillColor)
    draw.text((40,110),'天气:'+rt['wea'],font=setFont,fill=fillColor)
    draw.text((40,150),'现在温度:'+rt['tem'],font=setFont,fill=fillColor)
    draw.text((40,190),'温度范围:'+rt['tem2']+'-'+rt['tem1'],font=setFont,fill=fillColor)

    # 添加图片
    mark = Image.open("/home/tarena/project/WxRobot/utils/weather/robot.ico")
    txt.paste(mark,(im.size[0]-200,100))
    # 结合背景图和文字
    out = Image.composite(txt,im,txt)
    # 展示图片
    out.show()
    # 保存图片
    out.save("weather.jpg")
    return(my_rt)

if __name__ == '__main__':
    main()