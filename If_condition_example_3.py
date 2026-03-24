# Grading system simulation
Grade = float(input("Enter your grades: "))
if Grade > 80:
    print("You are in grade A")
elif Grade >= 70:
    print("You are in grade B")
elif Grade >= 60:
    print("You are in grade C")
elif Grade >= 50:
    print("You are in grade D")
else:
    print("You failed")