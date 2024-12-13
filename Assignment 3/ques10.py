s=input("enter a string")

def permutations(s):
    for i in range(len(s)+1):
        for j in range(i+1,len(s)+1):
            print(s[i:j])

permutations(s)            