'''
1 FOR SNAKE ,
-1 FOR WATER ,
0 FOR GUN.
'''
computer=-1
user=int(input("Enter your choices :"))
youdict={ "s":1,"w":-1,"g":0}
mynum=youdict

if(computer==-1):
    print("You choose water in this Game, ")
    print("You will Win")
elif(computer==1):
    print("You choose Snake in this game,")
    print("You Will Win the Game!")
elif(computer==0):
    print("You choose the Gun in this Game,")
    print("You will Win!")
else:
    print("you loose the game Better Luck Next Time,")
    print("Thank You Try Better Next Time ")

