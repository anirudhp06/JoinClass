import webbrowser

import sys as system

from os import system as sys

from time import sleep

import platform

import datetime  # Importing all necessary Modules required for program

x = datetime.datetime.now()
clear = ""

if platform.version == "Linux":
    clear = "clear"

else:
    clear = "cls"
subject_name = [
    "Java",
    "Java-Lab",
    "OS",
    "Unix",
    "DBMS",
    "DBMS-LAB",
    "English",
    "Kannada",
    "CN",
]  # Setting up Subjects to be displayed

links = [
    "https://trimurl.co/3CGlxF",
    "https://trimurl.co/L0JHyM",
    "https://trimurl.co/cm7wEP",
    "https://trimurl.co/DYBRhW",
    "https://trimurl.co/tuOTd1",
    "https://trimurl.co/SRbwm1",
    "https://trimurl.co/5HG6X7",
    "https://trimurl.co/40KwHl",
    "https://trimurl.co/oduL2S",
]  # Links are used to join the classes of corresponding classes


while True:  # Infite loop so program can run until user wants to...

    sys(clear)  # Clears command line of windows, if you want to clear command line of linux use 'clear' instead of 'cls'

    print("Which Class do you want to join?")

    sno = 1

    for i in subject_name:

        print(
            "{}.{}".format(sno, i)
        )  # Printing Subjects that are present in variable 'a'

        sno += 1

    print("10.Exit")  # Displayed at last

    select = int(input("Enter Your choice:"))

    if select == 1:

        print("Do you want to schedule When to join?(Y/N)(y/n):")
        sec = input()

        if sec == "y" or sec == "Y":  # If statements to determine correct decisions:

            print("After how much mins u want to join class? (in Mins):")
            rem = int(input())

            x = datetime.datetime.now()

            print(x.strftime("%I:%M %p"), end=" ")

            print("Joining Java Class in {} mins".format(rem))

            sleep(rem * 60)  # Sleep Function takes only seconds as inputs so multiplied 'rem' with 60

            sys("cls")

            webbrowser.open(links[select - 1])  # Function which will accurately opens class in web browser

        else:

            x = datetime.datetime.now()

            print(x.strftime("%I:%M %p"), end=" ")

            print("Joining Java Class")

            webbrowser.open(links[select - 1])

            sleep(1)

            sys("cls")

    elif select == 2:

        print("Do you want to schedule when to join?(Y/N)(y/n):")
        sec = input()

        if sec == "y" or sec == "Y":

            print("After how much mins u want to join class? (in Mins):")
            rem = int(input())

            x = datetime.datetime.now()

            print(x.strftime("%I:%M %p"), end=" ")

            print("Joining Java Lab in {} mins".format(rem))

            sleep(rem * 60)

            sleep(1)

            sys("cls")

            webbrowser.open(links[select - 1])

        else:

            x = datetime.datetime.now()

            print(x.strftime("%I:%M %p"), end=" ")

            print("Joining Java-Lab")

            webbrowser.open(links[select - 1])

            sleep(1)

            sys("cls")

    elif select == 3:

        print("Do you want to schedule when to join?(Y/N)(y/n):")
        sec = input()

        if sec == "y" or sec == "Y":

            print("After how much mins u want to join class? (in Mins):")
            rem = int(input())

            x = datetime.datetime.now()

            print(x.strftime("%I:%M %p"), end=" ")

            print("Joining OS in {} mins".format(rem))

            sleep(rem * 60)

            sleep(1)

            sys("cls")

            webbrowser.open(links[select - 1])

        else:

            x = datetime.datetime.now()

            print(x.strftime("%I:%M %p"), end=" ")

            print("Joining OS")

            webbrowser.open(links[select - 1])

            sleep(1)

            sys("cls")

    elif select == 4:

        print("Do you want to schedule when to join?(Y/N)(y/n):")
        sec = input()

        if sec == "y" or sec == "Y":

            print("After how much mins u want to join class? (in Mins):")
            rem = int(input())

            x = datetime.datetime.now()

            print(x.strftime("%I:%M %p"), end=" ")

            print("Joining UNIX  in {} mins".format(rem))

            sleep(rem * 60)

            sleep(1)

            sys("cls")

            webbrowser.open(links[select - 1])

        else:

            x = datetime.datetime.now()

            print(x.strftime("%I:%M %p"), end=" ")

            print("Joining UNIX")

            webbrowser.open(links[select - 1])

    elif select == 5:

        print("Do you want to schedule when to join?(Y/N)(y/n):")
        sec = input()

        if sec == "y" or sec == "Y":

            print("After how much mins u want to join class? (in Mins):")
            rem = int(input())

            x = datetime.datetime.now()

            print(x.strftime("%I:%M %p"), end=" ")

            print("Joining DBMS in {} mins".format(rem))

            sleep(rem * 60)

            sleep(1)

            sys("cls")

            webbrowser.open(links[select - 1])

        else:

            x = datetime.datetime.now()

            print(x.strftime("%I:%M %p"), end=" ")

            print("Joining DBMS")

            webbrowser.open(links[select - 1])

            sleep(1)

            sys("cls")

    elif select == 6:

        print("Do you want to schedule when to join?(Y/N)(y/n):")
        sec = input()

        if sec == "y" or sec == "Y":

            print("After how much mins u want to join class? (in Mins):")
            rem = int(input())

            x = datetime.datetime.now()

            print(x.strftime("%I:%M %p"), end=" ")

            print("Joining DBMS Lab in {} mins".format(rem))

            sleep(rem * 60)

            sleep(1)

            sys("cls")

            webbrowser.open(links[select - 1])

        else:

            x = datetime.datetime.now()

            print(x.strftime("%I:%M %p"), end=" ")

            print("Joining DBMS-Lab")

            sleep(1)

            sys("cls")

            webbrowser.open(links[select - 1])

    elif select == 7:

        print("Do you want to schedule when to join?(Y/N)(y/n):")
        sec = input()

        if sec == "y" or sec == "Y":

            print("After how much mins u want to join class? (in Mins):")
            rem = int(input())

            x = datetime.datetime.now()

            print(x.strftime("%I:%M %p"), end=" ")

            print("Joining English in {} mins".format(rem))

            sleep(rem * 60)

            sleep(1)

            sys("cls")

            webbrowser.open(links[select - 1])

        else:

            x = datetime.datetime.now()

            print(x.strftime("%I:%M %p"), end=" ")

            print("Joining English Class")

            webbrowser.open(links[select - 1])

            sleep(1)

            sys("cls")

    elif select == 8:

        print("Do you want to schedule when to join?(Y/N)(y/n):")
        sec = input()

        if sec == "y" or sec == "Y":

            print("After how much mins u want to join class? (in Mins):")
            rem = int(input())

            x = datetime.datetime.now()

            print(x.strftime("%I:%M %p"), end=" ")

            print("Joining Kannada Class in {} mins".format(rem))

            sleep(rem * 60)

            sleep(1)

            sys("cls")

            webbrowser.open(links[select - 1])

        else:

            x = datetime.datetime.now()

            print(x.strftime("%I:%M %p"), end=" ")

            print("Joining Kannada Class")

            sleep(1)

            sys("cls")

            webbrowser.open(links[select - 1])

    elif select == 9:

        print("Do you want to schedule when to join?(Y/N)(y/n):")
        sec = input()

        if sec == "y" or sec == "Y":

            print("After how much mins u want to join class? (in Mins):")
            rem = int(input())

            x = datetime.datetime.now()

            print(x.strftime("%I:%M %p"), end=" ")

            print("Joining Computer Networking Class in {} mins".format(rem))

            sleep(rem * 60)

            sleep(1)

            sys("cls")

            webbrowser.open(links[select - 1])

        else:

            x = datetime.datetime.now()

            print(x.strftime("%I:%M %p"), end=" ")

            print("Joining Computer Networking Class")

            sleep(1)

            sys("cls")

            webbrowser.open(links[select - 1])

    elif select == 10:

        print("Execution of program Stopped\n Closing Program in 3 Seconds")

        sleep(2)

        system.exit()  # Exits program After 3 seconds of selecting option to exit.

    else:

        x = datetime.datetime.now()

        print(x.strftime("%I:%M %p"), end=" ")

        print("Try Again with Option")

        sys("cls")  # Clears the user screen if user enters wrong option.
