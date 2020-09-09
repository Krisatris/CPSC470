'''
Class: CPSC 475
Team Member 1: Stella Beemer
Submitted by: Stella Beemer
GU Username: sbeemer2
File Name: proj1-1.py
System prompts for multiple strings, and parses them for a common substring
To Execute: python3 proj1-1.py
'''
import sys

'''
    pre:  called in main when user is asked for file name
    post: passes the found file to main (if it is found)
'''
def open_file():
    while(True):
        fileIn = input('Enter an input file name: ')
        try:
            fileIn = open(fileIn, 'r')
            break
        except:
            print("file does not exist, please try again.")
    return fileIn

'''
    pre:  fileIn is the file the user specifies
    post: file is parsed for the substring entered by the user
          displays how many times the substring is found
'''
def parseFile(fileIn):
    substring = input('Enter a substring: ')
    fileString = fileIn.read()
    fileLen = len(fileString)
    foundSub = 0;
    for i in range(fileLen):
        if (fileString[i] == substring[0]):
            foundSub += checkSub(fileString, substring, i)
    print('Substring found', foundSub, 'time(s)')

'''
    pre:  file is a string of the contents of the user file, sub is the substring
          specified by user, posF is the parsing position of the file string
    post: parses the substring and file to ensure the match is there, returns 1
          if it is and 0 if it isn't.
'''
def checkSub(file, sub, posF):
    posF += 1
    posS = 1
    fileLen = len(file)
    subLen = len(sub)
    while(posF < fileLen and posS < subLen):
        if(file[posF] != sub[posS]):
            return 0
        posF += 1
        posS += 1
    if(posF >= fileLen): 
        return 0
    else:
        return 1

'''
    pre:  main function, called below
    post: begins process of finding substrings
'''
def main():
    fileIn = open_file()
    parseFile(fileIn)

main()
