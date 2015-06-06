#!/usr/bin/python
x=''
while x != 'q':
	print 'hello'
	x = raw_input('Enter q to quit:')
	if not x:
		break
	if x == 'c':
		continue
	print 'one more time....'
else:
	print 'end....'
