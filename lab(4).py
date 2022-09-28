def lab4_11():
    n = int(input('n = '))
    arr = []
    for i in range(n - 1):
        arr.append(int(input()))
    for i in range(1, n + 1):
        if i not in arr:
            print(i)