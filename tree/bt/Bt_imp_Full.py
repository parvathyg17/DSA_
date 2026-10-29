
from collections import deque


# ============================================================
# 1. NODE CLASS
# ============================================================

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# ============================================================
# 2. BINARY TREE CLASS
# ============================================================

class Bt:
    def __init__(self):
        self.root = None

    # --------------------------------------------------------
    # A. INSERTION AND DISPLAY
    # --------------------------------------------------------

    # Insert a new node using level-order traversal (BFS)
    def insert(self, data):
        new_node = Node(data)

        if self.root is None:
            self.root = new_node
            return

        queue = deque([self.root])

        while queue:
            current = queue.popleft()

            if current.left is None:
                current.left = new_node
                return
            else:
                queue.append(current.left)

            if current.right is None:
                current.right = new_node
                return
            else:
                queue.append(current.right)

    # Display all nodes in level order
    def display(self):
        if self.root is None:
            print("Tree is empty")
            return

        queue = deque([self.root])

        while queue:
            current = queue.popleft()
            print(current.data, end=" ")

            if current.left:
                queue.append(current.left)

            if current.right:
                queue.append(current.right)

        print()

    # Get the immediate left child's value
    def show_left_sbt(self, node):
        if node is None or node.left is None:
            return None
        return node.left.data

    # Get the immediate right child's value
    def show_right_sbt(self, node):
        if node is None or node.right is None:
            return None
        return node.right.data

    # --------------------------------------------------------
    # B. TREE TRAVERSALS
    # --------------------------------------------------------

    # Inorder: Left -> Root -> Right
    def inorder(self, root):
        if root is None:
            return

        self.inorder(root.left)
        print(root.data, end=" ")
        self.inorder(root.right)

    # Preorder: Root -> Left -> Right
    def preorder(self, root):
        if root is None:
            return

        print(root.data, end=" ")
        self.preorder(root.left)
        self.preorder(root.right)

    # Postorder: Left -> Right -> Root
    def postorder(self, root):
        if root is None:
            return

        self.postorder(root.left)
        self.postorder(root.right)
        print(root.data, end=" ")

    # --------------------------------------------------------
    # C. COUNTING NODES
    # --------------------------------------------------------

    # Count all nodes in the tree
    def count_nodes(self, root):
        if root is None:
            return 0

        left = self.count_nodes(root.left)
        right = self.count_nodes(root.right)

        return 1 + left + right

    # Count leaf nodes (nodes with no children)
    def count_leaf_node(self, root):
        if root is None:
            return 0

        if root.left is None and root.right is None:
            return 1

        left = self.count_leaf_node(root.left)
        right = self.count_leaf_node(root.right)

        return left + right

    # Count internal nodes (nodes with at least one child)
    def count_internal_node(self, root):
        if root is None:
            return 0

        if root.left is None and root.right is None:
            return 0

        left = self.count_internal_node(root.left)
        right = self.count_internal_node(root.right)

        return 1 + left + right

    # --------------------------------------------------------
    # D. HEIGHT AND DEPTH
    # --------------------------------------------------------

    # Height measured in edges
    # Empty tree = -1, leaf node = 0
    def height(self, root):
        if root is None:
            return -1

        left = self.height(root.left)
        right = self.height(root.right)

        return 1 + max(left, right)

    # Find depth of a node containing target value
    # Root depth = 0; returns -1 if target not found
    def depth(self, root, target, level=0):
        if root is None:
            return -1

        if root.data == target:
            return level

        left = self.depth(root.left, target, level + 1)

        if left != -1:
            return left

        return self.depth(root.right, target, level + 1)

    # --------------------------------------------------------
    # E. PRINT LEAF AND INTERNAL NODES
    # --------------------------------------------------------

    # Print nodes with no children
    def print_leaf_node(self, root):
        if root is None:
            return

        if root.left is None and root.right is None:
            print(root.data, end=" ")
            return

        self.print_leaf_node(root.left)
        self.print_leaf_node(root.right)

    # Print nodes having at least one child
    def print_internal_node(self, root):
        if root is None:
            return

        if root.left is not None or root.right is not None:
            print(root.data, end=" ")

        self.print_internal_node(root.left)
        self.print_internal_node(root.right)

    # --------------------------------------------------------
    # F. LEFT VIEW AND RIGHT VIEW
    # --------------------------------------------------------

    # Print the first node at each level
    def left_view(self, root):
        if root is None:
            return

        queue = deque([root])

        while queue:
            n = len(queue)

            for i in range(n):
                current = queue.popleft()

                if i == 0:
                    print(current.data, end=" ")

                if current.left:
                    queue.append(current.left)

                if current.right:
                    queue.append(current.right)

    # Print the last node at each level
    def right_view(self, root):
        if root is None:
            return

        queue = deque([root])

        while queue:
            n = len(queue)

            for i in range(n):
                current = queue.popleft()

                if i == n - 1:
                    print(current.data, end=" ")

                if current.left:
                    queue.append(current.left)

                if current.right:
                    queue.append(current.right)

    # --------------------------------------------------------
    # G. TYPES OF BINARY TREES
    # --------------------------------------------------------

    # Full: Every node has either 0 or 2 children
    def is_full(self, root):
        if root is None:
            return True

        if root.left is None and root.right is None:
            return True

        if root.left is not None and root.right is not None:
            return (
                self.is_full(root.left)
                and self.is_full(root.right)
            )

        return False

    # Complete: All levels filled except possibly the last,
    # which must be filled from left to right
    def is_complete(self, root):
        if root is None:
            return True

        queue = deque([root])
        found_none = False

        while queue:
            current = queue.popleft()

            if current is None:
                found_none = True
            else:
                if found_none:
                    return False

                queue.append(current.left)
                queue.append(current.right)

        return True

    # Perfect: Every internal node has 2 children
    # and all leaf nodes are at the same depth
    def is_perfect(self, root):
        h = self.height(root)

        def check(node, depth):
            if node is None:
                return True

            if node.left is None and node.right is None:
                return depth == h

            if node.left is None or node.right is None:
                return False

            return (
                check(node.left, depth + 1)
                and check(node.right, depth + 1)
            )

        return check(root, 0)

    # Balanced: Height difference <= 1 at every node
    def is_balanced(self, root):
        if root is None:
            return True

        left = self.height(root.left)
        right = self.height(root.right)

        if abs(left - right) > 1:
            return False

        return (
            self.is_balanced(root.left)
            and self.is_balanced(root.right)
        )

    # Optimized balanced check: O(n)
    # -1 = empty subtree height
    # -2 = unbalanced subtree
    def is_balanced_opt(self, root):

        def check(node):
            if node is None:
                return -1

            left = check(node.left)
            if left == -2:
                return -2

            right = check(node.right)
            if right == -2:
                return -2

            if abs(left - right) > 1:
                return -2

            return 1 + max(left, right)

        return check(root) != -2

    # --------------------------------------------------------
    # H. REMOVE DUPLICATE VALUES
    # --------------------------------------------------------

    # Collect unique values using BFS, then rebuild the tree.
    # Note: Original tree structure may change.
    def remove_duplicates(self):
        if self.root is None:
            return

        seen = set()
        unique = []
        queue = deque([self.root])

        while queue:
            current = queue.popleft()

            if current.data not in seen:
                seen.add(current.data)
                unique.append(current.data)

            if current.left:
                queue.append(current.left)

            if current.right:
                queue.append(current.right)

        self.root = None

        for value in unique:
            self.insert(value)

    # --------------------------------------------------------
    # I. SUM OF NODES
    # --------------------------------------------------------

    # Sum of leaf nodes only
    def sum_leaf_node(self, root):
        if root is None:
            return 0

        if root.left is None and root.right is None:
            return root.data

        left = self.sum_leaf_node(root.left)
        right = self.sum_leaf_node(root.right)

        return left + right

    # Sum of all nodes, including root and internal nodes
    def sum_all_nodes(self, root):
        if root is None:
            return 0

        left = self.sum_all_nodes(root.left)
        right = self.sum_all_nodes(root.right)

        return root.data + left + right

    # --------------------------------------------------------
    # J. COMPARE TWO BINARY TREES
    # --------------------------------------------------------

    # Check whether two trees have identical structure
    # and identical values at corresponding nodes
    def identical(self, root1, root2):
        if root1 is None and root2 is None:
            return True

        if root1 is None or root2 is None:
            return False

        return (
            root1.data == root2.data
            and self.identical(root1.left, root2.left)
            and self.identical(root1.right, root2.right)
        )

    # --------------------------------------------------------
    # K. INVERT BINARY TREE
    # --------------------------------------------------------

    # Swap left and right children at every node
    def invert(self, root):
        if root is None:
            return None

        root.left, root.right = root.right, root.left

        self.invert(root.left)
        self.invert(root.right)

        return root

    # --------------------------------------------------------
    # L. CHECK WHETHER ONE TREE IS A SUBTREE OF ANOTHER
    # --------------------------------------------------------

    # Search every possible root and compare entire subtrees
    def is_subroot(self, root, sbroot):
        if sbroot is None:
            return True

        if root is None:
            return False

        if self.identical(root, sbroot):
            return True

        return (
            self.is_subroot(root.left, sbroot)
            or self.is_subroot(root.right, sbroot)
        )


