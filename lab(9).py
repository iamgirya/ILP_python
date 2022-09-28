def lab9_4():
    n = int(input('n = '))
    matr = [[ abs(n-i-j-1) for j in range(n)] for i in range(n)]
    for i in matr:
        print(*i)
lab9_4()