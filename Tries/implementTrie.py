class Trie:

    def __init__(self):
      self.val = ''
      self.leafs = {}

    def insert(self, word: str) -> None:
      branch = Trie()
      if word[0] in self.leafs.keys():
        return self.leafs[word[0]]
      if len(word) > 0:
        branch.val = word[0]
        branch.insert(word[1:])
        self.leafs[branch.val] = branch
      else:
        branch.val = ''
        self.leafs[branch.val] = branch

    def search(self, word: str) -> bool:
      print(word)
      print(list(self.leafs.keys()))
      if word == '' and '' in self.leafs.keys():
        return True
      if word == '' and '' not in self.leafs.keys():
        return False
      if word[0] in self.leafs.keys():
        return self.leafs[word[0]].search(word[1:])
      return False
    
    def startsWith(self, prefix: str) -> bool:
      if prefix == '':
        return True
      if prefix[0] in self.leafs.keys():
        return self.leafs[prefix[0]].startsWith(prefix[1:])
      return False
      

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)

trie = Trie()
trie.insert("apple")
print(trie.search("apple")==True)
print(trie.search("app")==False)
print(trie.startsWith("app")==True)
trie.insert("app")
print(trie.search("app")==True)
trie.insert("apps")
print(trie.search("app")==True)