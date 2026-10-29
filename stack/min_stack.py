class stack:
    def __init__(self):
        self.stack=[]
        self.min_stack=[]
    def push(self,val):
        self.stack.append(val)
        if not self.min_stack:
            self.min_stack.append(val)
        else:
            current=min(val,self.min_stack[-1])
            self.min_stack.append(current)
    def min_element(self):
        return self.min_stack[-1]
m=stack()
m.push(10)
m.push(20)
m.push(30)
m.push(40)
s=m.min_element()
print(s)