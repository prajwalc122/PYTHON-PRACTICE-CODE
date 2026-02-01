#write a program to accept 6 student marks display him into sorted mannar



marks=[]

f1= int(input("enter marks here  1:"))
marks.append(f1)

f2= int(input("enter marks here  2:"))
marks.append(f2)


f3= int(input("enter marks here  3:"))
marks.append(f3)


f4= int(input("enter marks here  4:"))
marks.append(f4)


f5= int(input("enter marks here  5:"))
marks.append(f5)


f6= int(input("enter marks here  6:"))
marks.append(f6)



f7= int(input("enter marks here  7:"))
marks.append(f7)

print("my first marks here is : ",f1)
print("my second marks here is :",f2)
print("my third marks here is :",f3)
print("my fourth marks here is :",f4)
print("my five marks here is :",f5)
print("my six marks here is :",f6)
print("my seven marks here is :",f7)

marks.sort()
print(marks)