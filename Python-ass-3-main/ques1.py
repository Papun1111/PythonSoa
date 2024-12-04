def find_greatest_digits(number):
    first = second = third = -1  

    while number > 0:
        digit = number % 10  
       
        if digit > first:
            third = second
            second = first
            first = digit
        elif digit > second and digit != first:
            third = second
            second = digit
        elif digit > third and digit != second:
            third = digit
            
        number //= 10  

    return [first, second, third]

# Sample usage
number = 1234
result = find_greatest_digits(number)
print(result)
