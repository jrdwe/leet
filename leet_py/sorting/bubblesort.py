# bubblesort

# o(n^2) time & o(n) space

# with bubble from the back

def bubblesort(a: list):
    n = len(a)
    while n > 1:
        swap = False
        for i in range(n - 1):
            if a[i] > a[i + 1]:
                a[i], a[i + 1] = a[i + 1], a[i]
                swap = True

        # already sorted
        if not swap:
            break
        n -= 1
    return a

if __name__ == '__main__':
    a = [421, 598, 220, 221, 5231, 799, 82]
    print(bubblesort(a))

    # a = [5085, 86031, 8066, 9243, 2505, 9431, 3111, 8054, 4225, 2550, 7647, 9589, 8467]
    # print(bubblesort(a))
