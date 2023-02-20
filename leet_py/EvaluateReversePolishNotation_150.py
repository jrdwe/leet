
# runtime: O(n)
# space:   O(n)

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        ops, sta = ['+', '-', '*', '/'], []
        for ch in tokens:
            if ch not in ops:
                sta.append(ch)
            else:
                v1, v2 = sta.pop(), sta.pop()
                if   ch == '+':
                    sta.append(int(v1) + int(v2))
                elif ch == '-':
                    sta.append(int(v2) - int(v1))
                elif ch == '/':
                    sta.append(int(v2) / int(v1))
                elif ch == '*':
                    sta.append(int(v1) * int(v2))
                else:
                    return False

        return int(sta[0]) if len(sta) == 1 else False
