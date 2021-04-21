import os
import time

def get_files(pics_path):
    listdir = os.listdir(pics_path)
    filepath = os.getcwd()
    allfile = []
    for file in listdir:
        allfile.append(filepath + '\\' + pics_path + '\\' + file)
    return allfile
    #print(allfile)

a = get_files(r"pic")
for i in a:
    print(i)