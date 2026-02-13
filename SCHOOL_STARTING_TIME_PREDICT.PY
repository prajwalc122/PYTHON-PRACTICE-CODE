
# time = float(input("Enter time (in hours, e.g. 8.30, 9.00): "))

# if time < 9.00:
#     print("School has not started")
# elif time == 9.00:
#     print("School starts now")
# else:
#     print("You are late to school")




school=input("Enter your School Name:")
SESSION=input("Enter your Session To Attend The Class:")

if SESSION=="morning":
    print("The school Name is:"+school+"AND This is an Morning Class you should attend the class before 9:00 AM")
elif SESSION=="evening":
    print("The school Name is:"+school+" AND This is an Evening Class  you should attend the class before 12:30 PM")
else:
    print("The school Name is:"+school+" AND This is Night Session and you Should attend the class Before 7:00pm")
