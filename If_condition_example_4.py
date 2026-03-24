# Salary increment based on experince
Salary = int(input("Your actual salary:"))
Experience = int(input("Enter your years of experience:"))

if Experience >= 10:
    New_salary = Salary * 1.5
    print(f"Your new salary is: {New_salary} Rwf")
    
elif Experience >= 5:
    New_salary = Salary * 1.2
    print(f"Your new salary is: {New_salary} Rwf")
    
else:
    print(f"Your salary {Salary} Rwf")