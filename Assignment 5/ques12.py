s=input("Enter a string:")
diction={}
for i in s:
    count=s.count(i)
    diction.update({i:count})
print("List of all duplicate elements are:")
for i,j in diction.items():
    if j>1:
        print(i,end=" ")
        
