number = input("Enter a Roman numeral: ")

def changeIntoNumber(n):
    s = 0
    prev_value = 0
    
    for char in reversed(n):
        if char == 'I':
            value = 1
        elif char == 'V':
            value = 5
        elif char == 'X':
            value = 10
        elif char == 'L':
            value = 50
        elif char == 'C':
            value = 100
        elif char == 'D':
            value = 500
        elif char == 'M':
            value = 1000
        else:
            value = 0
        
        if value < prev_value:
            s -= value
        else:
            s += value
        prev_value = value

    return s

num = changeIntoNumber(number)
print(f"The number {number} is {num}")
