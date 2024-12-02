l=[[1,2,3,4],[4,5,6,5],[7,8,9,6]]
sum=[]
sumc=0
def sumcol(l,i):
    sum=0
    for j in range(0,3):
        sum+=l[j][i]
    return sum
for i in range(0,4):
    sumc=sumcol(l,i)
    sum.append(sumc)
    sumc=0
print(sum)


