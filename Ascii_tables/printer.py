corner = "+"
border = "|"
dash = "-"
space = " "

def center(word, maxLength):
    topString = "%s%s%s" % (corner, dash * maxLength, border)
    
    startIndex = maxLength / len(word)
    cellString = [0] * maxLength
    
    index = 0
    while index < len(word):
        cellString[startIndex] = word[index]
        startIndex += 1
        index += 1
        
    index = 0
    while index < maxLength:
        if type(cellString[index]) == int:
            cellString[index] = " "
        index += 1
        
    print topString
    print ''.join(cellString)

#def top(word):
#    string = "%s%s%splus + len(word)
    

#dashCount = maxLen + 2
#top = "%s%s%s%s%s" % (corner, line * dashCount, border, line * dashCount, corner)
#mid = "%s%s%s%s%s" % (border, space * dashCount, border, space * dashCount, border)
#low = top

(center("asd", 6))
