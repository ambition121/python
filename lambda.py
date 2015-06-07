#!/usr/bin/python 
#coding:utf8

print '='*20
def f(x):	#阶乘的一个程序,根据我们的输入打印出阶乘
	if x==1 or x==0:
		return 1
	if x>1:
		return x*f(x-1)
n=input('Enter n:')
print f(n)

print '='*20
l=range(1,11)	#用内建的reduce函数实现阶乘 固定10的阶乘
def fun(x,y):
	return x*y
print reduce(fun,l)

print '='*20	# 使用lambda这个内建函数
g=lambda x,y:x*y
print g(2,3)
