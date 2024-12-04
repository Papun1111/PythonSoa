marks=int(input("Enter your grade"))
if marks>=90 and marks<=100:
    grade="A"
    print("Excellent")
elif marks>=80:
    grade="B"
    print("Good")
elif marks>=70:
    grade="C"
    print("Average")
elif marks>=60:
    grade="D"
    print("Needs Improvement")
else:
    grade="F"
    print("Failing")
