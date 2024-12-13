def replaceVow(s):
    str=""
    for i in s:
        if i=='a'or i=="e" or i=="i" or i=="o" or i=="u":
            str+="*"
        else:
            str+=i
    return str

s=input("Enter a String")
print(replaceVow(s.lower()))        
# Enter a String Papun
#  p*p*n