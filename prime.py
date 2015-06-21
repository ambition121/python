#!/usr/bin/env python
#coding:utf8
import math
for i in range(50, 100 + 1): #主要求50到100之间的素数
    for j in range(2, int(math.sqrt(i)) + 1): 
        if i % j == 0:
            break
    else:
        print i

