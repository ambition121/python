#!/usr/local/bin/python3.4
# 检查用户名和pin
data=[
	['lilei','1'],
	['hanlei','2'],
	['lily','3']
]
username=input('user:')
pin=input('pin code:')
if[username,pin] in data:print ('you are right!')
