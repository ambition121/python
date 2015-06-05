#!/usr/bin/python

people={
	'zhang':{'phone':'1234','addr':'the long road'},
	'wang':{'phone':'5678','addr':'corner of rouad'},
	'li':{'phone':'7890','addr':'unknow'}
}
labels={'phone':'phonenumber','addr':'address'} 

name=raw_input('Name:')
request=raw_input('phone number(p) or address(a)?')

if request=='p':key='phone'
if request=='a':key='addr'

if name in people:print "%s's %s is %s"%\
	   (name,labels[key],people[name][key])
