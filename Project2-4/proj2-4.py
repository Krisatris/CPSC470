'''
Class: CPSC475
Team Member 1: Stella Beemer
Submitted by: Stella Beemer
GU Username: sbeemer2
File name: proj2-4.py
Project computes and displays the minimum edit distance for converting a string
To Execute: python3 proj2-4.py source target
'''
import sys

def minEditDistance(str1, str2, i, j):
    if i == 0:
        return j

    if j == 0:
        return i

    if str1[i - 1] == str2[j - 1]:
        return minEditDistance(str1, str2, i - 1, j - 1)

    return 1 + min(minEditDistance(str1, str2, i, j - 1),
                   minEditDistance(str1, str2, i - 1, j),
                   minEditDistance(str1, str2, i - 1, j - 1))

def main():

    source = sys.argv[1]
    target = sys.argv[2]

    minDistance = minEditDistance(source, target, len(source), len(target))
    print(minDistance)

main()
