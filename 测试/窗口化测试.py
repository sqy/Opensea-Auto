import tkinter as tk
import tkinter.ttk as ttk
# 第1步，实例化object，建立窗口window
window = tk.Tk()

# 第2步，给窗口的可视化起名字
window.title("Welcome to sqy'code ")

# 第3步，设定窗口的大小(长 * 宽)
window.geometry('520x700')

# 第4步，定义触发函数功能
# 菜单File,New功能
def func_menu_new():
    print("I'm writing")

# 菜单File,New功能
def func_menu_open():
    print("I'm writing")

# 菜单File,New功能
def func_menu_save():
    print("I'm writing")

# 菜单Language,Chinese
def func_menu_chinese():
    try:
        menubar.entryconfig(index='File', label='文件')
        filemenu.entryconfig(index='New', label='新建')
        filemenu.entryconfig(index='Open', label='打开')
        filemenu.entryconfig(index='Save', label='保存')
        filemenu.entryconfig(index='Exit', label='退出')
        label_chrome_path.set(r'Chrome浏览器个人资料路径 :')
        label_metamask_password.set(r'Metamask钱包密码:')
        label_password_choice.set(r'我自己来输入密码')
        label_coll_name.set(r'收藏夹名称 :')
        label_nft_name.set(r'NFT 名称 :')
        label_nft_number.set(r'NFT 编号 :')
        label_add_number.set(r'每上架一个NFT，编号加1')
        label_name_suffix.set(r'将编号作为NFT名称后缀')
        label_no_number.set(r'不需要NFT编号')
        label_nft_price.set(r'NFT 价格(ETH) :')
        label_start.set(r'开始')
        label_enter_password.set(r'已输入密码')
        tag_main.tab(0, text='常规')
        tag_main.tab(1, text='更多选项')
    except:
        pass

# 菜单Language,English
def func_menu_english():
    try:
        menubar.entryconfig(index='文件', label='File')
        filemenu.entryconfig(index='新建', label='New')
        filemenu.entryconfig(index='打开', label='Open')
        filemenu.entryconfig(index='保存', label='Save')
        filemenu.entryconfig(index='退出', label='Exit')
        label_chrome_path.set(r'Chrome Profile path :')
        label_metamask_password.set(r'Metamask Password :')
        label_password_choice.set(r'Enter the password by myself')
        label_coll_name.set(r'Collection Name :')
        label_nft_name.set(r'NFT Name :')
        label_nft_number.set(r'NFT Number :')
        label_add_number.set(r'Increased by one for each NFT')
        label_name_suffix.set(r'Add number to NFT name as suffix')
        label_no_number.set(r"Don't need number")
        label_nft_price.set(r'NFT Price(ETH) :')
        label_start.set(r'Start')
        label_enter_password.set(r'Entered Password')
        tag_main.tab(0, text='General')
        tag_main.tab(1, text='More options')
    except:
        pass
# Metamask钱包密码，自己输入
def func_password_choice():
    if var_password_choice.get() == 1:
        var_metamask_password.set('')
        entry_metamask_password.config(state='disable')
    else:
        entry_metamask_password.config(state='normal')

# NFT编号，编号自动增加，编号作为名称后缀，不需要NFT编号
def func_number():
    if var_no_number.get() == 1:
        button_add_number.deselect()
        button_name_suffix.deselect()
        var_nft_number.set('')
        entry_nft_number.config(state='disable')
    else:
        entry_nft_number.config(state='normal')
        if var_add_number.get() == 1:
            print("I'm writing")
        elif var_name_suffix.get() == 1:
            print("I'm writing")
# 开始按键
def func_start():
    print("I'm writing")

# 链选择
def func_blockchain():
    print("I'm writing")

# 第5步，创建菜单栏
menubar = tk.Menu(window)
# 创建一个File菜单项
filemenu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label='File', menu=filemenu)
# 在File中加入New、Open、Save等小菜单
filemenu.add_command(label='New', command=func_menu_new)
filemenu.add_command(label='Open', command=func_menu_open)
filemenu.add_command(label='Save', command=func_menu_save)
filemenu.add_separator()    # 添加一条分隔线
filemenu.add_command(label='Exit', command=window.quit)  # 用tkinter里面自带的quit()函数

# 创建一个Language菜单项
langmenu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label='语言/Language', menu=langmenu)
# 在language中加入小菜单
langmenu.add_command(label='中文', command=func_menu_chinese)
langmenu.add_command(label='English', command=func_menu_english)
# 配置菜单
window.config(menu=menubar)

# 创建主分页签
tag_main = ttk.Notebook(window)
tag_main.place(x=0, y=170, width=520, height= 500)
#bg='#F0F0F0',
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

# 第8步，NFT相关信息
# 收藏夹名称
label_coll_name = tk.StringVar()
label_coll_name.set(r'Collection Name :')
tk.Label(tag1, text='*', font=('Arial', 12)).place(x=tag1_x0, y=tag1_y0)
tk.Label(tag1, textvariable=label_coll_name, font=('Arial', 12)).place(x=tag1_x0+10, y=tag1_y0)
var_coll_name = tk.StringVar()
entry_coll_name = tk.Entry(tag1, textvariable=var_coll_name, font=('Arial', 12)).place(x=tag1_x0+150, y=tag1_y0, width=330)

