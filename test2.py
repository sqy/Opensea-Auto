from PIL import Image

import os

def get_files(pics_path):
    listdir = os.listdir(pics_path)  # 定位文件夹位置
    filepath = os.getcwd()  # 当前工作目录
    allfile = []  # 定义为数组
    for file in listdir:
        allfile.append(filepath + '\\' + pics_path + '\\' + file)  # 拼装地址
    return allfile
Image.MAX_IMAGE_PIXELS = 2300000000
a = get_files('pic')
print(a)
for i in a:
    print(Image.open(i).size)
#  # 宽高
# (200, 153)