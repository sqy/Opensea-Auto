import time


time_begin = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
print(time_begin)
struct_time1 = time.strptime(time_begin, '%Y-%m-%d %H:%M:%S')
time.sleep(5)
time_now = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
print(time_now)

#n1 = '2019-07-18 20:07:56'
#n2 = '2019-07-19 22:03:12'
# 格式化时间转换为结构化时间
struct_time2 = time.strptime(time_now, '%Y-%m-%d %H:%M:%S')
# 结构化时间转换为时间戳格式
struct_time1, struct_time2 = time.mktime(struct_time1), time.mktime(struct_time2)
#struct_time1, struct_time2 = time.mktime(time_begin), time.mktime(time_now)
# 差的时间戳
diff_time = struct_time2 - struct_time1
# 将计算出来的时间戳转换为结构化时间
struct_time = time.gmtime(diff_time)
# 减去时间戳最开始的时间 并格式化输出
print('过去了{0}年{1}月{2}日{3}小时{4}分钟{5}秒'.format(
    struct_time.tm_year - 1970,
    struct_time.tm_mon - 1,
    struct_time.tm_mday - 1,
    struct_time.tm_hour,
    struct_time.tm_min,
    struct_time.tm_sec
))

if struct_time.tm_sec > 4:
    print('fuck')