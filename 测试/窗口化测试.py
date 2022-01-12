import tkinter as tk

# 第1步，实例化object，建立窗口window
window = tk.Tk()

# 第2步，给窗口的可视化起名字
window.title("Welcome to sqy'code ")

# 第3步，设定窗口的大小(长 * 宽)
window.geometry('500x900')

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
    except:
        pass

# NFT编号，编号自动增加
def func_add_number():
    if var_add_number.get() == 1:  # 如果选中
        print("I'm writing")
    elif var_add_number.get() == 0:  # 如果未选中
        print("I'm writing")

# NFT编号，编号作为名称后缀
def func_name_suffix():
    if var_name_suffix.get() == 1:  # 如果选中
        print("I'm writing")
    elif var_name_suffix.get() == 0:  # 如果未选中
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

# 第6步，浏览器相关信息
tk.Label(window, text='*', font=('Arial', 12)).place(x=10, y=200)
tk.Label(window, text='Chrome Profile path :', font=('Arial', 12)).place(x=20, y=200)
var_chrome_path = tk.StringVar()
entry_chrome_path = tk.Entry(window, textvariable=var_chrome_path, font=('Arial', 12)).place(x=10, y=230, width=430)

# 第6步，NFT相关信息
# 定义初始坐标
x0, y0 = 10, 350

# 收藏夹名称
tk.Label(window, text='*', font=('Arial', 12)).place(x=x0, y=y0)
tk.Label(window, text='Collection Name :', font=('Arial', 12)).place(x=x0+10, y=y0)
var_coll_name = tk.StringVar()
entry_coll_name = tk.Entry(window, textvariable=var_coll_name, font=('Arial', 12)).place(x=x0+150, y=y0, width=300)

# NFT名称
tk.Label(window, text='*', font=('Arial', 12)).place(x=x0, y=y0+40)
tk.Label(window, text='NFT Name :', font=('Arial', 12)).place(x=x0+10, y=y0+40)
var_nft_name = tk.StringVar()
entry_nft_name = tk.Entry(window, textvariable=var_nft_name, font=('Arial', 12)).place(x=x0+150, y=y0+40, width=300)

# NFT编号
tk.Label(window, text='NFT Number :', font=('Arial', 12)).place(x=x0+10, y=y0+80)
var_nft_number = tk.StringVar()
entry_nft_number = tk.Entry(window, textvariable=var_nft_number, font=('Arial', 12)).place(x=x0+150, y=y0+80, width=100)
# 定义两个Checkbutton选项并放置
var_add_number = tk.IntVar()  # 定义var1和var2整型变量用来存放选择行为返回值
var_name_suffix = tk.IntVar()
button_add_number = tk.Checkbutton(window, text='Increased by one for each NFT', variable=var_add_number, onvalue=1, offvalue=0, command=func_add_number).place(x=x0+250, y=y0+70)    # 传值原理类似于radiobutton部件
button_name_suffix = tk.Checkbutton(window, text='Add number to NFT name as suffix', variable=var_name_suffix, onvalue=1, offvalue=0, command=func_name_suffix).place(x=x0+250, y=y0+90)

# NFT价格
tk.Label(window, text='*', font=('Arial', 12)).place(x=x0, y=y0+120)
tk.Label(window, text='NFT Price(ETH) :', font=('Arial', 12)).place(x=x0+10, y=y0+120)
var_nft_price = tk.StringVar()
entry_nft_price = tk.Entry(window, textvariable=var_nft_price, font=('Arial', 12)).place(x=x0+150, y=y0+120, width=100)

# 可选操作

window.mainloop()