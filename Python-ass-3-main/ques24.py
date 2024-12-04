def removePunctuation(text):
    result = ""
    for char in text:
        if char.isalnum() or char.isspace(): 
            result += char
    return result

text = "cIGARRETES aFTER sEX !, HUHUH"
result = removePunctuation(text)
print(result)  # Output:cIGARRETES aFTER sEX  HUHUH