try:
    a = int(input("Enter a number: "))
    num = a % 5
    match num:
        case 0:
            print("The remainder is 0")
        case 1:
            print("The remainder is 1")
        case 2:
            print("The remainder is 2")
        case 3:
            print("The remainder is 3")
        case 4:
            print("The remainder is 4")
except ValueError:
    print("Invalid Number")
