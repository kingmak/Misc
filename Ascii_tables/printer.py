import os

#########################################################################
## TODO:
## add more structure to code
## add oop?
#########################################################################

corner = "+"
border = "|"
dash   = "-"
space  = " "

#########################################################################
## The below 3 functions deal with word alignment for cells.
#########################################################################

def left(word, maxLength):
    cellString = word + ((maxLength - len(word)) * space)
    return cellString

def right(word, maxLength):
    cellString = ((maxLength - len(word)) * space) + word
    return cellString

def center(word, maxLength):
    startIndex = (maxLength / 2) - (len(word) / 2)
    cellString = [0] * maxLength
    
    index = 0
    while index < len(word):
        cellString[startIndex] = word[index]
        startIndex += 1
        index += 1
        
    index = 0
    while index < maxLength:
        if cellString[index] == 0:
            cellString[index] = " "
        index += 1
        
    return ''.join(cellString)

#########################################################################   
## getData gets lines from a csv type file
#########################################################################

def getData(fileName):
    data = []

    with open(fileName) as inFile:
        for line in inFile:
            data.append(line.strip().split(','))
    return data

#########################################################################   
## getMaxLengths gets max word length from each column
#########################################################################

def getMaxLengths(wordList):
    maxLengths = [0] * len(wordList[0])

    for List in wordList:
        index = 0
        for word in List:
            if len(word) > maxLengths[index]:
                maxLengths[index] = len(word)
            index += 1
    return maxLengths

#########################################################################   
## buildLine will create cells in a line with proper alignment
#########################################################################

def buildLine(words, maxLengths):
    lineString = border
    formatString = corner

    index = 0
    for word in words:
        lineString += right(word, maxLengths[index])
        lineString += border
        formatString += (dash * maxLengths[index])
        formatString += corner
        index += 1

    print(lineString)
    print(formatString)

#########################################################################  
## main does the magic
#########################################################################

def main():
    #os.system('python randWordGen.py')
    lines = getData('MOCK_DATA.csv')
    maxs = getMaxLengths(lines)

    index = 0
    formatString = corner

    for word in lines[0]:
        formatString += (dash * maxs[index])
        formatString += corner
        index += 1

    print(formatString) # the first line
    for line in lines:
        buildLine(line, maxs)

main()
