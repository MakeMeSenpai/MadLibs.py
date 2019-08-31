from termcolor import colored
import os
import time

def MadLibs():
    name = input("Hi! What is your name? ")
    place1 = input("Name some place(house): ")
    place2 = input("Name another place(village): ")
    items1 = input("Name a plural item(grapes): ")
    items2 = input("Name a another plural item(keys): ")
    date = input("Name a set of time(month): ")
    descriptor = input("Name an adjustive(or descriptor): ")
    action = input("Name an action(moving): ")
    feeling = input("Name a feeling(past tense): ")
    time.sleep(1)
    os.system("clear")
    print("*** Loading Results!!! ***")
    time.sleep(2)
    print("###########", end="")
    time.sleep(1)
    print("####", end="")
    time.sleep(2)
    print("######")
    print("Story Time; ")
    print(f"""
        {name} went to the {place1} to buy lots and lots of {items1}. 
        However when {name} got the {items1}, they lost their {items2} over 
        the ridiculous price, and how they would now have to go {date} 
        with a bunch of {descriptor} {items1}. {name} {action}
        {place2} and {feeling}. The End.""")
MadLibs()

#Thanks Kevin for Helping me with same line print statements!

#To-Do list
#use a list, tupel, or dictionary

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