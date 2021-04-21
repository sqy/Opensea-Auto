import os
import xlrd

datafile_path = r'file.xlsx'  # 表格位置
data = xlrd.open_workbook(datafile_path)  # 获取数据
table = data.sheet_by_name(r'Sheet1')  # 表格内工作表
ncols = table.ncols  #定义列数

names = []
descs = []
for i in range(ncols):
    if i == 1:
        names = table.col_values(i)
    if i == 2:
        descs = table.col_values(i)
print(names)
print(descs)
