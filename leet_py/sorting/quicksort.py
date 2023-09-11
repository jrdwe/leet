# quicksort

# o(n log n) time (average) & o(1) space

# an iteration
# [5, 2, 1, 3]
# p = 3 s1 = { all < p } s2 = { all > p }
# p = 3 s1 = { 1, 2 } s2 = { 5 }
# [2, 1, 3, 5]
# p = 3 is now sorted

# when A[k] == p put into s1 or s2 randomly 

import random

def quicksort(a: list, l: int, h: int):
    if l < h:
        # random pivot: low + rand in range (0..high-low+1)
        r = l + random.randrange(h - l + 1)
        # [p, s1, s2, rand]
        a[l], a[r], m = a[r], a[l], l
        # sort partition
        for k in range(l + 1, h + 1):
            if a[k] < a[l] or a[k] == a[l] and random.randrange(2) == 0:
                m += 1
                a[m], a[k] = a[k], a[m]
        # put sorted pivot back
        a[l], a[m] = a[m], a[l]
        # recurse
        quicksort(a, m + 1, h)
        quicksort(a, l, m - 1)

    return a

if __name__ == '__main__':
    a = [4, 5, 22, 2, 5, 7, 8]
    quicksort(a, 0, len(a) - 1)
    print(a)
