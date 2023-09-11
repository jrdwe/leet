# binarysearch

def binarysearch(a: list, tg: int):
    n = len(a)
    # empty array
    if n < 1:
        return -1

    # iterative search
    i, s = 0, n // 2
    while s >= 1:
        while (s + i < n and a[s + i] <= tg):
            i += s
        s //= 2

    return -1 if a[i] != tg else i

if __name__ == '__main__':
    pass

# un autre choix
# l, h = 0, n - 1
# while l <= h:
#     m = (l + h) // 2    
#     if tg < a[m]:
#         h = m - 1
#     elif tg > a[m]:
#         l = m + 1
#     else:
#         return m
# return -1
