class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree(object):
    def __init__(self, root):
        self.root = Node(root)

    def search(self, find_val):
        """Return True if the value
        is in the tree, return
        False otherwise."""
        if self.root == None:
            return []
        val_stack = []
        stack = [self.root]
        while len(stack) > 0:
            current = stack.pop()
            val_stack.append(current.value)
            if current.right:
                stack.append(current.right)
            if current.left:
                stack.append(current.left)
        if find_val in val_stack:
            return True
        else:
            return False

    def print_tree(self):
        """Print out all tree nodes
        as they are visited in
        a pre-order traversal."""
        if self.root == None:
            return []
        val_stack = []
        stack = [self.root]
        while len(stack) > 0:
            current = stack.pop()
            val_stack.append(current.value)
            if current.right:
                stack.append(current.right)
            if current.left:
                stack.append(current.left)
        for i in val_stack:
            print(i)
        
    def preorder_search(self, start, find_val):
        """Helper method - use this to create a 
        recursive search solution."""
        if self.root == None:
            return False
        left_val = preorder_search(self.root.left, find_val)
        right_val = preorder_search(self.root.right, find_val)
        if left_val == find_val:
            return True
        

    def preorder_print(self, start, traversal):
        """Helper method - use this to create a 
        recursive print solution."""
        return traversal


# Set up tree
tree = BinaryTree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)

# Test search
# Should be True
print (tree.search(4))
# Should be False
print (tree.search(6))

# Test print_tree
# Should be 1-2-4-5-3
print (tree.print_tree())