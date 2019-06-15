########################################################
##  Author      : Bryan Leong
##  Date        : 5 June 2019
##  Version     : 0.1
##  Description : Draft version of qa utility menu
########################################################

import os
import platform

def clear_screen():

    if platform.system()=='Windows':
        os.system("cls")
    if platform.system()=='Linux':
        os.system("clear")
    
def menu():

    while True:
        print("--------------------")
        print("QA Utility")
        print("--------------------")
        print("1. Installation")
        print("2. Smoke Test")
        print("3. Regression Test")
        print("4. Quit")
        print("5. Testing")
        choice = int(input("Enter your choice: "))
        clear_screen()
        
        if choice == 1:
            print("You choose to install new SAA")
        elif choice == 2:
            print("You choose to run smoke test")
        elif choice == 3:
            print("You choose to regression test")  
        elif choice == 4:
            print("Bye")
            break
            exit
        else:
            print("Invalid choice. Enter 1-3")

## Main routine
menu()
