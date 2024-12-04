s=input("Enter a string:")
diction={}
for i in s:
    count=s.count(i)
    diction.update({i:count})
print(diction)
