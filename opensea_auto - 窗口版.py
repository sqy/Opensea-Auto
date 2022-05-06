import tkinter as tk
import tkinter.ttk as ttk
from tkinter.filedialog import askdirectory
import pickle
import tkinter.messagebox
import os

# 第1步，实例化object，建立窗口window
window = tk.Tk()
# 给窗口的可视化起名字
window.title("Welcome")
# 设定窗口的大小(长 * 宽)
window.geometry('520x750')
# 定义初始状态值
var_condition = 0
# 第4步，定义触发函数功能
# 菜单File,New功能
def func_menu_new():
    var_chrome_path.set('')
    var_metamask_password.set('')
    var_password_choice.set('0')
    var_nft_path.set('')
    var_coll_name.set('')
    var_nft_name.set('')
    var_nft_number.set('')
    entry_nft_number.config(state='disable')
    var_add_number.set('0')
    var_name_suffix.set('0')
    var_no_number.set('1')
    var_nft_price.set('')
    var_first.set('0')
    var_blockchain.set('Ethereum')
    var_supply.set('1')

# 菜单File,Save功能
def func_menu_save():
    filehandle = open('dataFile.txt', 'wb')
    datalist_wb = [var_condition,
                var_language,
                var_chrome_path.get(),
                var_metamask_password.get(),
                var_password_choice.get(),
                var_nft_path.get(),
                var_coll_name.get(),
                var_nft_name.get(),
                var_nft_number.get(),
                var_add_number.get(),
                var_name_suffix.get(),
                var_no_number.get(),
                var_nft_price.get(),
                var_first.get(),
                var_blockchain.get(),
                var_supply.get()
                   ]
    pickle.dump(datalist_wb, filehandle)
    filehandle.close()

# 菜单File,Exit功能
def func_menu_exit():
    func_menu_save()
    window.quit()

# 菜单Language,Chinese
def func_menu_chinese():
    global var_language
    try:
        var_language = 'chinese'
        menubar.entryconfig(index='File', label='文件')
        filemenu.entryconfig(index='New', label='新建')
        filemenu.entryconfig(index='Save', label='保存')
        filemenu.entryconfig(index='Exit', label='退出')
        label_chrome_path.set(r'Chrome浏览器个人资料路径 :')
        label_metamask_password.set(r'Metamask钱包密码:')
        label_password_choice.set(r'我自己来输入密码')
        label_nft_path.set(r'NFT文件夹路径 :')
        label_path_choice.set(r"路径选择")
        label_coll_name.set(r'收藏夹名称 :')
        label_nft_name.set(r'NFT 名称 :')
        label_nft_number.set(r'NFT 编号 :')
        label_add_number.set(r'每上架一个NFT，编号加1')
        label_name_suffix.set(r'将编号作为NFT名称后缀')
        label_no_number.set(r'不需要NFT编号')
        label_nft_price.set(r'NFT 价格(ETH) :')
        label_start.set(r'开始')
        #label_enter_password.set(r'已输入密码')
        label_first.set(r"第一次使用")
        label_first2.set(r"当浏览器页面出现选择钱包时,用户需要自行登录")
        label_first3.set(r"并输入钱包助记词.")
        tag_main.tab(0, text='常规')
        tag_main.tab(1, text='更多选项')
    except:
        pass

# 菜单Language,English
def func_menu_english():
    global var_language
    try:
        var_language = 'english'
        menubar.entryconfig(index='文件', label='File')
        filemenu.entryconfig(index='新建', label='New')
        filemenu.entryconfig(index='保存', label='Save')
        filemenu.entryconfig(index='退出', label='Exit')
        label_chrome_path.set(r'Chrome Profile path :')
        label_metamask_password.set(r'Metamask Password :')
        label_password_choice.set(r'Enter the password by myself')
        label_nft_path.set(r'NFT folder Path :')
        label_path_choice.set(r"Path Choice")
        label_coll_name.set(r'Collection Name :')
        label_nft_name.set(r'NFT Name :')
        label_nft_number.set(r'NFT Number :')
        label_add_number.set(r'Increased by one for each NFT')
        label_name_suffix.set(r'Add number to NFT name as suffix')
        label_no_number.set(r"Don't need number")
        label_nft_price.set(r'NFT Price(ETH) :')
        label_start.set(r'Start')
        #label_enter_password.set(r'Entered Password')
        label_first.set(r"For the first time")
        label_first2.set(r"When the select wallet page appears in the browser,")
        label_first3.set(r"the user needs to log in and enter Wallet Seed.")
        tag_main.tab(0, text='General')
        tag_main.tab(1, text='More options')
    except:
        pass
