'''
null_dic={
    
    "name":"prajwal c",
    "place": "shivamogga"
}


print(input("enter the set"),null_dic)
'''


import random
import string

print("===== PASSWORD GENERATOR=====")

length= int(input("Enter passwoard lenght : "))

letter= string.ascii_letters
digits=string.digits
symbols=string.punctuation

all_chars= letter+ digits + symbols

passwoard=""


for i in range(length):
    passwoard+=random.choice(all_chars)
    
    print("\n Generated Passwoard:",passwoard)
