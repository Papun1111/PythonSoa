n=int(input("Enter a number"))
sum=0
for i in range(1,n,1):
    if n%i==0:
        sum+=i

if(n==sum):
    print("number is perfect")
else:
    print("Number is not Perfect")    
# Enter a number6
# number is perfect