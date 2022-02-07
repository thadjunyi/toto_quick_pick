import random

# Variable to tweak
setCount = 20
numberGeneration = 6
lastWinningSet = [15, 28, 31, 32, 44, 49]
additionalNum = 18

# Fixed Variable
startNum = 1
endNum = 49

print("Winning Number:", lastWinningSet, "Additional Number:", additionalNum)
print()

#for each set
for i in range(setCount):

    #set generation
    list = []
    while len(list) < numberGeneration:
        num = random.randint(startNum, endNum)
        if num not in list:
            list.append(num)
    list.sort()

    #matched winning number with set
    winningCount = 0
    matchedList = []
    matchedCount = 0
    for item in list:
        if item in lastWinningSet:
            matchedList.append(item)
            matchedCount += 1
    if additionalNum in list:
        matchedList.append(additionalNum)
        matchedCount += 0.5

    #printing result
    print("Quick Pick Generator:", list)
    print("Matched number:", matchedCount, matchedList)
    print()
