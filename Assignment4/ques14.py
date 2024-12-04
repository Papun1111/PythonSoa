tup = ()
for i in range(10):
    number=int(input("enter a number"))
    tup += (number,)  

def gensquaretype(tup):
    newtup=tuple(map(lambda a:a**2,tup))
    return newtup
tup=gensquaretype(tup)
print(tup)