# ============================================================
# 3. CREATE TEST TREES
# ============================================================

bt = Bt()
for value in [10, 20, 30, 40, 50, 60, 70]:
    bt.insert(value)

bt1 = Bt()
for value in [10, 20, 30, 40, 60, 70, 80]:
    bt1.insert(value)

bt2 = Bt()
for value in [20, 40, 50]:
    bt2.insert(value)


# ============================================================
# 4. TEST EACH FUNCTION
# ============================================================

print("\n========== INSERTION AND DISPLAY ==========")
print("Main tree:")
bt.display()
print("Left child of root:", bt.show_left_sbt(bt.root))
print("Right child of root:", bt.show_right_sbt(bt.root))

print("\n========== TREE TRAVERSALS ==========")
print("Inorder:", end=" ")
bt.inorder(bt.root)
print()
print("Preorder:", end=" ")
bt.preorder(bt.root)
print()
print("Postorder:", end=" ")
bt.postorder(bt.root)
print()

print("\n========== NODE COUNTS ==========")
print("Total nodes:", bt.count_nodes(bt.root))
print("Leaf nodes:", bt.count_leaf_node(bt.root))
print("Internal nodes:", bt.count_internal_node(bt.root))

print("\n========== HEIGHT AND DEPTH ==========")
print("Tree height:", bt.height(bt.root))
print("Left subtree height:", bt.height(bt.root.left))
print("Depth of node 30:", bt.depth(bt.root, 30))

