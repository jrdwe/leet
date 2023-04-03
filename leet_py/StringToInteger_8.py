
# runtime: O(n)
# space:   O(n)

class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.lstrip()
        if len(s) < 1:
            return 0

        isNeg = True if s[0] == '-' else False

        i, n = 0, ""

        if s[0] == '+': i += 1
        if s[0] == '-': i += 1

        while i < len(s):
            if not s[i].isdigit():
                break
            n += s[i]
            i += 1

        if len(n) == 0:
            return 0

        n = int(n) * -1 if isNeg else int(n)

        if n < -2**31:    return -2**31
        if n > 2**31 - 1: return 2**31 - 1

        return n
