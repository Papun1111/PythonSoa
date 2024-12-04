n=int(input("Enter number of you want to enter: "))
lis=[]
def uniqueWordlexi(lis):
    for i in range(0,len(lis)):
        lis[i]=lis[i].lower()
    se=set(lis)
    lis=list(se)
    lis.sort()
    for i in lis:
        print(i,end=" ")
for i in range(0,n):
    lis.append(input("enter a word:"))

uniqueWordlexi(lis)

