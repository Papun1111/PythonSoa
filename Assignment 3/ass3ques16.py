def calculator():
    print("1.ADD\n2.SUBSTRACT\n3.MULTIPLY\n4.Division")
    s=input("enter a choice 1/2/3/4 ")
    a=int(input("enter first number"))
    b=int(input("enter second number"))
    if(s=="1"):
        print(f"sum is {a+b}")
    elif(s=="2"):
        print(f"the difference is {a-b}")
    elif(s=="3"):
        print(f"the product is {a*b}")
    elif(s=="4"):
        print(f"the quotient is {a/b}")
        print(f"the remainder is {a%b}")
    else:
        pass


calculator()    
        
