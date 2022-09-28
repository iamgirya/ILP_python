# 9 13 19
def lab12_9():
    while (True):
        tmp = input()
        if (tmp == ''):
            break
        try:
            toInt = int(tmp)
            if (toInt == 2):
                print("F")
            elif (toInt == 3):
                print("C")
            elif (toInt == 4):
                print("B")
            elif (toInt == 5):
                print("A")
            else:
                print("Неправильный формат")
        except:
            toChar = tmp
            if (toChar == "F"):
                print(2)
            elif (toChar == "C"):
                print(3)
            elif (toChar == "B"):
                print(4)
            elif (toChar == "A"):
                print(5)
            else:
                print("Неправильный формат")

def lab12_13():
    listOfElem = []
    try:
        inf = open("elements.txt", "r")
        line = inf.readline()
        while line != "":
            line = line.rstrip()
            elem = line.split(',')
            listOfElem.append((elem[0],elem[1],elem[2]))
            line = inf.readline()
    except FileNotFoundError:
        print("Невозможно открыть файл '%s'. Выходим...")
        return

    while (True):
        tmp = input()
        if (tmp == ''):
            break
        try:
            toInt = int(tmp)
            if (toInt-1 < len(listOfElem)):
                ind = toInt-1
                print(listOfElem[ind][0] + ' ' + listOfElem[ind][1] +' - '+ listOfElem[ind][2])
            else:
                print("Неправильный номер")
        except:
            toName = tmp
            obrs = [i[1] for i in listOfElem]
            names = [i[2] for i in listOfElem]
            if (toName in obrs):
                ind = obrs.index(toName)
                print(listOfElem[ind][0] + ' ' + listOfElem[ind][1] +' - '+ listOfElem[ind][2])
            elif (toName in names):
                ind = names.index(toName)
                print(listOfElem[ind][0] + ' ' + listOfElem[ind][1] +' - '+ listOfElem[ind][2])
            else:
                print("Неправильное обозначение")

def lab12_19():
    listOfwords = set()
    try:
        inf = open("words.txt", "r")
        line = inf.readline()
        while line != "":
            line = line.rstrip()
            listOfwords.add(line)
            line = inf.readline()
    except FileNotFoundError:
        print("Невозможно открыть файл '%s'. Выходим...")
        return
    inf.close()

    text = []
    fname = input("Введите имя файла: ")
    file_opened = False
    while file_opened == False:
        try:
            testInf = open(fname, "r")
            file_opened = True

            line = testInf.readline()
            while line != "":
                line = line.rstrip()
                text.append(line)
                line = testInf.readline()
        except FileNotFoundError:
            print("Файл '%s' не найден. Попробуйте еще.")
            fname = input("Введите имя файла: ")
    testInf.close()

    testOut = open(fname, "w")
    for i in text:
        newStr = ""
        for j in i.split(' '):
            if (j not in listOfwords):
                newStr +='ERROR<'+j+'> '
            else:
                newStr +=j+' '
        newStr = newStr[0:len(newStr)-1]+'\n'
        testOut.write(newStr)
    testOut.close()


lab12_9()
print()
lab12_13()
print()
lab12_19()