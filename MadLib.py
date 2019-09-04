from termcolor import colored
import os
import time

def MadLibs():
    print("Please do not type unless prompted")
    name = input("Hi! What is your name? ")
    place = list()
    place.append(input("Name a place(store): "))
    place.append(input("Name some other places(home): "))
    item = list()
    item.append(input("Name a plural item(grapes): ")) 
    item.append(input("Name a another plural item(mind): "))
    date = input("Name a set of time(months): ")
    descriptor = input("Name an adjustive(soggy): ")
    action = input("Name an action(ran): ")
    feeling = input("Name a feeling(cried): ")
    time.sleep(1)
    os.system("clear")
    print("*** Loading Results!!! ***")
    time.sleep(2)
    print("###############", end="")
    time.sleep(1)
    print("########", end="")
    time.sleep(2)
    print("##########")
    print("Story Time; ")
    print(f"""
        {name} went to the {place[0]} to buy lots and lots of {item[0]}. 
        However when {name} got the {item[0]}, they lost their {item[1]} over 
        the ridiculous price, and how they would now have to go {date} 
        with a bunch of {descriptor} {item[0]}. {name} {action}
        {place[1]} and {feeling}. The End.""")
MadLibs()

#Thanks Kevin for Helping me with same line print statements!

#Stretch
#Handles improper user input
#Story uses formatting and colors to provide a richer experience
#Randomize words of the same type
#use a list of words from a directory to generate words randomly if
###user requests it
#Use a different data structure to store words
#Build with test driven development (TDD)
#Use the system module (for accessing command-line arguments)
#Add ASCII art/design to your story
#Take MadLibs out of the terminal & have it running as a website
##~Bonus: make it live with Heroku (or your place of choice)