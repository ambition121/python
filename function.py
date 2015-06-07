#!/usr/bin/python 
#coding:utf8

def fun(x):
	print x
z=fun(5)
print z #默认返回是None


y=sum([1,2,3,4]) #sum默认返回的是求出到结果
print y


def add(a,b):
	print 'welcome!'
	return a+b
c=add(5,6)
print c     # 返回是return传过来的，这里是数字


def f():
	return 'hello!'
	return 'world'  #这里第二条return并未执行，第一条执行就结束了
d=f()
print d    # 这里是d接收return传过来的字符串（还可以是列表，元组，字典等类型）
