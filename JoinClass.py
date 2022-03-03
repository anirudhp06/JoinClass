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
subject_name=[each_string.lower() for each_string in subject_name]
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
        )  # Printing Subjects that are present in variable 'subject_name'

        sno += 1

    print("10.Exit")  # Displayed at last
    ind=0
    sub_sel = input("Enter Subject name(as is):")
    if sub_sel in subject_name:
        ind=subject_name.index(sub_sel)
        print("Do you want to schedule When to join?(Y/N)(y/n):")
        sec = input()

        if sec == "y" or sec == "Y":  # If statements to determine correct decisions:

            print("After how much mins u want to join class? (in Mins):")
            rem = int(input())

            x = datetime.datetime.now()

            print(x.strftime("%I:%M %p"), end=" ")

            print("Joining {} Class in {} mins".format(sub_sel,rem))

            sleep(rem * 60)  # Sleep Function takes only seconds as inputs so multiplied 'rem' with 60

            sys(clear)

            webbrowser.open(links[ind])  # Function which will accurately opens class in web browser

        else:

            x = datetime.datetime.now()

            print(x.strftime("%I:%M %p"), end=" ")

            print("Joining {} Class".format(sub_sel))

            webbrowser.open(links[ind])

            sleep(1)

            sys(clear)
    elif sub_sel == "exit" or "EXIT":

        print("Execution of program Stopped\n Closing Program in 3 Seconds")

        sleep(2)

        system.exit()  # Exits program After 3 seconds of selecting option to exit."""

    else:

        x = datetime.datetime.now()

        print(x.strftime("%I:%M %p"), end=" ")

        print("Try Again with Option")

        sys(clear)  # Clears the user screen if user enters wrong option.