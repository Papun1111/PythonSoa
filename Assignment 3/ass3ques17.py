def removeVowel(s):
    s=s.lower()
    str=""
    for i in s:
        if i=="a" or i=="e" or i=="i" or i=="o" or i=="u":
            pass
        else:
            str+=i
    return str
s=input("enter a string")
newstr=removeVowel(s)
print(f"new str without vowel is {newstr}")
