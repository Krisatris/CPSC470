'''
Class: CPSC475
Team Member 1: Stella Beemer
Submitted by: Stella Beemer
GU Username: sbeemer2
File name: proj2-4.py
Project computes and displays the minimum edit distance for converting a string
To Execute: python3 proj2-4.py source target
**important note, this program has the makings of the displaying alignment part
  of this assignment but I did not have the mental capacity to finish it before
  the due date. the functions are still here though so you can see where I was
  going with them
'''
import sys

'''
pre:  points is the array/list of arrows at each point in the matrix, source
      is the original string, target is the string to be changed to
post: prints the alignment of the source and target strings
def printTable(points, source, target):
    int i = len(source)
    int j = len(target)
    while (i != 0 and j != 0):
'''

'''
pre:  point is the list of pointers, i is the current horiz dist, j is the
      current vertical dist, dist is the array of distances, source is the
      original string, and target is the string to be changed to
post: returns the pointer array with the list updated for the current index

def setP(point, i, j, dist, source, target):
    temp = []
    temp.append(dist[i][j])

    # side/insert arrow
    if dist[i-1][j] == dist[i][j] - 1:
        temp.append(1)
    else:
        temp.append(0)

    # diagonal/swap arrow
    if dist[i-1][j-1] == dist[i][j] - 2:
        temp.append(1)
    elif dist[i-1][j-1] == dist[i][j]:
        if source[i-1] == target[j-1]:
            temp.append(1)
        else:
            temp.append(0)
    else:
        temp.append(0)

    # up/delete arrow
    if dist[i][j-1] == dist[i][j] - 1:
        temp.append(1)
    else:
        temp.append(0)

    point[i][j] = temp

    return pointer
''' 

'''
pre:  table is the dynamic table from the below function source is the beginning
      string, target is the string to be changed to, i is the current horizontal
      position and j is the current vertical position
post: returns the minVal at the current pos
'''
def getMin(table, i, j, source, target):
    deletionCost = table[i-1][j] + 1
    insertionCost = table[i][j-1] + 1
    if(source[i-1] == target[j-1]):
        subCost = table[i-1][j-1]
    else:
        subCost = table[i-1][j-1] + 2
    minVal = min(deletionCost, insertionCost, subCost)
    return minVal

'''
pre:  source is the beginning string, target is the string to be changed to, len1 is the length of source,
      len2 is the length of target
post: returns the min edit distance of the two strings
'''
def minEditDynamic(source, target, len1, len2):
    table = [[0 for a in range(len2 + 1)] for a in range(len1 + 1)]
    pTable = [[[0, 0, 0, 0] for a in range(len2 + 1)] for b in range(len1 + 1)]

    table[0][0] = 0
    for i in range(1, len1 + 1):
        table[i][0] = table[i-1][0] + 1
        pTable[i][0] = [table[i][0], 1, 0, 0]
    for j in range(1, len2 + 1):
        table[0][j] = table[0][j - 1] + 1
        pTable[0][j] = [table[0][j], 0, 0, 1]

    for i in range(1, len1 + 1):
        for j in range(1, len2 + 1):
            table[i][j] = getMin(table, i, j, source, target)
            #pTable = setP(table, i, j, pTable, source, target)

    #printPoint(pTable)

    return table[len1][len2]     

'''
pre:  str1 is the source string, str2 is the target string, i is the length of
      source and j is the length of target. these values will change as the function
      is called recursively
post: returns the min edit distance needed to edit a string
note: I created this function and then realized that it was not going to be useful
      when computing alignment but I'm keeping it in the program because I don't
      want to delete it (:
'''
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

    minDistance = minEditDynamic(source, target, len(source), len(target))
    print("The minimum edit distance for the strings entered is: " + str(minDistance))

main()
