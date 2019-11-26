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
                root.left = self.insert(root.left, val)
        elif val > root.val:
            if root.val == None:
                root.right= TreeNode(val)
            else:
                root.right = self.insert(root.right, val)
        return root
    
   
    def preorder(self,root):
        if root is None:return []
        result=[root.val]
        resultl=self.preorder(root.left)
        resultr=self.preorder(root.right)
        return result+resultl+resultr
    
    def preorder2(self,root):
        if root is None:return []
        result=[]
        result.append(root.val)
        result.append(self.preorder(root.left))
        result.append(self.preorder(root.right))
        return result
    
    def preorder1(self,root,arr):
        if not root:return []
        arr.append(root.val)
        self.preorder1(root.left)        
        self.preorder1(root.right)

    
    def search(self, root, target):
        if root == None:
            return False
        if root.val == target:
            return root
        elif target <= root.val:
            return self.search(root.left,target)
        elif target > root.val:
            return self.search(root.right,target)
        
    def findMin(self, root):
        if root.left:
            return self.findMin(root.left)
        else:
            return root
        
    def findMax(self, root):
        if root.right:
            return self.findMax(root.right)
        else:
            return root
        
    def delete(self, root, target):
        if root == None:
            return 
        if target < root.val:
            root.left = self.delete(root.left, target)
        elif target > root.val:
            root.right = self.delete(root.right, target)
        else:
            if root.left and root.right:
                temp = self.findMin(root.right)
                root.val = temp.val
                root.right = self.delete(root.right, temp.val)
            elif root.right == None and root.left == None:
                root = None
            elif root.right == None:
                root = root.left
            elif root.left == None:
                root = root.right
        return root
    
    def modify(self, root, target, new_val):
        if root == None:
            return False
        else:
            if root.val == target:
                root.val = new_val
                
            if root.left:
                self.modify(root.left, target, new_val)
        
            if root.right:
                self.modify(root.right, target, new_val)
            
        return root
