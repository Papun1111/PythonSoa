n=int(input("Enter number of students:"))
diction={}
for i in range(0,n):
    name=input(f"Enter student {i+1} name:")
    marks=[]
    for i in range(1,4):
        b=int(input(f"enter marks: {i}:"))
        marks.append(b)
    
    diction.update({name:marks})


print(diction)
