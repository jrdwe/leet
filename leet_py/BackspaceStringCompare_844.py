
# runtime: O(n + m)
# space  : O(n + m)

class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:

        def compute(x: str):
            stack = []
            for ch in x:
                if ch != "#":
                    stack.append(ch)
                elif stack:
                    stack.pop()
            return stack

        return compute(s) == compute(t)
