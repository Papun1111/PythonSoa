s=input("Enter a string: ")
se=set(s)
print(se)
count=0
for i in se:
    count+=1
print(f"total number of unique character the string {s} has is {count}")
