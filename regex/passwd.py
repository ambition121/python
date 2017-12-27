#!python2
import re

def password(inputpass):
	if len(inputpass) < 8:
		return False
	m1 = re.compile(r'[0-9]{1,}')
	if m1.search(inputpass) == None:
		return False

	m2 = re.compile(r'[a-z]{1,}')
	if m2.search(inputpass) == None:
		return False

	m3 = re.compile(r'[A-Z]{1,}')
	if m3.search(inputpass) == None:
		return False

	return True

print('please input you password')
for i in range(6):
	yourpassword = raw_input()
	if password(yourpassword) == True:
		print('you input password is ok')
		break
	else:
		print('reinput you password')

if password(yourpassword) == True:
	print('Thank you for input the ok password')
else:
	print('you could not input right password in 6 times')