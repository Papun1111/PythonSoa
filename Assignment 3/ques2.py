def isDivisible(num):
    if(num%3==0 and num%5==0):
        return True
    else:
        False

for i in range(100,501,1):
    num=isDivisible(i)
    if(num):
        print(i)