from selenium import webdriver  # 引入selenium模块
from PIL import Image
import xlrd   # 引入Excel读取模块
from xlutils.copy import copy        #导入copy模块
import time
import os

# 给根目录文件夹内的全部文件拼装绝对路径
def get_files(pics_path):
    listdir = os.listdir(pics_path)  # 定位文件夹位置
    filepath = os.getcwd()  # 当前工作目录
    allfile = []  # 定义为数组
    for file in listdir:
        allfile.append(filepath + '\\' + pics_path + '\\' + file)  # 拼装地址
    return allfile
# 定义浮点转字符函数
def float_to_str(float_value):
    try:
        float_value = int(float_value)    #尝试转换为整数
    except ValueError as e:    #文本或文本含数字情况赋值失败
        return float_value     #即无需转换，直接返回
    else:
        if (float_value == int(float_value)):  #如果值为整数
            return str(int(float_value))       #值转换为整数后转换为字符
        else :                                 #如果值为浮点数
            return str(float_value)            #值转换为字符
def get_pt():
    # 提取excel有多少行，并做成数组
    data = xlrd.open_workbook('file.xls', formatting_info=True)  # 打开xls文件,不修改原有样式
    table = data.sheets()[1]
    wb = copy(data)  # 利用xlutils.copy下的copy函数复制
    ws = wb.get_sheet(1)  # 获取表单
    num_nrows = []
    for i in range(int(table.nrows)):
        num_nrows.append(i)
    #提取部分desc做成数组
    table2 = data.sheet_by_name(r'item')  # 表格内工作表
    ncols = table2.ncols  # 定义列数
    desc_part = []
    for i in range(ncols):
        if i == 2:
            desc_part = table2.col_values(i)
    # 获取图片像素部分
    Image.MAX_IMAGE_PIXELS = 2300000000
    a = get_files('pic')
    desc_mix = []
    story = str(table2.col_values(8)[0])
    for i,j in zip(a,desc_part):
        desc_mix.append(str(j) + ' ' + str(Image.open(i).size[0]) + '  x  ' + str(Image.open(i).size[1]) + '  px  \n\n' + story)
    # 拼装描述内容
    for i,j in zip(num_nrows,desc_mix):
        ws.write(i,2,j)  # 改变（0,0）的值
    wb.save('file_do.xls')   # 保存文件
# 创建NFT

#get_pt()
coll = '//*[@id="__next"]/div[1]/div/div/main/div/div/section[2]/div/div/div[1]/div[3]/a/div/a/div'
pics = get_files(r"pic")  # 完成第一个数组（图片）
datafile_path = r'file_do.xls'  # 表格位置
data = xlrd.open_workbook(datafile_path)  # 获取数据
table = data.sheet_by_name(r'item')  # 表格内工作表
ncols = table.ncols  # 定义列数
names = []
descs = []
prop_type = []
prop_name = []
prs = []
for i in range(ncols):
    if i == 1:
        names = table.col_values(i)
    if i == 2:
        descs = table.col_values(i)
    if i == 3:
        prop_type = table.col_values(i)
    if i == 4:
        prop_name = table.col_values(i)
    if i == 5:
        prs = table.col_values(i)

print(prs)