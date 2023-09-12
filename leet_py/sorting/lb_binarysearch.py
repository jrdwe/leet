# lb_binarysearch

# finds the index of the first value to satisfy a condition
# [f, f, f, t, t, t, t]
#           ^ finds here

def lb_binarysearch(a: list, ok: callable):
    n = len(a)
    # empty array
    if n < 1:
        return -1

    # iterative search
    i, s = -1, len(a) - 1
    while s >= 1:
        while not ok(i + s): 
            i += s
        s //= 2

    return i + 1

if __name__ == '__main__':
    # a = [True, True, False, False, False, False]
    a = [False, False, False, False, True, True]

    print(lb_binarysearch(a, lambda x: a[x]))
