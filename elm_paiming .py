#!/usr/bin/env python
# encoding: utf-8

"""
@version: ??
@author: phpergao
@license: Apache Licence 
@file: elm_paiming.py
@time: 2016/8/2 11:18
"""

import requests,re,urllib,codeop,urllib.request,nturl2path,macurl2path,SQL,datetime,time
def main(store_name,paiming,address):
## ms = MSSQL(host="localhost",user="sa",pwd="123456",db="PythonWeiboStatistics")
## #返回的是一个包含tuple的list，list的元素是记录行，tuple的元素是每行记录的字段
## ms.ExecNonQuery("insert into WeiBoUser values('2','3')")

    ms = SQL.MSSQL(host='192.168.72.172',user="stdservice",pwd="数据库密码",db="stddata")
    #resList = ms.ExecQuery(cmd)
    #print(resList)
    #for i in resList:
     #   print(i)
    #dele =ms.ExecNonQuery("DELETE FROM waimai4.dbo.baidu_rueren")
    #update=ms.ExecNonQuery("UPDATE dbo.GOODS SET CLASSID='19' WHERE GOODSNAME LIKE'%牛肉%'")
    today = datetime.date.today()
    tm=time.strftime("%H:%M:%S")
    sj="{} {}".format(str(today),tm)
    insert=ms.ExecNonQuery('''INSERT INTO dbo.elm_paiming

VALUES  ( '{}' , -- store_name - char(20)
          {} , -- paiming - int
          '{}',
          '{}'
        )'''.format(store_name,paiming,address,sj))

User_Agent = "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36"#伪装成浏览器访问
headers = ('User-Agent', User_Agent)
opener = urllib.request.build_opener()
opener.addheaders = [headers]
def paiming(latitude,longitude):
    a=0
    flag=True
    num=0
    while flag:
        url ="https://www.ele.me/restapi/shopping/restaurants?extras%5B%5D=activities&geohash=ws0edemxcy4&latitude={}&limit=24&longitude={}&offset={}".format(latitude,longitude,a)
        a+=24
        ret = opener.open(url).read()

        html = re.findall(r'''"latitude".*?"longitude":.*?,"name":"(.*?)","next_business_time":".*?","only_use_poi":.*?,"opening_hours":''', str(ret,'utf8'))
        for i in html:
            num += 1
            #print(i)
            if '72' in i:
                address=re.findall(r"latitude=(.*?)&limit=24&longitude=(.*?)&offset=",url)
                print("店铺名:{},排名{},定位地址坐标:纬度{}经度{}.".format(i,num,address[0][0],address[0][1]))
                main(i,num,"定位地址坐标:纬度{}经度{}".format(address[0][0],address[0][1]))
                print("ok")
                flag=False
                
                break
        if a>1000:
            break

if __name__ == '__main__':
    urlslist=[

            "22.82124,113.68040",

            "22.73132,113.82848",
            "22.54677,114.05938",
            "22.53561,114.02428",
            "22.51951,113.92929",
            "22.82332,113.69032",
            "22.96579,114.01655",
        "23.12102,113.28648",
        "23.10144,113.32775",
        "23.15731,113.31691",
        "23.12692,113.40926",
        "23.12324,113.26319",
        "23.15061,113.26322",
        "23.11492,113.26190",
        "23.13165,113.32285",
        "23.13734,113.33958",
        "23.10137,113.34205",
        "23.15608,113.25575",
        "23.15350,113.33133",
        "23.14315,113.30050",
        "23.09373,113.28107",
        "23.12454,113.31606",
        "23.14013,113.34624",
        "22.94733,113.37166",
        "23.10185,113.27852",
        "23.19753,113.26775",
        "23.04427,113.32636",
        "23.13248,113.58353",
        "23.16692,113.26344",
        "23.17588,113.34749",
        "23.01246,113.35488",
        "22.53755,114.12410",
        "22.73725,113.83571",
        "22.55246,114.06603",
        "23.01878,113.10495",
        "22.97198,114.02276",
        "22.83730,113.68240",
        "22.55327,114.12776",
        "23.04515,113.76170",
        "22.56758,113.91300",
    ]
    for i in urlslist:
        latitude, longitude=i.split(',')
        paiming(latitude,longitude)
'''

'''