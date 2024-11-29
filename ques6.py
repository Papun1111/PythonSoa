a=[]
n=int(input("Enter size of the list"))
for i in range(0,n):
    b=int(input("Enter a number to add to list:"))
    a.append(b)
c=int(input("enter the number to be searched"))
count=0
for i in a:
    if i==c:
        count+=1

if(count>0):
    print(f"the number exists for count of {count}")