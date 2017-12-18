import random
i = random.randint(1,50)
'''
while True:
    print 'input you num'
    number = int(input())
    if number == i:
        print 'good job,the num is '+str(number)
        break
    if number < i:
        print 'your input is low'
    if number > i:
        print 'your input is high'
'''
for i in range(7):
    print 'input you num'
    number = int(input())
    if number < i:
        print 'your input is low'
    if number > i:
        print 'your input is high'
    else:
        break
if number == i:
    print 'you are in 6 times to find the num,the number is '+str(i)
else:
    print '......you lost the num is '+str(i)

