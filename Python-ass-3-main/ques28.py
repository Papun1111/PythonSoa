def ShiftOne(s):
    strs=""
    for i in s:
        if i=="z":
            strs+="a"
        else:    
            char=chr(ord(i)+1)
            strs+=char
    return strs
print(ShiftOne("python"))

# qzuipo