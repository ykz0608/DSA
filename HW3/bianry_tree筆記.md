# HW3 BINARY TREE
## 學習歷程：

### 二元搜索樹(Binary Search Tree)是基於二元樹的一種延伸，二元搜索樹的應用範圍很廣，可以利用在搜索、排序和提供資料集合基本結構，發展其他資料結構，所以也是重要的資料結構之一。

### 定義

定義除了繼承二元樹的定義外，二元搜索樹本身也有額外的定義，但可能會看到幾種不同的說法，而較多數人使用的定義如下：

* 左子樹不為空，則左子樹的所有節點的鍵值(Key)小於根節點的鍵值。
* 右子樹不為空，則右子樹的所有節點的鍵值(Key)大於根節點的鍵值。
* 左右子樹也都是二元搜索樹。
* 節點不會有重複的鍵值。
這個定義是樹中的節點都具有Key-value pair情況，有時候可能會其他變化：
    * 沒有鍵值，而用值(Value)來比較。
    * 允許重複的資料，此時會出現等於的情況，則將定義1.改成小於等於或者定義2.改成大於等於。

## 作業格式


```python
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None
        """
        :type val: int
        :type left: TreeNode or None
        :type right: TreeNode or None
        """
class Solution(object):
    def insert(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode(inserted node)
        """
    def delete(self, root, target):
        """
        :type root: TreeNode
        :type target: int
        :rtype: TreeNode(the root of new completed binary search tree) (cannot search())
        """
    def search(self, root, target):
        """
        :type root: TreeNode
        :type target: int
        :rtype: TreeNode(searched node)
        """
    def modify(self, root, target, new_val):
        """
        :type root: TreeNode
        :type target: int
        :type new_val: int
        :rtype:TreeNode(the root of new completed binary search tree) (cannot search())
        """
```

自己尝试寫一次:


```python
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def insert(self, root, val):
        if root == None:
            root = TreeNode(val)
        elif val < root.val:
            root.left = self.insert(root.left, val)
        elif val > root.val:
            root.right = self.insert(root.right, val)
        return root
    
    def printTree(self, root):
        # 打印二叉搜索树
        if root == None:
            return 
        self.printTree(root.left)
        print(root.val, end = ' ')
        self.printTree(root.right)
    
    
```


```python
bst = Solution()
root = TreeNode(5)
bstest1 = bst.insert(root, 3)
bstest2 = bst.insert(root, 3)
bstest3 = bst.insert(root, -5)
bstest4 = bst.insert(root, 8)
bstest5 = bst.insert(root, 7)
bstest6 = bst.insert(root, 6)
bstest7 = bst.insert(root, 10)

bst.printTree(root)
print(Solution().insert(root,5)==root,end = ' ')
print(Solution().insert(root,3)==root.left,end = ' ')



```

    -5 3 5 6 7 8 10 True False <__main__.TreeNode object at 0x000001FAD4D23148>
    

雖然成功但發現少一個重複的值“3”
少寫重複的值要怎麽處理


```python
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
    
    def printTree(self, root):
        # 打印二叉搜索树
        if root == None:
            return 
        self.printTree(root.left)
        print(root.val, end = ' ')
        self.printTree(root.right)
    
    
```
bst = Solution()
root = TreeNode(5)
bstest1 = bst.insert(root, 3)
bstest1 = bst.insert(root, 3)
bstest1 = bst.insert(root, -5)
bstest1 = bst.insert(root, 8)
bstest1 = bst.insert(root, 7)
bstest1 = bst.insert(root, 6)
bstest1 = bst.insert(root, 10)



```python
a=Solution().preorder(bstest1)
print(a)
```

    None
    


```python
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
    

bst = Solution()
root = TreeNode(5)
bstest1 = bst.insert(root, -5)
bstest1 = bst.insert(root, 3)
bstest1 = bst.insert(root, 3)
bstest1 = bst.insert(root, 8)
bstest1 = bst.insert(root, 7)
bstest1 = bst.insert(root, 10)
bstest1 = bst.insert(root, 6)



a=Solution().preorder2(bstest1)
print(a)
print(Solution().insert(root,5)==root)
print(Solution().insert(root,7)==root.right.left.left)
print(Solution().insert(root,-5)==root.left)
print("-----------------")
print(Solution().search(root,3)==root.left.right)
print(Solution().search(root,3)==root.left.right.left)
print(Solution().search(root,5)==root)
print(Solution().search(root,8)==root.right)
print(Solution().search(root,-5)==root.left)
print(Solution().search(root,7)==root.right.left)
print(Solution().search(root,10)==root.right.right)




```

    [5, [-5, 3, 3], [8, 7, 6, 10]]
    True
    False
    False
    -----------------
    True
    False
    True
    True
    True
    True
    True
    

root error


```python
bst = Solution()
root = TreeNode(5)
bstest1 = bst.insert(root, 3)
bstest2 = bst.insert(root, 3)
bstest3 = bst.insert(root, -5)
bstest4 = bst.insert(root, 8)
bstest5 = bst.insert(root, 7)
bstest6 = bst.insert(root, 6)
bstest7 = bst.insert(root, 10)
bstest8 = bst.insert(root, 8)
bstest9 = bst.insert(root, 11)
bstest10 = bst.insert(root, 57)


bst.printTree(root)
print(Solution().insert(root,5)==root,end = ' ')
print(Solution().insert(root,8)==root,end = ' ')
```

    -5 3 3 5 6 7 8 8 10 11 57 True True 

## 參考資料

### 參考網站:
>* https://emn178.pixnet.net/blog/post/94574434
>* 


```python

```


    ---------------------------------------------------------------------------

    ModuleNotFoundError                       Traceback (most recent call last)

    <ipython-input-20-4bd655a10d82> in <module>
    ----> 1 from pybst.draw import plot_tree
    

    ~\Anaconda3\lib\site-packages\pybst\draw.py in <module>
         19 import matplotlib.pyplot as plt
         20 import networkx as nx
    ---> 21 import bstree as bst
         22 
         23 def _get_pos_list(tree):
    

    ModuleNotFoundError: No module named 'bstree'

