#!/usr/bin/env python
# encoding: utf-8

"""
@version: ??
@author: phpergao
@license: Apache Licence 
@file: baidu_paiming.py
@time: 2016/8/1 11:10
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
    insert=ms.ExecNonQuery('''
INSERT INTO dbo.baidu_paiming

VALUES  ( '{}' , -- store_name - char(20)
          '{}' , -- paiming - int
          '{}' , -- dingwei_address - char(500)
          '{}'  -- updatetime - char(50)
        )'''.format(store_name,paiming,address,sj))

def chapaiming(urllist):
    User_Agent = "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36"#伪装成浏览器访问
    headers = ('User-Agent', User_Agent)
    opener = urllib.request.build_opener()
    opener.addheaders = [headers]
    num0=1
    num=1
    flag=True

    while flag:

        url="http://waimai.baidu.com/waimai/shoplist/{}?display=json&page={}&count=40".format(urllist,num0)
        num0 += 1
        if num0>100:
            break

        ret = opener.open(url)
        #ret =urllib.request.urlopen(url)
        ret=ret.read().decode('unicode_escape')
        html = re.findall(r'''"shop_name":"(.*?)","shop_announcement":''', ret)
        address=re.findall(r'''"poi_address":"(.*?)"},"sortby":''',ret)
        for i in html:
            num += 1
            if '72' in str(i):

                print(i,"排名在:{},定位地址:{}".format(num,address[0]))
                main(i,num,address[0])
                print("ok")
                num0 = 1
                flag=False

                break
            #print(i)




if __name__=="__main__":
    urllist = ["f7a2bee997ef68e8",  # 丽影
               "3b246a0864597e50",  # 穗丰
               "0ebf88697141f32f",  # 冠城
               "eff209d4a7f538ca",  # 礼岗
               "57f9e38e087acf61",  # 购书
               "873652c5edee4720",  # 东川
               "c9e2883cb7e4ea29",#72街(中医大店)
               "9aa836d8e3bd0abb",#72街(圣地店)
               "d6fcc2fb481b8354",#72街(岗顶店)
               "8b8e99cf327a6e06",#72街(沙河店)
               "b83d074f9b83d768",#72街(东圃分店)
               "8d234c801a2c206b",#72街(省中医店)
               "4f5d9fc58d772875",#72街(长江国际店)
               "865c5a08e84bf53b",#72街(沿江店)
               "5cdfce04a9264b56",#72街(盈丰店)
               "6fdcb0377da7a67e",#天河南
               "3d1a08d6c79fd0d6",#72街(赤岗店)
               "1104607b2375c182",#72街(广园西店)
               "018dc479e81f1767",#72街(宝泰二店)
               "acb5fda2bebca2e6",#72街（易发店）
               "5c37e1fcc15704e4",#72街(江南西店)
               "ea1eae6d6a611dbf",#72街（新市店）
               "c7694defca16747a",#72街（厦滘店)
               "2a5f35e13b50dd07",#72街（凤凰城店）
               "4081ff355c52bb1e",#72街（三元里店）
               "a4e8b15103aa511d",#72街（天河客运站店）
               "3e06ae79fa53a8e0",#72街(万达广场店）
               "49bf01b603eb2be8",#72街(罗湖火车站店)
               "e057040dad89b611",#72街（沙井书城店）
               "cb9cea4807e77aa3",#72街（中心书城店）
               "937784cab2ece026",#72街(东门茂业店)
               "179ca5ec2e64d393",#72街(香缤广场店)


               ]
    for i in urllist:
        chapaiming(i)