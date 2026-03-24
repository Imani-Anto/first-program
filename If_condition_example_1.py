# Online exam qualification
registered = input("Are you registered: yes/no")
tuition_fee = input("Are the tuition fee paid:")

if tuition_fee == "yes" and registered == "yes":
    print("Cleared for the exam")
elif tuition_fee == "no" and registered == "yes":
     print("Not allowed for exam")
else:
    print("You are nor allowed to come to school")