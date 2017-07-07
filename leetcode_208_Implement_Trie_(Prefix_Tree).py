#208. Implement Trie (Prefix Tree)
#使用前缀字典树


class TrieNode(object):
    def __init__(self):
        self.children={}
        self.word=False


class Trie(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root=TrieNode()
        

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        node=self.root
        for it in word:
            if it not in node.children:
                node.children[it]=TrieNode()
            node=node.children[it]
        node.word=True
            
        

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        node=self.root
        for it in word:
            if it not in node.children:
                return False
            node=node.children[it]
        return node.word
                

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        node=self.root
        for it in prefix:
            if it not in node.children:
                return False
            node=node.children[it]
        return True

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)