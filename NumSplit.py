def numSplit(num):
    numSplitList = []

    for i in range(len(str(num))):
        splitedNum = int(int(str(num)[i]) * ( 10 ** len(str(num)) / 10 ** (i+1)))

        if splitedNum != 0:
            numSplitList.append(splitedNum)

    return numSplitList 

print(numSplit(2022))