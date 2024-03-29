
# runtime: O(n)
# space  : O(n)

class Solution:
    def romanToInt(self, s: str) -> int:

        kp = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }

        s = s.replace("IV", "IIII").replace("IX", "VIIII")
        s = s.replace("XL", "XXXX").replace("XC", "LXXXX")
        s = s.replace("CD", "CCCC").replace("CM", "DCCCC")

        o = 0
        for n in s:
            o += kp[n]

        return o

