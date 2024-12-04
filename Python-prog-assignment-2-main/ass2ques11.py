while True :
    a=int(input("Enter a number"))
    b=int(input("Enter a number"))
    c=input("enter your choice")
    if(c=="+"):
        print(f"The sum of {a} and {b} is {a+b}")
    if(c=="-"):
        print(f"The diff of {a} and {b} is {a-b}")
    if(c=="*"):
        print(f"The prod of {a} and {b} is {a*b}")
    if(c=="/"):
        print(f"The quotient of {a} and {b} is {a//b}")
    if(c=="exit"):
        break                                