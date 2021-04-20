import os
import time

def get_files(pics_path):
    listdir = os.listdir(pics_path)
    filepath = os.getcwd()
    allfile = []
    for file in listdir:
        allfile.append(filepath + '\\' + path + '\\' + file)
    return allfile
    #print(allfile)

print(os.getcwd())
print(get_files(r"pic"))
print(get_files(r"pic")[0])
print(get_files(r"pic")[1])

