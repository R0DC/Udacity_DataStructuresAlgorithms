class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BST(object):
    def __init__(self, root):
        self.root = Node(root)

    def insert(self, new_val):
        if new_val > self.root.value:
            if self.root.left:
                self.root.left.insert(new_val)
            else:
                self.root.left = BST(new_val)
        else:
            if self.root.right:
                self.root.right.insert(new_val)
            else:
                self.root.right = BST(new_val)

    def search(self, find_val):
        if self.root.value == find_val:
            return True
        if find_val < self.root.value:
            if self.root.left:
                self.root.left.search(find_val)
            else:
                return False
        else:
            if self.root.right:
                self.root.right.search(find_val)
            else:
                return False
        return False
    
# Set up tree
tree = BST(4)

# Insert elements
tree.insert(2)
tree.insert(1)
tree.insert(3)
tree.insert(5)

# Check search
# Should be True
print (tree.search(4))
# Should be False
print (tree.search(6))