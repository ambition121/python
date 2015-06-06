#1/usr/bin/python
def change(n): # change (xiang dang yu liang ge bian liang tong shi yin yong yi ge lie biao)
	n[0]='zhang'
names=['wang','li']
change(names)
print names

def try_to_change(n): # no change(han shu nei can shu fu xin zhi bu hui gai bian wai bu lian liang de zhi)
	n='nihao'
name='hello'
try_to_change(name)
print name

def try_change(n): # no change (qie pian xiang dang yu yi ge fu ben)
	n[0]='liu'
namess=['wang','li']
try_change(namess[:])
print namess
