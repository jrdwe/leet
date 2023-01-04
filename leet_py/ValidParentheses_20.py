
# runtime: O(n)
# space:   O(n)

class Solution:
    def isValid(self, s: str) -> bool:

        kp = {'(':')', '{':'}', '[':']'}
        stack = []

        for v in s:
            if v in kp.keys():
                stack.append(v)
            elif stack:
                last = stack.pop()
                if last in kp and kp[last] != v:
                    return False
            else:
                return False

        return not stack
