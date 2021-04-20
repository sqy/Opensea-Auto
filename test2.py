import os


def getabsroute(path):
    listdir = os.listdir(path)
    filepath = os.getcwd()
    allfile = []
    for file in listdir:
        allfile.append(filepath + '\\' + file)
    return allfile
    #print(allfile)


print(getabsroute(r"pic"))
print(getabsroute(r"pic")[0])
print(getabsroute(r"pic")[1])