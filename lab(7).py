def lab7_5():
    n = int(input('n = '))
    arr = []
    for i in range(n - 1):
        arr.append(int(input()))
    k = 0
    for i in range(1, n-1):
        if arr[i] > arr[i-1] and arr[i] > arr[i+1]:
            k += 1
    print(k)