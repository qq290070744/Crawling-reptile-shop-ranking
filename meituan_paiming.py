#!/usr/bin/env python
# encoding: utf-8
 
"""
@version: ??
@author: phpergao
@license: Apache Licence 
@file: meituan_paiming.py
@time: 2016/8/1 15:16
"""
 
 
import urllib,json,re
import urllib.parse
import http.cookiejar
import urllib.request,datetime,time,SQL
from multiprocessing import Process
import collections
 
def main(store_name,paiming):
## ms = MSSQL(host="localhost",user="sa",pwd="123456",db="PythonWeiboStatistics")
## #返回的是一个包含tuple的list，list的元素是记录行，tuple的元素是每行记录的字段
## ms.ExecNonQuery("insert into WeiBoUser values('2','3')")
 
    ms = SQL.MSSQL(host='192.168.72.172',user="stdservice",pwd="7数据库密码",db="stddata")
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
INSERT INTO dbo.meituan_paiming
 
VALUES  ( '{}' , -- store_name - char(20)
          '{}' , -- paiming - int
          ' ' , -- dingwei_address - char(500)
          '{}'  -- updatetime - char(50)
        )
        '''.format(store_name,paiming,sj))
 
 
def paiming(url):
    cj = http.cookiejar.LWPCookieJar()
    cookies_support = urllib.request.HTTPCookieProcessor(cj)
    opener = urllib.request.build_opener(cookies_support, urllib.request.HTTPHandler)
    urllib.request.install_opener(opener)
    User_Agent = "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36"#伪装成浏览器访问
    headers = ('User-Agent', User_Agent)
    opener = urllib.request.build_opener()
    opener.addheaders = [headers]
    ret = urllib.request.urlopen(url).read()
    #ret = opener.open(url).read()
    html=re.findall(r'''<div data-title="(.*?)" data-bulletin=".*?\n*?.*?" data-poiid=".*?" class="restaurant" data-all=".*?"''',str(ret,'utf8'))
 
    today = datetime.date.today()
    tm = time.strftime("%H:%M:%S")
    sj = "{} {}".format(str(today), tm)
    a=0
    for i in html:
        a+=1
        if "72" in i:
            print(i,a,sj)
            main(i,a)
            print("ok")
urllist = [
    "http://waimai.meituan.com/home/ws0e9gmds0u7",
    "http://waimai.meituan.com/home/ws0edu48zvm8",
    "http://waimai.meituan.com/home/ws0e6v9brqq8",
    "http://waimai.meituan.com/home/ws0ec83j0fbm",
    "http://waimai.meituan.com/home/ws0efv4veqks",
    "http://waimai.meituan.com/home/ws0edg19uxt6",
    "http://waimai.meituan.com/home/ws0esdnh56um",
    "http://waimai.meituan.com/home/ws0e937zdbph",
    "http://waimai.meituan.com/home/ws0e3rfy1wxb",
    "http://waimai.meituan.com/home/ws0eddzptu5e",
    "http://waimai.meituan.com/home/ws0eeh52gdry",
    "http://waimai.meituan.com/home/ws0e7jmpm28g",
    "http://waimai.meituan.com/home/ws0e9pqmfr47",
    "http://waimai.meituan.com/home/ws0edyvqgmrt",
    "http://waimai.meituan.com/home/ws0edjnftj0h",
    "http://waimai.meituan.com/home/ws0e3u0fb2gx",
    "http://waimai.meituan.com/home/ws0ed9dq6x1f",
    "http://waimai.meituan.com/home/ws0eehrxexqc",
    "http://waimai.meituan.com/home/ws0dec6tzjwm",
    "http://waimai.meituan.com/home/ws0e3txh5ym6",
    "http://waimai.meituan.com/home/ws0ecqzp6n82",
    "http://waimai.meituan.com/home/ws0e4g1dxshy",
    "http://waimai.meituan.com/home/ws0g8ejh80rp",
    "http://waimai.meituan.com/home/ws0ec37vje4d",
    "http://waimai.meituan.com/home/ws0eg711k1t1",
    "http://waimai.meituan.com/home/ws0dgmq924yy",
    "http://waimai.meituan.com/home/ws0cff7x3m4u",
    "http://waimai.meituan.com/home/ws0cg5zd5g4y",
    "http://waimai.meituan.com/home/ws0ghenxxz82",
    "http://waimai.meituan.com/home/ws0cfvkuzvtk",
    "http://waimai.meituan.com/home/ws14dtvjhqm4",
    "http://waimai.meituan.com/home/ws100stcewjn",
    "http://waimai.meituan.com/home/ws104zssdsyp",
    "http://waimai.meituan.com/home/ws102hkctrhh",
    "http://waimai.meituan.com/home/ws10m19qgq7h",
    "http://waimai.meituan.com/home/ws1079s3ek0m",
    "http://waimai.meituan.com/home/ws0cq7hwhebm",
    "http://waimai.meituan.com/home/ws10hyydu2f0",
    "http://waimai.meituan.com/home/ws06vy2w07yr"
 
           ]
if __name__ == '__main__':
    for i in urllist:
        p = Process(target=paiming, args=(i,))
        p.start()
        time.sleep(10)
