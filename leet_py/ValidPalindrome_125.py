
# runtime: O(n)
# space: O(n)

class Solution:
    def isPalindrome(self, s: str) -> bool:

        a = ""
        for x in s:
            # checks if valid alphanumeric char
            if x.isalpha(): a += x.lower()

            # checks if valid numeric char
            if x.isnumeric(): a += x

        # a[::-1] reverses the string
        return a == a[::-1]
