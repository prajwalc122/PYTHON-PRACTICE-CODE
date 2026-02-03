a1=int(input("enter youre Test 1 marks: "))
a2=int(input("enter youre Test 2 marks: "))
a3=int(input("enter youre Test 3 marks: "))
a4=int(input("enter youre Test 4 marks: "))


total_marks=[a1+a2+a3+a4]
       
if(a1>a2 and a1>a3 and a1>a4):
    print("highest marks in A1",a1)
    
elif(a2>a1 and a2>a3 and a2>a4):
    print("highest marks in A2",a2)
    
elif(a3>a1 and a3>a2 and a3>a4):
    print("highest marks in A3",a3)
    
elif(a4>a1 and a4>a2 and a4>a3):
    print("highest marks in A4",a4)
    
    
print(total_marks)