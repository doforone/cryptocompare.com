# -*- coding: UTF-8 -*-

from urllib import request, parse
from urllib.parse import quote

import time
import json
#import pyodbc

from PIL import Image, ImageDraw,ImageFont
import random
import os

import datetime
from datetime import timedelta
#from datetime import datetime, timezone

#============================时间到强制结束线程
import threading
import inspect
import ctypes

def _async_raise(tid, exctype):
    """raises the exception, performs cleanup if needed"""
    tid = ctypes.c_long(tid)
    if not inspect.isclass(exctype):
        exctype = type(exctype)
    res = ctypes.pythonapi.PyThreadState_SetAsyncExc(tid, ctypes.py_object(exctype))
    if res == 0:
        raise ValueError("invalid thread id")
    elif res != 1:
        # """if it returns a number greater than one, you're in trouble,
        # and you should call it again with exc=NULL to revert the effect"""
        ctypes.pythonapi.PyThreadState_SetAsyncExc(tid, None)
        raise SystemError("PyThreadState_SetAsyncExc failed")
 
def stop_thread(thread):
    _async_raise(thread.ident, SystemExit)

#=============================

def get_htmll(urll,dataa=None):     #请求页面，这个函数要用线程，长时间不响应就杀死线程，参数5秒有时不起作用
    print(urll)
    if 1:
        global htmll
        headers = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
        try:
            req = request.Request(urll, headers=headers)
            with request.urlopen(req, timeout=125) as resp:
                htmll=resp.read().decode("utf-8")
        except Exception as e:
            htmll=""


f0=lambda x: 0.0 if x=="" else float(x)


def tt_d(x):  # 时间戳转日期
    timestamp = x  # 假设这是一个时间戳
    # 使用 fromtimestamp() 方法将时间戳转换为日期时间对象
    #date_time = datetime.datetime.fromtimestamp(timestamp)
    date_time = datetime.datetime.fromtimestamp(timestamp, tz=datetime.timezone.utc)
    #date_time = datetime.datetime.fromtimestamp(timestamp, tz=pytz.timezone('Asia/Shanghai'))
    # 然后可以使用 strftime() 方法将日期时间格式化为特定的日期字符串
    #formatted_date = date_time.strftime('%Y-%m-%d %H:%M:%S')
    formatted_date = date_time.strftime('%Y-%m-%d')
    return formatted_date  # 输出格式化后的日期字符串


def a_b(a,b):
    # 计算a-b,保留最长的小数位
    a=str(a);b=str(b)
    
    if a.find(".")==-1:
        a_max=0
    else:
        a_max=len(str(a).split('.')[-1])

    if b.find(".")==-1:
        b_max=0
    else:
        b_max=len(str(b).split('.')[-1])

    maxx=max(a_max, b_max)

    return round(float(a)-float(b),maxx)


#  {"time":1732924800,"high":97514.26,"low":96137.13,"open":97510.92,"volumefrom":12565.01,"volumeto":1215861238.63,"close":96473.51,"conversionType":"direct","conversionSymbol":""}
#  时间  高  低  开  量  额  收

#  https://min-api.cryptocompare.com/data/v2/histoday?fsym=BTC&tsym=USD&limit=300&toTs=1733011200&allData=true
#  https://min-api.cryptocompare.com/data/v2/histoday?fsym=BTC&tsym=USD&allData=true

if __name__ == "__main__":
    htmll=""

    with open(f'所有交易所交易对_处理后.txt', 'r', encoding='utf-8-sig', newline='\r\n') as f:
        uuu=json.loads(f.read())

    rrr=set()
    for uu in uuu:
        rrr.add(uu[2])

    print(len(rrr))


    print("--end--")




