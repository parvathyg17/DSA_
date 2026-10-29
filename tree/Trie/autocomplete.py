class TrieNode:
  def __init__(self):
    self.children={}
    self.is_end=False
class Trie:
  def __init__(self):
    self.root=TrieNode()
  def insert(self,words):

    node=self.root
    for char in words:
      if char not in node.children:
        node.children[char]=TrieNode()

      node=node.children[char]
    node.is_end=True
  def autocomplete(self,prefix):
    node = self.root
    for char in prefix:
      if char not in node.children:
        return []
      node=node.children[char]
    words=[]

    def dfs(node,current):
      if node.is_end:
        words.append(current)
      for char,next_node in node.children.items():
        dfs(next_node,current+char)
    dfs(node,prefix)
    return words
        
    

tr=Trie()
tr.insert("cat")
tr.insert("car")
tr.insert("dog")
tr.insert("cash")
tr.insert("door")
s=tr.autocomplete("ca")
print(s)



  
  