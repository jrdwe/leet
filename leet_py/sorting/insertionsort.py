# insertionsort

# o(n^2) time & o(1) space

def insertionsort(a: list):
    for i in range(1, len(a)):
        x, j = a[i], i - 1
        while j >= 0 and a[j] > x:
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = x
    return a

if __name__ == '__main__':
    # a = [421, 598, 220, 221, 5231, 799, 82]
    # print(insertionsort(a))

    a = [5085, 86031, 8066, 9243, 2505, 9431, 3111, 8054, 4225, 2550, 7647, 9589, 8467]
    print(insertionsort(a))
