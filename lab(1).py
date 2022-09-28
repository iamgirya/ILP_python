def lab1_4():
    n = int(input('Количество минут с начала дня = '))
    n %= 24 * 60
    hour = n // 60
    minutes = n % 60
    print(str(hour) + ':' + (str(minutes) if (minutes > 10) else '0' + str(minutes)))