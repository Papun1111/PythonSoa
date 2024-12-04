number=input("enter a number")
length=len(number)
number=int(number)



def isArmstrong(number):
    n=number
    s=0
    while n>0:
        d=n%10
        s+=pow(d,length)
        n//=10
    return s==number

if(isArmstrong):
    print("Number is Armstrong")

else:
    print("Number is not Armstrong")


           
       
        
        
