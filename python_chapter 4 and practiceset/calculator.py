import time
import os

def countdown(minutes)
    second=minutes*60

    while second>0:
        mins,secs=divmod(second,60)
        timer_display=f"{mins:02d}:{secs:02d}"
        print(f"Time remaining:{timer_display}",end="\r")

        time.sleep(1)
        seconds-=1

        print("\nTime up!Take a brealk!")

        if_name_=="_main_":
        print("---python task timer---")
        user_input=input("enter focus time in minutes:")

        try:
            minutes=int(user_input)
            print(f"starting a{minutes}minute sessions...")
            countdown(minutes)
        except valueError:
            print("please enter a valid number.")