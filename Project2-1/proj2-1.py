'''
Class: CPSC 475
Team Member 1: Stella Beemer
Team Member 2: None
Submitted by: Stella Beemer
GU Username: sbeemer2
File name: proj2-1.py
Program adapts the Eliza function to ask more questions using regex and re functions
To Execute: python3 proj2-1.py
'''

import sys
import re

'''
pre:  userIn is a string of user input from main function
post: returns a string that matches responds to what the user entered.
'''
def chooseReply(userIn):
    if re.search(r"^hello|hi$", userIn):
        return "Hello! Are you ready for the best question?"
    elif re.search(r"(grilled|cheese|ham$)", userIn):
        return "Ah, a human of taste."
    elif re.search(r"(fairy|vegemite)", userIn):
        return "Begonne, Australian."
    elif re.search(r"(samwich|sandwich|pb&j)", userIn):
        return "I mean, you're not wrong, but dig a little deeper!"
    elif re.search(r"(dog|lasagna)", userIn):
        return "No. Bad."
    elif re.search(r"(dumpling|empanada|samosa|gyoza)", userIn):
        return "Just because something has a bread-like outside \nand filling doesn't mean it's a sandwich. Next."
    elif re.search(r"burger", userIn):
        return "I can't argue with that one."
    elif re.search(r"^what|why", userIn):
        return "Because I (the omnipotent computer) said so :)"
    return "What is something you consider a sandwich?"

'''
pre:  main function, called at bottom of program when program starts
post: calls chooseReply to respond to user
'''
def main():
    print("Welcome! How may I help you? (type \"bye\" to quit).\n")
    while True:
        userInput = input("User: ")
        userInput = userInput.lower()
        if re.search(r'\bbye\b', userInput):
            print("Nice chatting with you!\n")
            return 0
        print(chooseReply(userInput))
        print()
        
if __name__ == "__main__":
    sys.exit(main())
