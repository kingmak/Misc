import random, string

rmax = 15  # row max
rmin = 2   # row min
cmax = 15  # col max
cmin = 2   # col min
smax = 8   # str max
smin = 2   # str min

pool = string.printable[:-37]
cols = random.randint(cmin, cmax)
rows = random.randint(rmin, rmax)

index = 0
wordList = []

for row in range(rows):
    wordList.append([])
    for col in range(cols):
        string = ''.join(random.sample(pool, random.randint(smin, smax)))
        wordList[index].append(string)
    index += 1

File = open('data.txt', 'w')
for List in wordList:
    File.write(','.join(List) + '\n') 
File.close()      