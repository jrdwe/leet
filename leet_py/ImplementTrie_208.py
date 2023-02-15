
class TNode:
    def __init__(self):
        self.object = [None] * 26
        self.is_word = False

class Trie:
    def __init__(self):
        self.root = TNode()

    def insert(self, word: str) -> None:
        node = self.root
        for ch in word:
            i = ord(ch) - ord('a')
            if node.object[i] is None:
                node.object[i] = TNode()
            node = node.object[i]
        node.is_word = True

    def search(self, word: str) -> bool:
        node = self.root
        for ch in word:
            i = ord(ch) - ord('a')
            if node.object[i] is None:
                return False
            node = node.object[i]
        return node.is_word

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for ch in prefix:
            i = ord(ch) - ord('a')
            if node.object[i] is None:
                return False
            node = node.object[i]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)