# Metamask钱包密码，自己输入
def func_password_choice():
    if var_password_choice.get() == 1:
        var_metamask_password.set('')
        entry_metamask_password.config(state='disable')
        #button_enter_password.config(state='normal')
    else:
        entry_metamask_password.config(state='normal')
        #button_enter_password.config(state='disable')

# NFT文件夹路径
def func_nft_path():
    path_ = askdirectory()
    var_nft_path.set(path_)

# NFT编号，编号自动增加，编号作为名称后缀，不需要NFT编号
def func_number():
    if var_no_number.get() == 1:
        button_add_number.deselect()
        button_name_suffix.deselect()
        var_nft_number.set('')
        entry_nft_number.config(state='disable')
        button_add_number.config(state='disable')
        button_name_suffix.config(state='disable')
    else:
        entry_nft_number.config(state='normal')
        button_add_number.config(state='normal')
        button_name_suffix.config(state='normal')
        if var_add_number.get() == 1:
            print("I'm writing")
        elif var_name_suffix.get() == 1:
            print("I'm writing")
# 开始按键
def func_start():
    # 默认状态为可开始
    var_start = 1
    # 对NFT编号判定
    nft_number = var_nft_number.get()
    if nft_number == '':  # 如果nft_number为空
        var_no_number.set('1')
        var_add_number.set('0')
        var_name_suffix.set('0')
    else:  # 如果nft_number不为空
        try:
            nft_number = int(nft_number)  # 尝试把nft_number数据定义为整数
        except:  # NFT编号不为整数的，清空输入框，并提示
            var_nft_number.set('')
            var_add_number.set('0')
            var_name_suffix.set('0')
            if var_language == 'chinese':
                tkinter.messagebox.showerror(title='', message=r'NFT编号 请填写整数！')
            elif var_language == 'english':
                tkinter.messagebox.showerror(title='', message=r'Please enter an integer in NFT Number!')

    # 对NFT价格判定
    nft_price = var_nft_price.get()
    if nft_price == '':  # 如果nft_price为空
        var_start = 0  # 无价格不能开始
        if var_language == 'chinese':
            tkinter.messagebox.showerror(title='', message=r'请填写NFT价格！')
        elif var_language == 'english':
            tkinter.messagebox.showerror(title='', message=r'Please enter a number in NFT Price!')
    else:  # 如果nft_price不为空
        try:
            nft_price = float(var_nft_price.get())  # 尝试把nft_price数据定义为浮点数
        except:
            var_start = 0  # 价格不为数字不能开始
            var_nft_price.set('')
            if var_language == 'chinese':
                tkinter.messagebox.showerror(title='', message=r'NFT价格 请填写数字！')
            elif var_language == 'english':
                tkinter.messagebox.showerror(title='', message=r'Please enter a number in NFT Price!')

    # 对块链和Supply判定
    if var_blockchain.get() == 'Polygon':
        try:
            nft_supply = int(var_supply.get())  # 尝试把Supply数据定义为整数
            if nft_supply < 1:
                var_start = 0  # Supply不为数字不能开始
                var_supply.set('1')
                if var_language == 'chinese':
                    tkinter.messagebox.showerror(title='', message=r'Supply 最小为1，自动修改为默认”1“！')
                elif var_language == 'english':
                    tkinter.messagebox.showerror(title='', message=r'The number of Supply must be 1 or greater !')
        except:
            var_start = 0  # Supply不为数字不能开始
            var_supply.set('1')
            if var_language == 'chinese':
                tkinter.messagebox.showerror(title='', message=r'Supply 请填写整数，自动修改为默认”1“！')
            elif var_language == 'english':
                tkinter.messagebox.showerror(title='', message=r'Please enter a integer in Supply!')

    # 开始前自动保存数据
    func_menu_save()
    # 开始程序
    if var_start == 1:
        print('start code')
    else:
        print('start failed')

# 第一次使用
def func_first():
    if var_first.get() == 1:
        lab_first2.config(fg='black')
        lab_first3.config(fg='black')
        var_password_choice.set('1')
        func_password_choice()
        button_password_choice.config(state='disable')
    elif var_first.get() == 0:
        lab_first2.config(fg='#F0F0F0')
        lab_first3.config(fg='#F0F0F0')
        button_password_choice.config(state='normal')

