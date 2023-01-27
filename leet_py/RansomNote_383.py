
# runtime: O(n)
# space:   O(n)

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:

        pool = Counter(magazine)
        for ch in ransomNote:
            if ch not in pool or pool[ch] <= 0:
                return False
            pool[ch] -= 1

        return True
