#!/usr/bin/python
#coding:utf8
print '='*30
# 传递的实参和所定义的形参相同情况
def f(x,y):
	print '%s:%s' % (x,y)

t=('name','age')
f(*t)	#把元组的值传过来

def fun(name='name',age='20'):
	print 'name:%s'% name
	print 'age:%s'% age

fun('zhang',30) #用的是我们输入的参数
fun()  #用的是默认参数

fun(40,'wang')	#这只和顺序有关，前面第一对应第一个，第二个对应第二个


d={'name':'lily','age':18}#定义一个字典,字典中的键值key应该和形参一样
fun(**d)	#把字典的值传过来

d1={'n':'xiaoming','a':12}
fun(d1['n'],d1['a'])	#如果字典中的键值和函数中的形参不一样的时候

print '='*30
# 当传递的实参和所定义的形参不相同情况，冗余参数
def f(x,*args,**kwargs):
	print x
	print args
	print kwargs
f(1)
f(1,2,3,4,5)
f(x=1,y=2)
f(1,2,3,4,5,y=20,z=30)	#其中1传递给x，2，3，4，5传递给元组，y=20，z=30传递给字典
