# 3 8 9
from decimal import ROUND_UP


def lab10_3():
    n = (str(input()).split(' '))
    m = (str(input()).split(' '))
    print([int(i) for i in list(set(n) & set(m))])

def lab10_8():
    n = int(input('n = '))
    seti = []
    tmp = ''
    while (True):
        tmp = input()
        if (tmp == "HELP"):
            break
        seti.append([int(i) for i in tmp.split(' ')])
    
    nowSet = set([i+1 for i in range(n)])
    for setik in seti:
        tmpSet = set(setik) & nowSet
        if (len(tmpSet) > len(nowSet)//2):
            print("YES")
            nowSet = tmpSet
        else :
            print("NO")
            nowSet = set(setik) ^ nowSet
    print(list(nowSet).sort())
            


def lab10_9():
    listOfSet = []
    n = int(input('n = '))
    for i in range(n):
        listOfSet.append(set())
        m = int(input('m = '))
        for j in range(m):
            tmp = input()
            listOfSet[i].add(tmp)

    allLang = listOfSet[0]
    for i in range(n):
        allLang = allLang & listOfSet[i]
    print(len(allLang))
    for i in allLang:
        print(i)

    anyLang = listOfSet[0]
    for i in range(n):
        anyLang = anyLang | listOfSet[i]
    print(len(anyLang))
    for i in anyLang:
        print(i)    

lab10_3()
print()
lab10_8()
print()
lab10_9()