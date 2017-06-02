corner = "+"
border = "|"
dash = "-"
space = " "

def center(word, maxLength):
    startIndex = maxLength / 2
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

def lCell(word, maxLength):
    topString = "%s%s%s" % (corner, dash * maxLength, border)
    cellString = "%s%s%s" % (border, center("asdasd", maxLength), border)
    print(topString)
    print(cellString)
    

#dashCount = maxLen + 2
#top = "%s%s%s%s%s" % (corner, line * dashCount, border, line * dashCount, corner)
#mid = "%s%s%s%s%s" % (border, space * dashCount, border, space * dashCount, border)
#low = top
print("%s%s%s" % (border, center("asdasd", 19), border))
print(center("asd", 19))
(lCell("a", 19))
