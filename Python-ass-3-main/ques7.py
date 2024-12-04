char=input("enter a character")

def isVowel(char):
    vowel="AEIOUaeiou"
    if char in vowel:
        return True
    else:
        return False
    
if(isVowel(char)):
    print("It is vowel")
else:
    print("consonant")        