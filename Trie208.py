class Trie(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.l=[]
        

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: None
        """
        self.l.append(word)
        

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        if word in self.l:
            return True
        else:
            return False
        

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        for i in self.l:
            if len(i)<len(prefix):
                continue

            if i[:len(prefix)]==prefix:
                return True
            else:
                continue
        return False
        