# 链选择
def func_blockchain():
    if var_blockchain.get() == 'Ethereum':
        var_supply.set('1')
        entry_supply.config(state='disable')
    elif var_blockchain.get() == 'Polygon':
        entry_supply.config(state='normal')
        #button_blockchain_ethereum = tk.Radiobutton(tag2, text='Ethereum', variable=var_blockchain, value='Ethereum', command=func_blockchain).place(x=tag2_x0 + 210, y=tag2_y0 + 20)
        #button_blockchain_polygon = tk.Radiobutton(tag2, text='Polygon', variable=var_blockchain, value='Polygon', command=func_blockchain).place(x=tag2_x0 + 310, y=tag2_y0 + 20)

# 第5步，创建菜单栏
menubar = tk.Menu(window)
# 创建一个File菜单项
filemenu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label='File', menu=filemenu)
# 在File中加入New、Open、Save等小菜单
filemenu.add_command(label='New', command=func_menu_new)
filemenu.add_command(label='Save', command=func_menu_save)
filemenu.add_separator()    # 添加一条分隔线
filemenu.add_command(label='Exit', command=func_menu_exit)  # 用tkinter里面自带的quit()函数

# 创建一个Language菜单项
var_language = 'english'
langmenu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label='语言/Language', menu=langmenu)
# 在language中加入小菜单
langmenu.add_command(label='中文', command=func_menu_chinese)
langmenu.add_command(label='English', command=func_menu_english)
# 配置菜单
window.config(menu=menubar)

# 创建主分页签
tag_main = ttk.Notebook(window)
tag_main.place(x=0, y=170, width=520, height=550)

# 创建第一页框架
tag1 = tk.Frame(tag_main)
tag1.place(x=0, y=0)
tag_main.add(tag1, text='General')

# 定义初始坐标
tag1_x0, tag1_y0 = 10, 170

# 第6步，浏览器相关信息
label_chrome_path = tk.StringVar()
label_chrome_path.set(r'Chrome Profile path :')
tk.Label(tag1, text='*', font=('Arial', 12)).place(x=tag1_x0, y=tag1_y0-150)
tk.Label(tag1, textvariable=label_chrome_path, font=('Arial', 12)).place(x=tag1_x0+10, y=tag1_y0-150)
var_chrome_path = tk.StringVar()
var_chrome_path.set(r'C:/Users/Suqing/AppData/Local/Google/Chrome/User Data/')
entry_chrome_path = tk.Entry(tag1, textvariable=var_chrome_path, font=('Arial', 12)).place(x=tag1_x0, y=tag1_y0-120, width=480)

# 第7步，钱包密码相关信息
label_metamask_password = tk.StringVar()
label_metamask_password.set(r'Metamask Password :')
tk.Label(tag1, text='*', font=('Arial', 12)).place(x=tag1_x0, y=tag1_y0-90)
tk.Label(tag1, textvariable=label_metamask_password, font=('Arial', 12)).place(x=tag1_x0+10, y=tag1_y0-90)
var_metamask_password = tk.StringVar()
entry_metamask_password = tk.Entry(tag1, textvariable=var_metamask_password, font=('Arial', 12))
entry_metamask_password.place(x=tag1_x0, y=tag1_y0-60, width=480)
label_password_choice = tk.StringVar()
label_password_choice.set(r'Enter the password by myself')
var_password_choice = tk.IntVar()  # 定义变量用来存放选择行为返回值
button_password_choice = tk.Checkbutton(tag1, textvariable=label_password_choice, variable=var_password_choice, onvalue=1, offvalue=0, command=func_password_choice)
button_password_choice.place(x=tag1_x0+250, y=tag1_y0-90)

# 图片存放文件夹
label_nft_path = tk.StringVar()
label_nft_path.set(r'NFT folder Path :')
tk.Label(tag1, text='*', font=('Arial', 12)).place(x=tag1_x0, y=tag1_y0-30)
tk.Label(tag1, textvariable=label_nft_path, font=('Arial', 12)).place(x=tag1_x0+10, y=tag1_y0-30)
var_nft_path = tk.StringVar()
entry_nft_path = tk.Entry(tag1, textvariable=var_nft_path, font=('Arial', 12)).place(x=tag1_x0+150, y=tag1_y0-30)
label_path_choice = tk.StringVar()
label_path_choice.set(r"Path Choice")
button_path_choice = tk.Button(tag1, textvariable=label_path_choice, command=func_nft_path).place(x=tag1_x0+340, y=tag1_y0-35)

