def left_sbt(self, node):
    if node and node.left:
        return node.left.data
    return None

def right_sbt(self, node):
    if node and node.right:
        return node.right.data
    return None

def parent(self, value):
    if self.root is None or self.root.data == value:
        return None

    queue = deque([self.root])

    while queue:
        current = queue.popleft()

        if current.left:
            if current.left.data == value:
                return current.data
            queue.append(current.left)

        if current.right:
            if current.right.data == value:
                return current.data
            queue.append(current.right)

    return None