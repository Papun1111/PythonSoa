number = int(input("Enter an integer: "))
a=number
ans=""
while a>0:
    d=a%10
    if d == 0:
        ans="Zero "+ans
    if d == 1:
        ans="ONE "+ans
    if d == 2:
        ans="TWO "+ans
    if d == 3:
        ans="THREE "+ans
    if d == 4:
        ans="FOUR "+ans
    if d == 5:
        ans="FIVE "+ans        
    if d == 6:
        ans="SIX "+ans
    if d == 7:
        ans="SEVEN "+ans
    if d == 8:
        ans="EIGHT "+ans 
    if d==9:
        ans="NINE "+ans
    a=a//10

print(ans)