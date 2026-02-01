#chapter 4 lists and truples 
frends=["apple",18,10.4,False]
frends[0]="prajwal"
print(frends[0],frends[1],frends[2],frends[3])
print(len(frends))
print(frends[0:2])
print(frends[0:3])
print(frends[2:3])
print(frends[-4:-1])
print(frends[0:-1])
print("im replace you and i will slicing",frends[0:3])



'''
Let me explain Mutable and Immutable in Python in a very simple & exam-friendly way.

🔹 What is Mutable?

👉 Mutable means “can be changed” after creation

✔ You can modify the value without creating a new object
Examples of Mutable objects:

list

dict

set

Example:
a = [1, 2, 3]
a[0] = 10
print(a)


Output:

[10, 2, 3]


✅ List changed → so list is mutable

🔹 What is Immutable?

👉 Immutable means “cannot be changed” after creation

✔ If you try to change, Python creates a new object
Examples of Immutable objects:

int

float

string

tuple

Example:
s = "Python"
s[0] = "J"


❌ Error:

TypeError: 'str' object does not support item assignment


✅ String cannot be changed → string is immutable

🔹 Another Example (Tuple)
t = (1, 2, 3)
t[1] = 5


❌ Error → tuple is immutable

🔹 Memory Concept (Simple)
x = 10
x = 20


👉 Old value not changed
👉 New value created

🔹 Comparison Table (Important for Exam)
Feature	Mutable	Immutable
Can change value	Yes	No
Memory	Same object	New object created
Examples	list, dict, set	int, string, tuple'''
