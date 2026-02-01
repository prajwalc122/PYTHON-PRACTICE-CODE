#sorting by using the listfunction
a=[1,3,5,6,2,7,9,8]
a.sort()
print(a)


#reverse by using the list functions
a=["custom","board","big",55,43]
a.reverse()
print(a)


#using append function inlists

h=["prajwal",11,88,"jio",False,21]
h.append("hi")
h.append(2)
print(h)


#ussing insert function in lists
B=["boy","ball","bat",4]
B.insert(4,333)
print(B)

#using pop methods for deleting
lot=["my first lot","praj",2,22,34,90]
lot.pop(5)
print(lot)

#another example

name=["prajwal","ninja","sorting"]
value=name.pop(2)
print(name)
print(value)



a = [10, 20, 30]
a.insert(1, 15)
print(a)



a=["prajwal","harry","phone","passangers","advocate","learning","earning"]
a.insert(1, "pop")
print(a)


'''

🔹 What is a List in Python?

👉 A list is a collection of multiple values stored in a single variable
👉 Lists are written using square brackets [ ]
👉 Lists are ordered, mutable (changeable), and allow duplicates

Example:
numbers = [10, 20, 30, 40]

🔹 Features of List

✔ Can store different data types
✔ Values can be changed
✔ Index starts from 0
✔ Allows duplicate values

data = [1, "Python", 3.5, True]

🔹 Accessing List Elements (Indexing)
fruits = ["apple", "banana", "mango"]
print(fruits[0])   # apple
print(fruits[2])   # mango

🔹 Changing List Elements
fruits[1] = "orange"
print(fruits)


Output:

['apple', 'orange', 'mango']'''


'''
🔹 Most Used List Functions in Python
1️⃣ append()

👉 Adds one element at the end

a = [1, 2, 3]
a.append(4)
print(a)


Output: [1, 2, 3, 4]

2️⃣ extend()

👉 Adds multiple elements

a = [1, 2]
a.extend([3, 4, 5])
print(a)


Output: [1, 2, 3, 4, 5]

3️⃣ insert()

👉 Inserts element at specific position

a = [10, 20, 30]
a.insert(1, 15)
print(a)


Output: [10, 15, 20, 30]

4️⃣ remove()

👉 Removes specific element

a = [10, 20, 30]
a.remove(20)
print(a)

5️⃣ pop()

👉 Removes element using index (default = last)

a = [1, 2, 3]
a.pop()
print(a)

6️⃣ clear()

👉 Removes all elements

a = [1, 2, 3]
a.clear()
print(a)


Output: []

7️⃣ index()

👉 Finds position of element

a = [10, 20, 30]
print(a.index(20))


Output: 1

8️⃣ count()

👉 Counts how many times element appears

a = [1, 2, 2, 3]
print(a.count(2))


Output: 2

9️⃣ sort()

👉 Sorts list (ascending by default)

a = [4, 1, 3, 2]
a.sort()
print(a)

🔟 reverse()

👉 Reverses the list

a = [1, 2, 3]
a.reverse()
print(a)

1️⃣1️⃣ copy()

👉 Copies list

a = [1, 2, 3]
b = a.copy()
print(b)

1️⃣2️⃣ max() and min()

👉 Finds largest & smallest value

a = [5, 2, 9]
print(max(a))
print(min(a))

1️⃣3️⃣ sum()

👉 Finds total

a = [10, 20, 30]
print(sum(a))

1️⃣4️⃣ len()

👉 Finds length

a = [1, 2, 3]
print(len(a))

📝 One-Line Exam Answer

List functions are used to add, remove, modify, and manage elements in a list.

💡 Quick Memory Tip (Very Important)
Add	Remove	Check	Arrange
append	pop	index	sort
extend	remove	count	reverse
'''


