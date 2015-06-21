#!/usr/bin/env python 
#coding:utf8
def maxfactor(num):
    count = num/2 #从num的一半开始计数
    while count>1:
        if num % count ==0:
            print 'the largest factor of %d is %d' % (num,count)
            break
        count -=1

    else:
        print num, 'is prime'

for eachnum in range(10,20):
    maxfactor(eachnum)
#首先是从num的一半count计数，看是否能被2整除，如果能整除那么count就是最大约数，否则循环递减1，如果循环到1还没发现约数，那么就是素数，上面是10到20之间的数的情况

