# author:吴紫葳
# times:2020/8/12 15:25
# # coding:-*- utf-8 -*-

import time
import datetime


def time_stamp(times):
    """时间秒级转换时间戳"""
    # 字符类型的时间
    tss1 = times
    # 转为时间数组
    timeArray = time.strptime(tss1, "%Y-%m-%d %H:%M:%S")
    # 转为时间戳
    timeStamp = int(time.mktime(timeArray))
    print(timeStamp)


def times_data(times):
    timeStamp = times
    dateArray = datetime.datetime.utcfromtimestamp(timeStamp)
    otherStyleTime = dateArray.strftime("%Y-%m-%d %H:%M:%S")
    print(otherStyleTime)


if __name__ == '__main__':
    # time_stamp('')
    times_data(1381419600)
