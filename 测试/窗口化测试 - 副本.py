# pickle模块主要函数的应用举例
import pickle
import pprint

dataList = [[8, 1, 'python'],
            [8, 1, 'python'],
            [8, 0, 'python'],
            [8, 1, 'C++'],
            [8, 1, 'C++']]
dataDic = {0: [1, 2, 3, 4],
           1: ('a', 'b'),
           2: {'c': 'yes', 'd': 'no'}}
print("原始数据dataList：")
pprint.pprint(dataList)
print('\n')
print("原始数据dataDic：")
pprint.pprint(dataDic)

# 使用dump()将数据序列化到文件中
fw = open('dataFile.txt', 'wb')
# Pickle the list using the highest protocol available.
pickle.dump(dataList, fw)
# Pickle dictionary using protocol 0.
pickle.dump(dataDic, fw)
fw.close()

# 使用load()将数据从文件中序列化读出
fr = open('dataFile.txt', 'rb')
data1 = pickle.load(fr)
print('\n'+"反序列化1：%r" % data1)
data3 = pickle.load(fr)
print("反序列化3：%r" % data3 + '\n')
fr.close()

# 使用dumps()和loads()举例
p = pickle.dumps(dataList)
print(pickle.loads(p))
p = pickle.dumps(dataDic)
print(pickle.loads(p))