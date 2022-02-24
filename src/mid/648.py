from typing import List

class Node:
    def __init__(self, c=""):
        self.child = [None] * 26
        self.c = c
        self.end = False

class Trie:
    def __init__(self):
        self.root = Node()

    def insert(self, s):
        node = self.root
        for c in s:
            idx = ord(c) - ord('a')
            if node.child[idx] is None:
                node.child[idx] = Node(c)
            node = node.child[idx]
        node.end = True

    def search(self, s):
        node = self.root
        for i in range(len(s)):
            idx = ord(s[i]) - ord('a')
            if node.child[idx] is None:
                break
            node = node.child[idx]
            if node.end:
                return s[:i+1]
        return s

class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        root = Trie()
        for dic in dictionary:
            root.insert(dic)
        ans = ""
        ss = sentence.split(" ")
        for s in ss:
            ans += root.search(s) + " "
        return ans[:-1]


s = Solution()
assert s.replaceWords(dictionary = ["cat","bat","rat"], sentence = "the cattle was rattled by the battery") == "the cat was rat by the bat"
assert s.replaceWords(dictionary = ["a","b","c"], sentence = "aadsfasf absbs bbab cadsfafs") == "a a b c"
