#10
def sumOfDigitInThird(num):
    tmp = ''
    if (num < 0):
        num *= -1
    while(num > 0):
        mod = num % 3
        tmp = str(mod) + tmp
        num -=mod
        num //=3
    
    sum =0
    for i in tmp:
        sum += int(i)
    return sum

def getMagicNums(nums):
    newNums = []
    for i in range(len(nums)):
        if (nums[i] < 0):
            if (sumOfDigitInThird(nums[i]) == 12):
                newNums.append((i, nums[i]))
    return newNums

def iz1_10(fileName):
    inf = open(fileName, "r")
    line = inf.readline()
    line = (line.rstrip()).split(' ')
    n = int(line[0])
    k = int(line[1])
    d = int(line[2])

    nums = []
    for i in range(n):
        nums.append(int(inf.readline().rstrip()))
    
    magicNums = getMagicNums(nums)
    maxCountOfMagic = len(magicNums)

    sumList = [0]
    for i in range(n):
        sumList.append(nums[i]+sumList[i])

    maxSum = -10 **9
    kInc = 1
    while(k*kInc <= maxCountOfMagic):
        nowCountOfMagic = k*kInc
        for magicOffset in range(maxCountOfMagic-nowCountOfMagic+1):
            startOfMagicSubstr = magicNums[magicOffset][0]
            endOfMagicSubStr =magicNums[magicOffset+nowCountOfMagic-1][0]
            rangeBetweenFirstAndLastMagic = endOfMagicSubStr - startOfMagicSubstr +1
            
            dInc = rangeBetweenFirstAndLastMagic//d
            if (rangeBetweenFirstAndLastMagic % d != 0):
                dInc+=1
            freePozition = d - rangeBetweenFirstAndLastMagic % d

            isHasSubstr = True
            while(isHasSubstr):
                isHasSubstr = False
                for freePositionOffset in range(freePozition+1):
                    finalStartOfSubstr = startOfMagicSubstr-(freePozition-freePositionOffset)
                    finalEndOfSubstr = endOfMagicSubStr+freePositionOffset
                    
                    if (magicOffset > 0):
                        leftEnd = magicNums[magicOffset-1][0]
                    else:
                        leftEnd = -1
                    if (finalStartOfSubstr <= leftEnd):
                        continue
                    
                    if (magicOffset < maxCountOfMagic-nowCountOfMagic):
                        rightEnd = magicNums[magicOffset+nowCountOfMagic][0]
                    else:
                        rightEnd = n
                    if (finalEndOfSubstr >= rightEnd):
                        continue

                    
                    isHasSubstr = True
                    #nowSum = get_range_sum(finalStartOfSubstr+1,finalEndOfSubstr+1, bit) Деревье Фенвика неэффективно
                    nowSum = sumList[finalEndOfSubstr+1] - sumList[finalStartOfSubstr]
                    if (nowSum > maxSum):
                        maxSum = nowSum
                freePozition +=d
                dInc+=1
        kInc+=1
    
    if (maxSum == -10 ** 9):
        print('Нет решения')
    else:
        print(maxSum)

iz1_10("10a.txt") #Нет решения
iz1_10("10b.txt") #168674858