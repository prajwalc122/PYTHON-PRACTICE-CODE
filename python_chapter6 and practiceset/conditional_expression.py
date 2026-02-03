'''
conditional_expression:-
in python concise way to write if else statements is called as conditional expressions.\
    * if 
    * elif
    * else
    
    
    value if true => IF
    value if false => else


'''

a=int(input("enter your age:"))

if (a>=18):
    print("he was an above the 18")
    print("Its an good")

    
elif(a>0):
    print("0 is not valid for yours age")
    
elif(a<100):
    print("negaTIve sign does not contain any AGE")
    
else:
    print("he was an below 18 age  ")
    print("it was not an bad")