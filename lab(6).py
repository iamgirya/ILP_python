def lab6_4():
    x = float(input('x = '))
    y = float(input('y = '))
    n = 0
    while x < y:
        x *= 1.1
        n += 1
    print(n)