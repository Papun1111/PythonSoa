def CorresNumber(n):
    s = str(n)
    strs = ""
    for i in s:
        if i == "1":
            strs += "One "
        elif i == "2":
            strs += "Two "
        elif i == "3":
            strs += "Three "
        elif i == "4":
            strs += "Four "
        elif i == "5":
            strs += "Five "
        elif i == "6":
            strs += "Six "
        elif i == "7":
            strs += "Seven "
        elif i == "8":
            strs += "Eight "
        elif i == "9":
            strs += "Nine "
        elif i == "0":
            strs += "Zero "
    return strs.strip()


print(CorresNumber(81))