# 第8步，NFT相关信息
# 收藏夹名称
label_coll_name = tk.StringVar()
label_coll_name.set(r'Collection Name :')
tk.Label(tag1, text='*', font=('Arial', 12)).place(x=tag1_x0, y=tag1_y0+10)
tk.Label(tag1, textvariable=label_coll_name, font=('Arial', 12)).place(x=tag1_x0+10, y=tag1_y0+10)
var_coll_name = tk.StringVar()
entry_coll_name = tk.Entry(tag1, textvariable=var_coll_name, font=('Arial', 12)).place(x=tag1_x0+150, y=tag1_y0+10, width=330)

# NFT名称
label_nft_name = tk.StringVar()
label_nft_name.set(r'NFT Name :')
tk.Label(tag1, text='*', font=('Arial', 12)).place(x=tag1_x0, y=tag1_y0+10+40)
tk.Label(tag1, textvariable=label_nft_name, font=('Arial', 12)).place(x=tag1_x0+10, y=tag1_y0+10+40)
var_nft_name = tk.StringVar()
entry_nft_name = tk.Entry(tag1, textvariable=var_nft_name, font=('Arial', 12)).place(x=tag1_x0+150, y=tag1_y0+10+40, width=330)

# NFT编号  ## 要改为编码仅能输入整数
label_nft_number = tk.StringVar()
label_nft_number.set(r'NFT Number :')
tk.Label(tag1, textvariable=label_nft_number, font=('Arial', 12)).place(x=tag1_x0+10, y=tag1_y0+10+80)
var_nft_number = tk.StringVar()
entry_nft_number = tk.Entry(tag1, textvariable=var_nft_number, font=('Arial', 12), state='disable')
entry_nft_number.place(x=tag1_x0+150, y=tag1_y0+10+80, width=100)

# 定义两个Checkbutton选项并放置
label_add_number = tk.StringVar()
label_name_suffix = tk.StringVar()
label_add_number.set(r'Increased by one for each NFT')
label_name_suffix.set(r'Add number to NFT name as suffix')
var_add_number = tk.IntVar()  # 定义变量用来存放选择行为返回值
var_name_suffix = tk.IntVar()  # 定义变量用来存放选择行为返回值
button_add_number = tk.Checkbutton(tag1, textvariable=label_add_number, variable=var_add_number, onvalue=1, offvalue=0, state='disable', command=func_number)    # 传值原理类似于radiobutton部件
button_add_number.place(x=tag1_x0+250, y=tag1_y0+10+70)
button_name_suffix = tk.Checkbutton(tag1, textvariable=label_name_suffix, variable=var_name_suffix, onvalue=1, offvalue=0, state='disable', command=func_number)
button_name_suffix.place(x=tag1_x0+250, y=tag1_y0+10+90)
label_no_number = tk.StringVar()
label_no_number.set(r"Don't need number")
var_no_number = tk.IntVar()  # 定义变量用来存放选择行为返回值
var_no_number.set(1)
button_no_number = tk.Checkbutton(tag1, textvariable=label_no_number, variable=var_no_number, onvalue=1, offvalue=0, command=func_number)    # 传值原理类似于radiobutton部件
button_no_number.place(x=tag1_x0, y=tag1_y0+10+100)

# NFT价格  ## 确定nft价格输入最大范围值，并仅能输入数字
label_nft_price = tk.StringVar()
label_nft_price.set(r'NFT Price(ETH) :')
tk.Label(tag1, text='*', font=('Arial', 12)).place(x=tag1_x0, y=tag1_y0+10+140)
tk.Label(tag1, textvariable=label_nft_price, font=('Arial', 12)).place(x=tag1_x0+10, y=tag1_y0+10+140)
var_nft_price = tk.StringVar()
entry_nft_price = tk.Entry(tag1, textvariable=var_nft_price, font=('Arial', 12)).place(x=tag1_x0+150, y=tag1_y0+10+140, width=100)

