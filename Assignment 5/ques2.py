n=int(input("Enter number of students:"))
diction={}
for i in range(0,n):
    name=input(f"Enter student {i+1} name:")
    b=int(input(f"enter percenatage :"))
    diction.update({name:b})


print(diction)

