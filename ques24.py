loft=[(1,2,3),(4,5),(5,6,7,8)]

k=int(input("Enter length:"))
count=0
for i in loft:
    if len(i)==k:
        loft.pop(count)
    count+=1
print(loft)
