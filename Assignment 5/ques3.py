diction={}
a=[]
for i in range(1,4):
    b=int(input(f"Enter value {i}:"))
    a.append(b)
diction.update({1:a})
sum=0
for i in diction.values():
    for j in i:
        sum+=j
print(sum)
    
