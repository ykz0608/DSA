class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def insert(self, root, val):
        if root == None:
            root = TreeNode(val)
        elif val <= root.val:
            root.left = self.insert(root.left, val)
        elif val > root.val:
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
