day = input()

if day == "Monday":
    print("Working day")
elif day == "Tuesday":
    print("Working day")
elif day == "Wednesday":
    print("Working day")
elif day == "Thursday":
    print("Working day")
elif day == "Friday":
    print("Working day")
elif day == "Saturday":
    print("Weekend")
elif day == "Sunday":
    print("Weekend")
else:
    print("Error")
################################## vtori nachin za pisane na zadachata
if day in "Monday Tuesday Wednesday Thursday Friday":
    print("Working day")
elif day in "Saturday Sunday":
    print("Weekend")
else:
    print("Error")
