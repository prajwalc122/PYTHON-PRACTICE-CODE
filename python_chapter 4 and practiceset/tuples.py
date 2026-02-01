'''
🔹 What is a Tuple?

👉 A tuple is a collection used to store multiple values in a single variable
👉 Tuples are written using round brackets ( )
👉 Tuples are ordered and immutable (cannot be changed)

🔹 Creating a Tuple
t = (10, 20, 30)
print(t)

Single-element tuple (important ❗)
t = (10,)   # comma is mandatory

🔹 Accessing Tuple Elements (Indexing)
t = ("apple", "banana", "mango")
print(t[0])   # apple
print(t[2])   # mango

🔹 Tuple is Immutable (Cannot Change)
t = (1, 2, 3)
t[0] = 10


❌ Error:

TypeError: 'tuple' object does not support item assignment
'''

a=(1,2,3,4,5,6,7,8,9,10)
print(type(a))                           #the output will be tuple cl
print(a)

b=(2,4,53,3,23,4,3,2)
print(type(b))