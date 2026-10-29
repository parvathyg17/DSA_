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
  def search(self,words):
    node=self.root
    for char in words:
      if char not in node.children:
        return False
      node=node.children[char]
    return node.is_end
  def display(self):
    words=[]
    def dfs(node,current):
      if node.is_end:
        words.append(current)
      for char,next_node in node.children.items():
        dfs(next_node,current+char)
    dfs(self.root, "")
    print(words)
  def starts_with_word_and_count(self,prefix):
    node=self.root
    for char in prefix:
      if char not in node.children:
        return [],0
      node=node.children[char]
    words=[]
    count=0
    def dfs(node,current):
      nonlocal count
      if node.is_end:
        words.append(current)
        count+=1
      for char,next_node in node.children.items():
        dfs(next_node,current+char)
    dfs(node,prefix)
    return words,count
  def starts_with(self,prefix):
    node=self.root
    for char in prefix:
      if char not in node.children:
        return False
      node=node.children[char]
    words=[]
    def dfs(node,current):
      if node.is_end:
        words.append(current)
      for char,next_node in node.children.items():
        dfs(next_node,current+char)
    dfs(node,prefix)
    return words
  def delete(self,word):
    def dfs(node,index):
      if index==len(word):
        if not node.is_end:
          return False
        node.is_end=False
        return(len(node.children)==0)
      char=word[index]

      if char not in node.children:
        return False
      child_node=node.children[char]
      should_delete = dfs(child_node, index + 1)
      if should_delete:

        del node.children[char]
        return (
          not node.is_end
            and len(node.children) == 0
                )
      return False

    dfs(self.root, 0)
          
  


tr=Trie()
tr.insert("cat")
tr.insert("car")
tr.insert("dog")
tr.display()
print(tr.search("dogg"))
print(tr.starts_with("c"))
print(tr.delete("cat"))
tr.display()
print(tr.starts_with_word_and_count("ca"))


  
  