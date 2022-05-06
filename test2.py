import pickle  # 引入pickle模块 数据


# 获取基础数据
fileread = open('dataFile.txt', 'rb')  # 打开数据文件
datalist_rb = pickle.load(fileread)  # 读取数据
var_language = datalist_rb[1]
var_chrome_path = datalist_rb[2]  # 配置Chrome浏览器参数调用
var_metamask_password = datalist_rb[3]  # Sign，第6步调用
var_password_choice = datalist_rb[4]
var_nft_path = datalist_rb[5]  # Upload_prepare，第5步调用
var_coll_name = datalist_rb[6]  # Upload_prepare，第4步调用
var_nft_name = datalist_rb[7]  # Fill，第2步调用
var_nft_number = datalist_rb[8]
var_add_number = datalist_rb[9]
var_name_suffix = datalist_rb[10]
var_no_number = datalist_rb[11]
var_nft_price = datalist_rb[12]
var_first = datalist_rb[13]
var_blockchain = datalist_rb[14]

print('var_nft_number = ', var_nft_number)
print('var_add_number = ', var_add_number)
print('var_name_suffix = ', var_name_suffix)
print('var_no_number = ', var_no_number)