s=input("Enter a string:")
diction={}
for i in s:
    if i=='a' or i=='e' or i=='i' or i=='o' or i=='u':
        count=s.count(i)
        diction.update({i:count})
for i,j in diction.items():
    print(i,j)
