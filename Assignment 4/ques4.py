l=["papun","naka","prateek","Laksh","papun","prateek"]
o=input("enter the name who  want to remove")
count=0
for i in l:
    if i==o:
        count+=1

for i in range(0,count):
    l.remove(o)
print(l)