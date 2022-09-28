def lab8_3():
    def capitalize(word):
        big_char = chr(ord(word[0])-32)
        return big_char+word[1:]
    s = (input('word = '))
    print(capitalize(s))