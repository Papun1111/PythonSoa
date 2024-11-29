print("a. Create a list of N integers:")
print("b.Display the list elements:")
print("c.Insert an element at a specific position:")
print("d.Delete an element at a given position:")
print("e.Exit")
list=[]

a=True
while a:
    choice=input("Enter your choice:")
    if(choice=='a'):
        N=int(input("enter N:"))
        
        for i in range(1,N+1,1):
            b=int(input("enter number:"))
            list.append(b)
    elif choice=='b':
        for i in list:
            print(i,end=",")
        print()
    elif choice=='c':
        pos=int(input("Enter position:"))
        ele=pos=int(input("Enter element:"))
        list.insert(pos,ele)
    elif choice=='d':
        pos=int(input("Enter position:"))
        list.pop(pos)
    elif choice=='e':
        a=False
    else:
        print("Error")
        



