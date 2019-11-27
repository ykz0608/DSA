class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def __init__(self):
        self.root = None
        
    def insert(self, root, val):
        if root == None:
            root = TreeNode(val)
        elif val <= root.val:
            if root.val == None:
                root.left= TreeNode(val)
            else:
                self.insert(root.left, val)
        elif val >root.val:
            if root.val == None:
                root.right= TreeNode(val)
            else:
                self.insert(root.right, val)
        else:
            return None
            
    def insert_pre(self, root, val):
        if root == None:
            root = TreeNode(val)
        elif val <= root.val:
            if root.val == None:
                root.left= TreeNode(val)
            else:
                root.left = self.insert_pre(root.left, val)
        elif val > root.val:
            if root.val == None:
                root.right= TreeNode(val)
            else:
                root.right = self.insert_pre(root.right, val)
        return root

    def preorder(self, root):
        if root == None:
            return []
        return [root.val] + self.preorder(root.left) + self.preorder(root.right)
    
    def search(self, root, target):
        if root == None:
            return False
        else:
            if root.val == target:
                return root
            elif target <= root.val:
                return self.search(root.left,target)
            elif target > root.val:
                return self.search(root.right,target)
    
        
    def FM(self, root):
        if root.left:
            return self.FM(root.left)
        else:
            return root
    
    def delete(self, root, target):
        if root == None:
            return None
        
        elif target == root.val:
            if root.left and root.right:
                temp = self.FM(root.right)
                root.val = temp.val
                root.right = self.delete(root.right, temp.val)
            elif root.right == None and root.left == None:
                root = None
            elif root.right == None:
                root = root.left
            elif root.left == None:
                root = root.right
            else:
                return None
        
        elif root.val> target:
            root.left = self.delete(root.left, target)
            
        elif root.val< target:
            root.right = self.delete(root.right, target)
            
        return root
    
    def modify(self, root, target, new_val):
        if root == None:
            return 
        else:
            if root.val == target:
                root.val = new_val
                
            if root.left:
                self.modify(root.left, target, new_val)
        
            if root.right:
                self.modify(root.right, target, new_val)
            
        return root
    
