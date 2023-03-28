class BST:
    # three entities 
    def __init__(self, value=None):
        self.left = None
        self.right = None
        self.value = value
    
    def insert(self, value):
        # If tree is empty ...
        if not self.value:
            self.value = value
            return
        # If duplicate value coming in ...
        if self.value == value:
            return
        # Left sub tree ...
        if value < self.value:
            if self.left is not None:
                self.left.insert(value)
            else:
                self.left = BST(value)
        # right sub tree ...
        else:
            if self.right is not None:
                self.right.insert(value)
            else:
                self.right = BST(value)
            
    
    def preorder(self, values):
        if self.value is not None:
            values.append(self.value)
        if self.left is not None:
            self.left.preorder(values)
        if self.right is not None:
            self.right.preorder(values)
        return values

    def inorder(self, values):
        if self.left is not None:
            self.left.inorder(values)
        if self.value is not None:
            values.append(self.value)
        if self.right is not None:
            self.right.inorder(values)
        return values

    def postorder(self, values):
        if self.left is not None:
            self.left.postorder(values)
        if self.right is not None:
            self.right.postorder(values)
        if self.value is not None:
            values.append(self.value)
        return values

    def search(self, value):
        pass