# radixsort

# o(w + (N + k)) time & o(N + k) space

# only base 10

import collections

def radixsort(a: list):
    # find longest number of digits
    w = max([len(list(str(x))) for x in a])

    # base 10 configure queues
    q = [collections.deque([]) for x in range(10)]

    for i in range(-1, -1 - w, -1):
        for j in a:
            # preceding zeroes if missing digits
            if -1 * i > len(str(j)):
                q[0].append(j)
            # add to relevent bucket
            else:
                b = int(str(j)[i])
                q[b].append(j)

        # unwind, pop all in order
        k = 0
        for v in q:
            while v:
                a[k] = v.popleft()
                k += 1
    return a

if __name__ == '__main__':
    # a = [421, 598, 220, 221, 5231, 799, 82]
    # print(radixsort(a))

    a = [5085, 86031, 8066, 9243, 2505, 9431, 3111, 8054, 4225, 2550, 7647, 9589, 8467]
    print(radixsort(a))
