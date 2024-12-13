number=int(input("enter a number"))

def fibonacci(number):
    if(number==0 or number ==1):
        return 1

    return fibonacci(number-1)+fibonacci(number-2)


print(fibonacci(number))


           
       
        
        
