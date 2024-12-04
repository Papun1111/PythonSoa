def reverse(s):
    str=""
    i=len(s)-1
    while i>=0:
        str=str+s[i]
        i=i-1
    return str

s="papun"
str=reverse(s)
print(str)
