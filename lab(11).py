# 6 7 8
def lab11_6():
    n = int(input())
    dictWords = dict()
    for i in range(n):
        words = input().split(' ')
        for j in words:
            if j in dictWords:
                dictWords[j] +=1
            else:
                dictWords[j] = 1
    needList = list()
    for i in dictWords:
        needList.append((dictWords[i], i))
    needList.sort()
    needList.reverse()
    for i in range(n):
        print(needList[i][1])

def lab11_7():
    n = int(input())
    dictWords = dict()
    for i in range(n):
        words = input().split(' ')
        dictWords[words[0]] = [i for i in words[1:]]
    
    n = int(input())
    for i in range(n):
        word = input()
        for i in dictWords:
            if (word in dictWords[i]):
                print(i)
                break

def lab11_8():
    n = int(input())
    dictWords = dict()
    for i in range(n):
        words = input().split(' ')
        for j in words[2:]:
            if (j in dictWords):
                dictWords[j].append(words[0])
            else:
                dictWords[j] = [words[0]]

    print(len(dictWords))
    for i in dictWords:
        tmp = ''
        for j in dictWords[i]:
            tmp += j + ' '
        print(i + ' - ' + tmp)

lab11_6()
print()
lab11_7()
print()
lab11_8()