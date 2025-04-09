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


eee=["DATA\\Binance\\", "DATA\\OKEX\\", "DATA\\Gateio\\"]
aaa=['1INCH', 'AAVE', 'ACA', 'ACE', 'ACH', 'ADA', 'AERGO', 'AEVO', 'AGLD',
     'ALCX', 'ALGO', 'ALPHA', 'APE', 'API3', 'APT', 'AR', 'ARB', 'ARKM',
     'ASTR', 'ATOM', 'AUCTION', 'AVAX', 'AXS', 'BADGER', 'BAL', 'BANANA',
     'BAND', 'BAT', 'BCH', 'BICO', 'BLUR', 'BNB', 'BNT', 'BOME', 'BONK',
     'BTC', 'BTT', 'CATI', 'CELO', 'CELR', 'CETUS', 'CFX', 'CHZ', 'CITY',
     'CLV', 'COMP', 'CRV', 'CVC', 'CVX', 'DGB', 'DIA', 'DOGE', 'DOGS',
     'DOT', 'DYDX', 'EGLD', 'EIGEN', 'ELF', 'ENJ', 'ENS', 'EOS', 'ETC',
     'ETH', 'ETHERNITY', 'ETHFI', 'FET', 'FIL', 'FLM', 'FLOKI', 'FLOW',
     'FORTH', 'FTM', 'FXS', 'G', 'GALA', 'GAS', 'GFT', 'GHST', 'GLM',
     'GLMR', 'GMT', 'GMX', 'GRT', 'HBAR', 'HMSTR', 'ICP', 'ICX', 'ID',
     'ILV', 'IMX', 'INJ', 'IOST', 'IQ', 'JOE', 'JST', 'JTO', 'JUP', 'KAIA',
     'KDA', 'KNC', 'KSM', 'LDO', 'LINK', 'LPT', 'LQTY', 'LRC', 'LSK', 'LTC',
     'LUNA', 'LUNC', 'MAGIC', 'MANA', 'MASK', 'MDT', 'MEME', 'METIS', 'MINA',
     'MIOTA', 'MKR', 'MLN', 'MOVR', 'NANO', 'NEAR', 'NEIRO', 'NEO', 'NMR',
     'NOT', 'NULS', 'OM', 'ONE', 'ONT', 'OP', 'ORDI', 'OXT', 'PENDLE',
     'PEOPLE', 'PEPE', 'PERP', 'PHA', 'PNUT', 'POL', 'PYTH', 'QTUM', 'RAY',
     'RDNT', 'RENDER', 'RONIN', 'RPL', 'RSR', 'RVN', 'SAND', 'SC', 'SCROLL',
     'SHIB', 'SKL', 'SLP', 'SNT', 'SNX', 'SOL', 'SSV', 'STORJ', 'STRK',
     'STX', 'SUI', 'SUSHI', 'T', 'THETA', 'TIA', 'TNSR', 'TON', 'TRB',
     'TRX', 'TURBO', 'UMA', 'UNI', 'W', 'WAXP', 'WBTC', 'WIF', 'WIN', 'WLD',
     'WOO', 'XLM', 'XRP', 'XTZ', 'YFI', 'YGG', 'ZIL', 'ZK', 'ZRO', 'ZRX']  # 已去掉USDC, DAI, USTC
bbb=['USDT']

ddd={}
gain=0
rrr=[]

# 0时间  1开盘  2最低  3最高  4收盘  5成交量  6成交额

# 数据全部加载
for aa in aaa:
    for bb in bbb:
        if os.path.exists(f'DATA/Binance/{aa}_{bb}_d.txt'):
            with open(f'DATA/Binance/{aa}_{bb}_d.txt', 'r', encoding='utf-8-sig', newline='\r\n') as f:
                ddd[aa]=json.loads(f.read())
        else:
            continue
                
for i in range(-998,-3):
    AOV_n0={"A":0,"O":0,"V":0}
    AOV_n1={"A":0,"O":0,"V":0}
    for aa in aaa:
        if aa!="BTC" and len(ddd[aa])>=abs(i)+2 and ddd[aa][i][0]==ddd["BTC"][i][0]:  # 与BTC的时间戳对齐
            if ddd[aa][i][4]>ddd[aa][i][1]:
                AOV_n0["A"]+=1
            elif ddd[aa][i][4]<ddd[aa][i][1]:
                AOV_n0["V"]+=1
            else:
                AOV_n0["O"]+=1

            if ddd[aa][i+1][4]>ddd[aa][i+1][1]:
                AOV_n1["A"]+=1
            elif ddd[aa][i+1][4]<ddd[aa][i+1][1]:
                AOV_n1["V"]+=1
            else:
                AOV_n1["O"]+=1            

    #print(AOV_n0)
    #print(AOV_n1)
    
    #if (AOV_n0["A"]/AOV_n0["V"]) if AOV_n0["V"]>0 else float('-inf') < 3/7 or 7/3 <= (AOV_n0["A"]/AOV_n0["V"]) if AOV_n0["V"]>0 else float('inf'):
    if (AOV_n0["A"]/AOV_n0["V"]) if AOV_n0["V"]>0 else float('-inf') < 3/7:
        if 0 > ((ddd["BTC"][i-1][4]-ddd["BTC"][i-1][1])/ddd["BTC"][i-1][1]) if ddd["BTC"][i-1][1]>0 else 0 \
           > ((ddd["BTC"][i][4]-ddd["BTC"][i][1])/ddd["BTC"][i][1]) if ddd["BTC"][i][1]>0 else 0:

            #if (AOV_n1["A"]/AOV_n1["V"]) if AOV_n1["V"]>0 else float('-inf') < 3/7 or 7/3 <= (AOV_n1["A"]/AOV_n1["V"]) if AOV_n1["V"]>0 else float('inf'):
            if (AOV_n1["A"]/AOV_n1["V"]) if AOV_n1["V"]>0 else float('-inf') < 3/7:
                gain+=(ddd["BTC"][i+1][4]-ddd["BTC"][i+1][1])/ddd["BTC"][i+1][1] if ddd["BTC"][i+1][1]>0 else 0  # 用第二天的收益计算
            else:
                gain+=(ddd["BTC"][i+2][4]-ddd["BTC"][i+1][1])/ddd["BTC"][i+1][1] if ddd["BTC"][i+1][1]>0 else 0  # 用两天的收益计算

            print(i,gain)

            rrr.append([gain,ddd["BTC"][i][0]])
                
print(gain)
print(rrr)
print(len(rrr))


print("--end--")
