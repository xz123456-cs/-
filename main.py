from urllib.request import urlopen,Request
from bs4 import BeautifulSoup
import re
url="http://www.shanghairanking.cn/rankings/bcur/2020"
headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3947.100 Safari/537.36'}
ret=Request(url,headers=headers)
html=urlopen(ret)
bs=BeautifulSoup(html,"html.parser")
areas=bs.find_all('td')
wz=bs.find_all('a')
area_list=[]
#以下部分是创建列表，以便之后讲元素放入
paiming_list=['排名']
college_name=['学校名称']
shengshi_list=['省市']
leixing_list=['类型']
zongfen_list=['总分']
wangzhi1_list=[]
wangzhi_list=['网址']

for area in areas:
    area = area.get_text()
    area1 = area.strip()
    area_list.append(area1)
#此时的area_list是按顺序排列的所有我们要的元素


#以下19行是在将他们分类放在列表里
a1,a2,a3,a4,a5=0,1,2,3,4
while a1 < 6*567:
    paiming_list.append(area_list[0+a1])
    a1 = a1+6
while a2 < 6*567:
    college_name.append(area_list[0+a2])
    a2 = a2+6
while a3 < 6*567:
    shengshi_list.append(area_list[0+a3])
    a3 = a3+6
while a4 < 6*567:
    leixing_list.append(area_list[0+a4])
    a4 = a4+6
while a5 < 6*567:
    zongfen_list.append(area_list[0+a5])
    a5 = a5+6
#以下部分和上面部分相似
for wangzhi1 in wz:
    wangzhi1_list.append(wangzhi1.get('href'))

for i in wangzhi1_list:
    if i[0:12] == '/institution':
        wangzhi_list.append(i)
wangzhi_list.pop(1)

for paiming,college,shengshi,leixing,zongfen,wangzhi in zip(paiming_list,college_name,shengshi_list,leixing_list,zongfen_list,wangzhi_list):
    #这是将好几个列表同时遍历一遍，以便将他们同时打印在一起
    print(paiming.ljust(3),college.ljust(15),shengshi.ljust(3),leixing,zongfen.ljust(8),wangzhi)
