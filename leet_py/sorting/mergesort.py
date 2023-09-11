# mergesort

# o(n log n) time & o(n) space

# [5, 2, 1, 3]
# [5, 2] [1, 3]
# [5] [2] [1] [3]
# ... and sort it

def mergesort(a: list):
    if len(a) > 1:
        m = len(a) // 2
        l, r = a[:m], a[m:]

        mergesort(l)
        mergesort(r)

        i, j, k = 0, 0, 0
        while i < len(l) and j < len(r):
            if l[i] <= r[j]:
                a[k] = l[i]
                i += 1
            else:
                a[k] = r[j]
                j += 1
            k += 1

        while j < len(r):
            a[k] = r[j]
            k += 1
            j += 1   

        while i < len(l):
            a[k] = l[i]
            k += 1
            i += 1

    return a

if __name__ == '__main__':
    pass
