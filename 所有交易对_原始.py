# AB量化，运行环境Python3.8
# -*- coding: UTF-8 -*-


from urllib import request, parse
from urllib.parse import quote
import urllib.parse

import time
import datetime
import json
import base64
import hashlib
import random
import os
import io
import zipfile
import zlib

import urllib.request
import gzip

from PIL import Image, ImageDraw,ImageFont


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


def get_english_len(s):
    length = 0
    for ch in s:
        if '\u4e00' <= ch <= '\u9fff':
            length += 2  # 中文字符占两个字节
        else:
            length += 1  # 英文字符占一个字节
    return length


with open(f'所有交易对_原始.txt', 'r', encoding='utf-8-sig', newline='\r\n') as f:
    uuu=json.loads(f.read())

rrr=[]
for kk in uuu["Data"]["exchanges"].keys():
    for k in uuu["Data"]["exchanges"][kk]["pairs"].keys():
        for k0 in uuu["Data"]["exchanges"][kk]["pairs"][k]["tsyms"].keys():
            #print(k,k0,kk)
            rrr.append([k,k0,kk])

with open(f'所有交易所交易对_处理后.txt', 'w', encoding='utf-8', newline='\r\n') as f:
    f.write(json.dumps(rrr, indent=0, ensure_ascii=False)+"\r\n")

print(len(rrr))
print("--end--")
