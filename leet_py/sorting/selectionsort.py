# selectionsort

# o(n^2) time & o(1) space

def selectionsort(a: list):
    for i in range(len(a)):
        m = a.index(min(a[i:]))
        a[i], a[m] = a[m], a[i]
    return a

if __name__ == '__main__':
    a = [421, 598, 220, 221, 5231, 799, 82]
    print(selectionsort(a))

    a = [5085, 86031, 8066, 9243, 2505, 9431, 3111, 8054, 4225, 2550, 7647, 9589, 8467]
    print(selectionsort(a))