# NFT名称
label_nft_name = tk.StringVar()
label_nft_name.set(r'NFT Name :')
tk.Label(tag1, text='*', font=('Arial', 12)).place(x=tag1_x0, y=tag1_y0+40)
tk.Label(tag1, textvariable=label_nft_name, font=('Arial', 12)).place(x=tag1_x0+10, y=tag1_y0+40)
var_nft_name = tk.StringVar()
entry_nft_name = tk.Entry(tag1, textvariable=var_nft_name, font=('Arial', 12)).place(x=tag1_x0+150, y=tag1_y0+40, width=330)

# NFT编号
label_nft_number = tk.StringVar()
label_nft_number.set(r'NFT Number :')
tk.Label(tag1, textvariable=label_nft_number, font=('Arial', 12)).place(x=tag1_x0+10, y=tag1_y0+80)
var_nft_number = tk.StringVar()
entry_nft_number = tk.Entry(tag1, textvariable=var_nft_number, font=('Arial', 12), state='disable')
entry_nft_number.place(x=tag1_x0+150, y=tag1_y0+80, width=100)

# 定义两个Checkbutton选项并放置
label_add_number = tk.StringVar()
label_name_suffix = tk.StringVar()
label_add_number.set(r'Increased by one for each NFT')
label_name_suffix.set(r'Add number to NFT name as suffix')
var_add_number = tk.IntVar()  # 定义变量用来存放选择行为返回值
var_name_suffix = tk.IntVar()  # 定义变量用来存放选择行为返回值
button_add_number = tk.Checkbutton(tag1, textvariable=label_add_number, variable=var_add_number, onvalue=1, offvalue=0, command=func_number)    # 传值原理类似于radiobutton部件
button_add_number.place(x=tag1_x0+250, y=tag1_y0+70)
button_name_suffix = tk.Checkbutton(tag1, textvariable=label_name_suffix, variable=var_name_suffix, onvalue=1, offvalue=0, command=func_number)
button_name_suffix.place(x=tag1_x0+250, y=tag1_y0+90)
label_no_number = tk.StringVar()
label_no_number.set(r"Don't need number")
var_no_number = tk.IntVar()  # 定义变量用来存放选择行为返回值
var_no_number.set(1)
button_no_number = tk.Checkbutton(tag1, textvariable=label_no_number, variable=var_no_number, onvalue=1, offvalue=0, command=func_number)    # 传值原理类似于radiobutton部件
button_no_number.place(x=tag1_x0, y=tag1_y0+100)

# NFT价格
label_nft_price = tk.StringVar()
label_nft_price.set(r'NFT Price(ETH) :')
tk.Label(tag1, text='*', font=('Arial', 12)).place(x=tag1_x0, y=tag1_y0+140)
tk.Label(tag1, textvariable=label_nft_price, font=('Arial', 12)).place(x=tag1_x0+10, y=tag1_y0+140)
var_nft_price = tk.StringVar()
entry_nft_price = tk.Entry(tag1, textvariable=var_nft_price, font=('Arial', 12)).place(x=tag1_x0+150, y=tag1_y0+140, width=100)

# 开始按键
label_start = tk.StringVar()
label_start.set(r'Start')
button_start = tk.Button(tag1, textvariable=label_start, font=('Arial', 15), width=10, height=1, command=func_start).place(x=tag1_x0+60, y=tag1_y0+200)
label_enter_password = tk.StringVar()
label_enter_password.set(r'Entered Password')
button_enter_password = tk.Button(tag1, textvariable=label_enter_password, font=('Arial', 15), width=20, height=1, command=func_start).place(x=tag1_x0+220, y=tag1_y0+200)

# 创建第二页框架，可选操作
tag2 = tk.Frame(tag_main)
tag2.place(x=0, y=0)
tag_main.add(tag2, text='More options')

# 定义初始坐标
tag2_x0, tag2_y0 = 10, 10

label_blockchain = tk.StringVar()
label_blockchain.set(r'Blockchain :')
tk.Label(tag2, textvariable=label_blockchain, font=('Arial', 12)).place(x=tag2_x0+80, y=tag2_y0+20)
var_blockchain = tk.StringVar()
var_blockchain.set(r'Ethereum')
button_blockchain_ethereum = tk.Radiobutton(tag2, text='Ethereum', variable=var_blockchain, value='Ethereum', command=func_blockchain).place(x=tag2_x0+210, y=tag2_y0+20)
button_blockchain_polygon = tk.Radiobutton(tag2, text='Polygon', variable=var_blockchain, value='Polygon', command=func_blockchain).place(x=tag2_x0+310, y=tag2_y0+20)

tk.Label(tag2, text='Trying to write code', font=('Arial', 15)).place(x=tag2_x0+170, y=tag2_y0+240)
tk.Label(tag2, text='Please wait patiently', font=('Arial', 15)).place(x=tag2_x0+170, y=tag2_y0+270)

window.mainloop()