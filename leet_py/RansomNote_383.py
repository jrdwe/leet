
# runtime: O(n)
# space:   O(n)

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:

        kp = {}
        for ch in magazine:
            if ch not in kp:
                kp[ch] = 1
            else:
                kp[ch] += 1

        for ch in ransomNote:
            if ch not in kp:
                return False
            else:
                if kp[ch] == 0:
                    return False
                kp[ch] -= 1

        return True
