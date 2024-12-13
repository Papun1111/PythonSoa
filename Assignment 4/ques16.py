list=[]
for i in range(10):
    list.append(int(input("Enter a number : ")))

a=True
for i in range(0,9):
    if list[i]<list[i+1]:
        pass
    else:
        a=False
print(a)