print("\n========== PRINT LEAF / INTERNAL NODES ==========")
print("Leaf nodes:", end=" ")
bt.print_leaf_node(bt.root)
print()
print("Internal nodes:", end=" ")
bt.print_internal_node(bt.root)
print()

print("\n========== TREE VIEWS ==========")
print("Left view:", end=" ")
bt.left_view(bt.root)
print()
print("Right view:", end=" ")
bt.right_view(bt.root)
print()

print("\n========== BINARY TREE TYPES ==========")
print("Full:", bt.is_full(bt.root))
print("Complete:", bt.is_complete(bt.root))
print("Perfect:", bt.is_perfect(bt.root))
print("Balanced:", bt.is_balanced(bt.root))
print("Balanced optimized:", bt.is_balanced_opt(bt.root))

print("\n========== SUM OF NODES ==========")
print("Sum of leaf nodes:", bt.sum_leaf_node(bt.root))
print("Sum of all nodes:", bt.sum_all_nodes(bt.root))

print("\n========== TREE COMPARISON ==========")
print("Identical to bt1:", bt.identical(bt.root, bt1.root))
print("bt2 is a subtree of bt:", bt.is_subroot(bt.root, bt2.root))
print("bt is a subtree of bt1:", bt.is_subroot(bt1.root, bt.root))

print("\n========== REMOVE DUPLICATES ==========")
duplicate_tree = Bt()
for value in [10, 10, 20, 30, 40, 40, 50]:
    duplicate_tree.insert(value)

print("Before:", end=" ")
duplicate_tree.display()
duplicate_tree.remove_duplicates()
print("After:", end=" ")
duplicate_tree.display()

print("\n========== INVERT BINARY TREE ==========")
print("Before:", end=" ")
bt.display()
bt.invert(bt.root)
print("After:", end=" ")
bt.display()
