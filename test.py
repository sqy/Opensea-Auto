from PIL import Image
import xlutils
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
sizes1 = []
sizes2 = []
for i in a:
    sizes1.append(Image.open(i).size[0])
    sizes2.append(Image.open(i).size[1])

# 3.3.3 xlutils读取 写入 Excel 表格信息
def fun3_3_3():
    # file_path：文件路径，包含文件的全名称
    # formatting_info=True：保留Excel的原格式（使用与xlsx文件）
    workbook = xlrd.open_workbook('3_3 xlutils 修改操作练习.xlsx')

    new_workbook = copy(workbook)  # 将xlrd对象拷贝转化为xlwt对象

    # 读取表格信息
    sheet = workbook.sheet_by_index(0)
    col2 = sheet.col_values(1)  # 取出第二列
    cel_value = sheet.cell_value(1, 1)
    print(col2)
    print(cel_value)

    # 写入表格信息
    write_save = new_workbook.get_sheet(0)
    write_save.write(0, 0, "xlutils写入！")

    new_workbook.save("new_test.xls")  # 保存工作簿