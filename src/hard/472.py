from typing import List

class Node:
    def __init__(self, char):
        self.c = char
        self.end = False
        self.children = [None for _ in range(26)]


class Trie:
    def __init__(self):
        self.root = Node('')

    def insert(self, word):
        node = self.root
        for c in word:
            idx = ord(c) - ord('a')
            if node.children[idx] is None:
                node.children[idx] = Node(c)
            node = node.children[idx]
        node.end = True

class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        ans = []
        tree = Trie()
        words.sort(key=lambda x:len(x))
        for word in words:
            if self.dfs(word, 0, tree, [False] * len(word)):
                ans.append(word)
            else:
                tree.insert(word)
        return ans

    def dfs(self, word, idx, tree, vis):
        if idx == len(word):
            return True
        if vis[idx]:
            return False
        vis[idx] = True
        node = tree.root
        for i in range(idx, len(word)):
            c = word[i]
            idx = ord(c) - ord('a')
            if node.children[idx] is None:
                return False
            node = node.children[idx]
            if node.end and self.dfs(word, i+1, tree, vis):
                return True
        return False

s = Solution()
print(s.findAllConcatenatedWordsInADict(["a","aa","aaa","aaaa","aaaaa","aaaaaa"]))