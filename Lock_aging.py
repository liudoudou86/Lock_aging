#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:lz
# Description:一键全开所有锁次数老化

import time

import serial
from loguru import logger


def lock():
 
    ser = serial.Serial("COM3", 9600, timeout=0.5)
    ser.flushInput() # 清空缓冲区
    command=bytes([0xFA, 0xFA, 0x09, 0x00, 0x91, 0x00, 0x00, 0x00, 0x20, 0x3A, 0xFD, 0xFD])
    ser.write(command) # 一键开锁
    ser.close()

time_tup=time.localtime(time.time()) # 获取当前时间
format_time="%Y-%m-%d_%H-%M-%S"
cur_time=time.strftime(format_time,time_tup)
 
if __name__ == '__main__':

    logger.add('log_{}.txt'.format(cur_time), rotation="100 MB") # 将日志输出到txt文本中
    count = 0
    for i in range (0, 1000): # 对函数做循环
        lock()
        time.sleep(3) # 3秒缓冲
        count += 1
        logger.info("已完成 --- > 第" + str(count) + "次")

