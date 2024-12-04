def tuptup(tup):
    sum=0
    for i in tup:
        for j in i:
            sum+=j
    return sum

tup=((1,2,3,4),(1,2,3,4),(1,2,3,4))
sum=tuptup(tup)
print(sum)