marks=int(input("enter your marks:"))

if(marks>90 and marks<100):
    print("DISTINCTION")
elif(marks>80 and marks<90):
    print("FIRST CLASS ")
elif(marks>75 and marks<80):
    print("SECOND CLASS")
elif(marks>45 and marks<70):
    print("PASS")
elif(marks>30 and marks<45):
    print("FAIL")
else:
    print("HE WAS NOT APPEAR FOR THE EXAM ")