def printProgression(firstTerm,commonDif):
    for i in range(10):
        term = firstTerm + i * commonDif
        print(term)

firstTerm=int(input("Enter the first Term"))

commonDif=int(input("Enter the common difference T"))
printProgression(firstTerm,commonDif)

# Enter the first Term1
# Enter the common difference T1
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# 10