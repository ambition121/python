#!/usr/bin/python
fibs=[0,1]
num=input('How many Fibonacci num do you want?:')
if num>=2: 
	for i in range(num-2):
		fibs.append(fibs[-2]+fibs[-1])
else:
	print 'wrong num'
	exit()
print fibs
