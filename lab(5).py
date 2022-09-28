def lab5_4():
    s = (input('word = '))
    arr = s.split(' ')
    arr[0], arr[1] = arr[1], arr[0]
    print(arr[0] + ' ' + arr[1])
