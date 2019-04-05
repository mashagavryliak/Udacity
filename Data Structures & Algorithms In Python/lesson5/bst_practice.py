class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BST(object):
    def __init__(self, root):
        self.root = Node(root)

    def insert(self, new_val):
        self.insert_helper(self.root, new_val)

    def insert_helper(self, current, new_val):
        if new_val == current.value:
            return
        elif new_val < current.value:
            current.left = current.left or Node(new_val)
            current = current.left
        else:
            current.right = current.right or Node(new_val)
            current = current.right
        return self.insert_helper(current, new_val)

    def search(self, find_val):
        return self.search_helper(self.root, find_val)

    def search_helper(self, current, find_val):
        if current is None:
            return False
        elif current.value == find_val:
            return True
        elif find_val < current.value:
            return self.search_helper(current.left, find_val)
        else:
            return self.search_helper(current.right, find_val)


# Set up tree
tree = BST(4)

# Insert elements
tree.insert(2)
tree.insert(1)
tree.insert(3)
tree.insert(5)

# Check search
# Should be True
print tree.search(4)
# Should be False
print tree.search(6)