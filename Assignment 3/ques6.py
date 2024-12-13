a=input("Enter a word")
def reverse(s):
    str=""
    i=len(s)-1
    while i>=0:
        str=str+s[i]
        i=i-1
    return str
def isPalindrome(a):
    str=reverse(a)
    if(str==a):
        return True
    else:
        return False
    
print(isPalindrome(a))    
