import os


def getabsroute(path):
    listdir = os.listdir(path)
    filepath = os.getcwd()
    allfile = []
    for file in listdir:
        allfile.append(filepath + '\\' + file)
    print(allfile)

def get_files(path):
    abs_path = getabsroute(path)
    Filelist = []
    # os.walk()用类似于深度遍历的方式遍历文件夹中的子文件夹以及文件。
    # 最基本的显示方式为(root_path,[file_dirs],[files]),
    for home, dirs, files in os.walk(abs_path):
        for file in files:
            Filelist.append(os.path.join(home, file))
            #Filelist.append(file)
    return Filelist

list = get_files(r"pic")
print(list)