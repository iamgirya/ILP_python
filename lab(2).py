def lab2_7():
    x1 = int(input('Координаты ладьи:\n'))
    y1 = int(input(''))
    x2 = int(input('Координаты клетки:\n'))
    y2 = int(input(''))
    if 8 >= x1 >= 0 and 8 >= y1 >= 0 and 8 >= x2 >= 0 and 8 >= y2 >= 0:
        if x1 == x2 or y2 == y1:
            print('YES')
        else:
            print('NO')
    else:
        print('Ошибка')