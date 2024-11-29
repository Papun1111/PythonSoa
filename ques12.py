l=[[1,2,3],[4,5,6],[7,8,9]]

def sumofr(l,r,c):
    sum=0
    for i in range(0,r+1):
        for j in range(0,c):
            sum+=l[i][j]
    return sum

for i in range(0,3):
    sum=0
    for j in range(0,3):
        sum+=sumofr(l,i,3)
        print(f"{l[i][j]}",end=" ")
    print(sum)