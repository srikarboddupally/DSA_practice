class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def insert_into_BST(root, val):
    if not root:
        return TreeNode(val)
    if val < root.val:
        root.left = insert_into_BST(root.left, val)
    elif val > root.right:
        root.right = insert_into_BST(root.right, val)
    return root 
def minValueNode(root):
    curr = root
    while curr and curr.left:
        currr = curr.left
    return curr

def remove(root, val):
    if not root:
        return None
    
    if val > root.val:
        root.right = remove(root.right, val)
    elif val < root.val:
        root.left = remove(root.left, val)
    else:
        minNode = minValueNode(root.right)
        root.val = minNode.val
        root.right = remove(root.right, minNode.val)
    return root

def search(root, target):
    if not root:
        return False
    
    if root.val == target:
        return True
    elif target< root.val:
        return search(root.left, target)
    else:
        return search(root.right, target)