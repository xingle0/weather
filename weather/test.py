# import json
# #　打开json文件 
# fb = open("/home/tarena/wea_project/weather/weather_id.json")
# # 加载并获取js对象
# city_list = json.load(fb)
# print(len(city_list))
# # for i in city_list:
# #     print(i['cityZh'],i['leaderZh'],i['provinceZh'])
# #　打开json文件
# fb.close()
# import subprocess

import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime

# from matplotlib import font_manager
# from pylab import mpl

# 扫描matplot自带字体库以及系统字体库,寻找支持能够支持的中文字体
# def get_matplot_zh_font():
#     fm = font_manager.FontManager()
#     mat_donts = set(f.name for f in fm.ttflist)

#     output = subprocess.check_output('fc-list :lang=zh -f "%{family}\n"',shell=True)
#     zh_fonts = set(f.split(',',1)[0]for f in str(output).split('\n'))
#     available = list(mat_donts & zh_fonts)

#     print('*'*10,'可用的字体','*'*10)
#     for f in available:
#         print(f)
#     return available
# def set_matplot_zh_font():
#     available = get_matplot_zh_font()
#     if len(available)>0:
#         mpl.rcParams['font.sans-serif']=[available[0]]
#         mpl.rcParams['axes.unicode_minus']=False
# set_matplot_zh_font()
# print(dir(plt.rcParams))
# plt.rcParams['font.sans-serif']=['simhei']
# plt.rcParams['axes.unicode_minus']=False
# plt.figure()

# l_time=['02日08时','02日11时','02日14时','02日17时','02日20时','02日23时','03日02时','03日05时']
# xs = [datetime.strptime(d,'%d日%H时') for d in l_time]
# # x = [i for i in (2,5,8,11,14,17,20,23)]
# y = [2,2,5,14,16,16,12,5]

# fig = plt.figure()
# ax = fig.add_subplot(1,1,1)

# # 指定x轴以日期格式(带小时)显示
# ax.xaxis.set_major_formatter(mdates.DateFormatter('%d日%H时'))
# # x轴的间隔为小时
# ax.xaxis.set_major_locator(mdates.HourLocator())
# plt.plot(xs,y,'o-')
# plt.title("3-9天气折线图")
# plt.xlabel("时间")
# plt.ylabel("温度")
# for xy in zip(xs,y):
#     plt.annotate(xy[1],xy=xy,xytext=(0,0),textcoords='offset points')
# plt.gcf().autofmt_xdate()
# plt.show()

label_list = ['2014','2015','2016','2017']
num_list1 = [20,30,15,35]
num_list2 = [15,30,40,20]
x = range(len(num_list1))

rects1 = plt.bar(x,height=num_list1,width=0.4,color='red',label='一部门')
rects２ = plt.bar(x=[i + 0.4 for i in x],height=num_list2,width=0.4,color='green',label='二部门')
plt.ylim(0,50)
plt.ylabel("数量")
plt.xticks([index + 0.2 for index in x],label_list)
plt.xlabel('年份')
plt.title('某某公司')
plt.legend()


for rect in rects1:
    height = rect.get_height()
    plt.text(rect.get_x()+rect.get_width()/2,height+1,str(height),ha="center",va="bottom")
for rect in rects2:
    height = rect.get_height()
    plt.text(rect.get_x()+rect.get_width()/2,height+1,str(height),ha="center",va="bottom")
plt.show()
# for x in range(0,100):
#     for y in range(0,100):
#         for z in range(0,100):
#             if x+y+z==100 and 5*x+3*y+z/3==100:
#                 print (x,y,z)

# lst = [(x,y,z) for x in range(0,100) for y in range(0,100)for z in range(0,100) if x+y+z==100 and 5*x+3*y+z/3==100]
# print (lst)
