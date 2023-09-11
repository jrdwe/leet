# countingsort

# o(n + U) time & o(U) space
# U is the max in the array

# doesn't work for negatives

def countingsort(a: list):
    t = [0 for i in range(max(a) + 1)]
    for i in a:
        t[i] += 1

    k = 0
    for i, v in enumerate(t):
        for j in range(v):
            a[k], k = i, k + 1

    return a

if __name__ == '__main__':
    a = [4, 5, 22, 2, 5, 7, 8]
    print(countingsort(a))
