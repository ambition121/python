valid=False
count=3
passwordlist=('123','234','456','567')

while count>0:
    
    password=raw_input("Enter your the num's password:")
    for num in passwordlist:
        if password == num:
            valid=True
            print 'right'
            break
    if not valid:
            print "invalid password"
            count -=1 
            continue
    else:
        break

