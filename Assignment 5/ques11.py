diction = {
    1: "One",
    2: "Two",
    3: "Three",
    4: "Four",
    5: "Five",
    6: "Six",
    7: "Seven",
    8: "Eight",
    9: "Nine"}
n=input("Enter a number: ")
for i in n:
    print(diction.get(int(i)),end=" ")
