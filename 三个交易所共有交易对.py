import os


rrr1=set()
folder_path = "DATA\\Binance\\"  # 将这里替换为实际的文件夹路径
file_names = os.listdir(folder_path)
for file_name in file_names:
    if file_name.find("_USDT_d.txt")>-1:
        rrr1.add(file_name.replace("_USDT_d.txt",""))
        #print(file_name)
print(rrr1)


rrr2=set()
folder_path = "DATA\\OKEX\\"  # 将这里替换为实际的文件夹路径
file_names = os.listdir(folder_path)
for file_name in file_names:
    if file_name.find("_USDT_d.txt")>-1:
        rrr2.add(file_name.replace("_USDT_d.txt",""))
        #print(file_name)
print(rrr2)


rrr3=set()
folder_path = "DATA\\Gateio\\"  # 将这里替换为实际的文件夹路径
file_names = os.listdir(folder_path)
for file_name in file_names:
    if file_name.find("_USDT_d.txt")>-1:
        rrr3.add(file_name.replace("_USDT_d.txt",""))
        #print(file_name)
print(rrr3)


rrr=rrr1&rrr2&rrr3
rrr.remove("USDC")
rrr.remove("DAI")
rrr.remove("USTC")
print("-----------")
print(rrr)
print(len(rrr))
print(sorted(rrr))
