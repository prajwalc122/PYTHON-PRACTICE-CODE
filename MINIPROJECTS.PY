you = input("Enter your choice: ")

youDict = {
    "sanjay": 1,
    "prajwal": 2,
    "ninja": 4
}

if you in youDict:
    print("The choice is:", you)
    print("Value is:", youDict[you])
else:
    print("Invalid choice")
