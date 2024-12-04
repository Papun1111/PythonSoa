for i in range(0,5,1):
    for j in range(0,i,1):
        print("*",end="")
    print()    

for i in range(5,0,-1):
    for b in range(0,i,1):
        print(" ",end="")
    for j in range(5,i,-1):
        print("*",end="")
    print()         
print() 
for i in range (0,5):
    for b in range(0,i):
        print(" ",end="")
    for j in range(5,i+1,-1):
        print("*",end="")
    print()   
print()  
for i in range(5,0,-1):
    for j in range(5,i,-1):
        print(" ",end="")
    for j in range(0,i):
        print("* ",end="")
    print()    

for i in range(0,5):
    for j in range(5,i+1,-1):
        print("*",end="")
    print()   
print()        


for i in range(1, 5):
    print(" " * (4 - i) + "*" * (2 * i - 1))
for i in range(3, 0, -1):
    print(" " * (4 - i) + "*" * (2 * i - 1))


for i in range(0,4,1):
    for b in range(4,i,-1):
        print(" ",end="")       
    print("*",end=" ")
    for j in range(0,i,1):
         print(" ",end="")
    for j in range(0,i,1):
         print(" ",end="")       
    print("*")
for i in range(0,11,1):
    print("*",end="")   
print()
for i in range(6):
    for j in range(6 - i):
        print(j, end=" ")
    print()




for i in range(7):
    for j in range(5):
        if i == 0 or i == 6 or j == 0 or j == 4:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()  

n = 7  

for i in range(n):
    for j in range(n):
        if i + j == n // 2 or \
           i - j == n // 2 or \
           j - i == n // 2 or \
           i + j == n + n // 2 - 1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()  

for i in range(1,10,2):
    for j in range (1,i+1,2):
        print(i,end="")
    print()    

n = 5  
for i in range(1, n + 1):
    for j in range(i, 0, -1):
        print(j, end=" ")
    print()    

n = 5 

for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(i * j, end=" ")
    print()


rows = 6 
current_char = ord('A') 

for i in range(1, rows + 1):
    for j in range(i):
        print(chr(current_char), end=" ")
        current_char += 1
        if current_char > ord('Z'):  
            current_char = ord('A')
    print()    

rows = 5

for i in range(1, rows + 1):
    print(" " * (rows - i), end="")
    
    for j in range(i, 0, -1):
        print(j, end=" ")
    
    for j in range(2, i + 1):
        print(j, end=" ")
    
    print()