# 开始按键
label_start = tk.StringVar()
label_start.set(r'Start')
button_start = tk.Button(tag1, textvariable=label_start, font=('Arial', 17), width=10, height=1, command=func_start).place(x=tag1_x0+60, y=tag1_y0+10+200)
#label_enter_password = tk.StringVar()
#label_enter_password.set(r'Entered Password')
#button_enter_password = tk.Button(tag1, textvariable=label_enter_password, font=('Arial', 15), width=20, height=1, command=func_start, state='disable')
#button_enter_password.place(x=tag1_x0+220, y=tag1_y0+10+200)

# 第一次使用按键
label_first = tk.StringVar()
label_first.set(r"For the first time")
var_first = tk.IntVar()  # 定义变量用来存放选择行为返回值
button_first = tk.Checkbutton(tag1, textvariable=label_first, variable=var_first, onvalue=1, offvalue=0, command=func_first)    # 传值原理类似于radiobutton部件
button_first.place(x=tag1_x0+50, y=tag1_y0+10+250)
label_first_color = tk.StringVar()
label_first2 = tk.StringVar()
label_first2.set(r"When the select wallet page appears in the browser,")
lab_first2 = tk.Label(tag1, textvariable=label_first2, font=('Arial', 12), fg='#F0F0F0')
lab_first2.place(x=tag1_x0+50, y=tag1_y0+10+280)
label_first3 = tk.StringVar()
label_first3.set(r"the user needs to log in and enter Wallet Seed.")
lab_first3 = tk.Label(tag1, textvariable=label_first3, font=('Arial', 12), fg='#F0F0F0')
lab_first3.place(x=tag1_x0+50, y=tag1_y0+10+305)

# 创建第二页框架，可选操作
tag2 = tk.Frame(tag_main)
tag2.place(x=0, y=0)
tag_main.add(tag2, text='More options')

# 定义初始坐标
tag2_x0, tag2_y0 = 10, 10

# 块链选择功能
label_blockchain = tk.StringVar()
label_blockchain.set(r'Blockchain :')
tk.Label(tag2, textvariable=label_blockchain, font=('Arial', 12)).place(x=tag2_x0+80, y=tag2_y0+20)
var_blockchain = tk.StringVar()
var_blockchain.set(r'Ethereum')
button_blockchain_ethereum = tk.Radiobutton(tag2, text='Ethereum', variable=var_blockchain, value='Ethereum', command=func_blockchain).place(x=tag2_x0+210, y=tag2_y0+20)
button_blockchain_polygon = tk.Radiobutton(tag2, text='Polygon', variable=var_blockchain, value='Polygon', command=func_blockchain).place(x=tag2_x0+310, y=tag2_y0+20)

label_supply = tk.StringVar()
label_supply.set(r'Supply :')
tk.Label(tag2, textvariable=label_supply, font=('Arial', 12)).place(x=tag2_x0+80, y=tag2_y0+50)
var_supply = tk.StringVar()
var_supply.set('1')
entry_supply = tk.Entry(tag2, textvariable=var_supply, font=('Arial', 12), state='disable')
entry_supply.place(x=tag2_x0+210, y=tag2_y0+50, width=100)

tk.Label(tag2, text='Trying to write code', font=('Arial', 15)).place(x=tag2_x0+170, y=tag2_y0+240)
tk.Label(tag2, text='Please wait patiently', font=('Arial', 15)).place(x=tag2_x0+170, y=tag2_y0+270)

# 第9步，定义数据类型并读取文件数据
try:
    fileread = open('dataFile.txt', 'rb')
    datalist_rb = pickle.load(fileread)
    var_condition = datalist_rb[0]
    var_language = datalist_rb[1]
    if var_language == 'chinese':
        func_menu_chinese()
    var_chrome_path.set(datalist_rb[2])
    var_metamask_password.set(datalist_rb[3])
    var_password_choice.set(datalist_rb[4])
    func_password_choice()
    var_nft_path.set(datalist_rb[5])
    var_coll_name.set(datalist_rb[6])
    var_nft_name.set(datalist_rb[7])
    var_nft_number.set(datalist_rb[8])
    var_add_number.set(datalist_rb[9])
    var_name_suffix.set(datalist_rb[10])
    var_no_number.set(datalist_rb[11])
    func_number()
    var_nft_price.set(datalist_rb[12])
    var_first.set(datalist_rb[13])
    var_blockchain.set(datalist_rb[14])
    var_supply.set(datalist_rb[15])
    func_blockchain()
    func_first()
except:
    print('Save Error')

window.mainloop()