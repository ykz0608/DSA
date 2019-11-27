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

# 流程圖
* insert
*
![](https://github.com/ykz0608/DSA/blob/master/image/binarysearchtree-insert.svg)
* case1:待刪除節點既無左子樹也無右子樹：直接刪除該節點即可
![](https://github.com/ykz0608/DSA/blob/master/image/binarysearchtree-delete%20case%201.svg)
* case2.待刪除節點只有左子樹或者只有右子樹：將其左子樹或右子樹根節點代替待刪除節點
![](https://github.com/ykz0608/DSA/blob/master/image/binarysearchtree-delete%20case%202.svg)
* case3.待刪除節點既有左子樹也有右子樹：找到該節點右子樹中最小值節點，使用該節點代替待刪除節點，然後在右子樹中刪除最小值節點
![](https://github.com/ykz0608/DSA/blob/master/image/binarysearchtree-delete%20case%203.svg)



自己尝试寫一次insert:


```python
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
        elif val < root.val:
            root.left = self.insert(root.left, val)
        elif val > root.val:
            root.right = self.insert(root.right, val)
        return root

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
```

加上BST的遍歷 用的是先序遍歷（root.left.right） 


```python
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
        elif val < root.val:
            root.left = self.insert(root.left, val)
        elif val > root.val:
            root.right = self.insert(root.right, val)
        return root
    
    def preorder(self, root):
        if root == None:
            return []
        return [root.val] + self.preorder(root.left) + self.preorder(root.right)

```


```python
bst = Solution()
root = TreeNode(5)
bstest1 = bst.insert(root, 3)
bstest1 = bst.insert(root, 3)
bstest1 = bst.insert(root, -5)
bstest1 = bst.insert(root, 8)
bstest1 = bst.insert(root, 7)
bstest1 = bst.insert(root, 6)
bstest1 = bst.insert(root, 10)
a=Solution().preorder(bstest1)
print(a)
```

    [5, 3, -5, 8, 7, 6, 10]
    

雖然成功但發現少一個重複的值“3”
少寫重複的值要怎麽處理



```python
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
            root.left = self.insert(root.left, val)
        elif val > root.val:
            root.right = self.insert(root.right, val)
        return root
    
    def preorder(self, root):
        if root == None:
            return []
        return [root.val] + self.preorder(root.left) + self.preorder(root.right)

```


```python
bst = Solution()
root = TreeNode(5)
bstest1 = bst.insert(root, 3)
bstest1 = bst.insert(root, 3)
bstest1 = bst.insert(root, -5)
bstest1 = bst.insert(root, 8)
bstest1 = bst.insert(root, 7)
bstest1 = bst.insert(root, 6)
bstest1 = bst.insert(root, 10)
a=Solution().preorder(bstest1)
print(a)
```

    [5, 3, 3, -5, 8, 7, 6, 10]
    

助教測值


```python
root = TreeNode(5)
root.left = TreeNode(3)  
root.left.left = TreeNode(3) 
root.left.left.left = TreeNode(-5) 
root.right = TreeNode(8)
root.right.left = TreeNode(7)
root.right.left.left = TreeNode(6)
root.right.right = TreeNode(10)
```


```python
print(Solution().insert(root,4)==root.left.right)
```

    False
    

修改後:


```python
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

    def preorder(self, root):
        if root == None:
            return []
        return [root.val] + self.preorder(root.left) + self.preorder(root.right)

```


```python
bst = Solution()
root = TreeNode(5)
bstest1 = bst.insert(root, 3)
bstest1 = bst.insert(root, 3)
bstest1 = bst.insert(root, -5)
bstest1 = bst.insert(root, 8)
bstest1 = bst.insert(root, 7)
bstest1 = bst.insert(root, 6)
bstest1 = bst.insert(root, 10)
a=Solution().preorder(bstest1)
print(a)
print("----------------------------------")
root = TreeNode(5)
root.left = TreeNode(3)  
root.left.left = TreeNode(3) 
root.left.left.left = TreeNode(-5) 
root.right = TreeNode(8)
root.right.left = TreeNode(7)
root.right.left.left = TreeNode(6)
root.right.right = TreeNode(10)
print(Solution().insert(root,4)==root.left.right)

```

    []
    ----------------------------------
    True
    

加一個insert_preorder方便觀察


```python
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

```


```python
bst = Solution()
root = TreeNode(5)
bstest1 = bst.insert_pre(root, 3)
bstest1 = bst.insert_pre(root, 3)
bstest1 = bst.insert_pre(root, -5)
bstest1 = bst.insert_pre(root, 8)
bstest1 = bst.insert_pre(root, 7)
bstest1 = bst.insert_pre(root, 6)
bstest1 = bst.insert_pre(root, 10)
a=Solution().preorder(bstest1)
print(a)
print("----------------------------------")
root = TreeNode(5)
root.left = TreeNode(3)  
root.left.left = TreeNode(3) 
root.left.left.left = TreeNode(-5) 
root.right = TreeNode(8)
root.right.left = TreeNode(7)
root.right.left.left = TreeNode(6)
root.right.right = TreeNode(10)
print(Solution().insert(root,4)==root.left.right)

```

    [5, 3, 3, -5, 8, 7, 6, 10]
    ----------------------------------
    True
    

Next:Search


```python
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
            return None
        if root.val == target:
            return root
        elif target <= root.val:
            return self.search(root.left,target)
        elif target > root.val:
            return self.search(root.right,target)
    
```


```python
root = TreeNode(5)
root.left = TreeNode(3)  
root.left.left = TreeNode(3) 
root.left.left.left = TreeNode(-5) 
root.right = TreeNode(8)
root.right.left = TreeNode(7)
root.right.left.left = TreeNode(6)
root.right.right = TreeNode(10)
print(Solution().search(root,7)==root.right.left)
print(Solution().search(root,10)==root.right.right)
```

    True
    True
    

修改search


```python
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
    
```


```python
root = TreeNode(5)
root.left = TreeNode(3)  
root.left.left = TreeNode(3) 
root.left.left.left = TreeNode(-5) 
root.right = TreeNode(8)
root.right.left = TreeNode(7)
root.right.left.left = TreeNode(6)
root.right.right = TreeNode(10)
print(Solution().search(root,7)==root.right.left)
print(Solution().search(root,10)==root.right.right)
```

    True
    True
    

search done!Next:Delete

* 想法:
    1. 如果节点是一片树叶，那么可以立即被删除
    2. 如果节点只有一个儿子，则将此节点parent的指针指向此节点的儿子，然后删除
    3. 如果节点有两个儿子，则将其右子树的最小数据代替此节点的数据，并将其右子树的最小数据
* 參考:
```python
def delete(self,x):
    if self.find(x):
        if x<self.key:
            self.left=self.left.delete(x)
            return self
        elif x>self.key:
            self.right=self.right.delete(x)
            return self
        elif self.left and self.right:
            key=self.right.findMin().key
            self.key=key
            self.right=self.right.delete(key)
            return self
        else:
            if self.left:
                return self.left
            else:
                return self.right
    else:
        return self
```
參考網站:https://www.cnblogs.com/linxiyue/p/3624597.html


```python
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
    

```


```python
bstest2 = bst.delete(root, 7)
b=Solution().preorder(bstest2)
print(Solution().delete(root,7)==root)
```

    True
    

中間跳過一萬字 加速中......


```python
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
        
            else:
                return root.val
        
        elif root.val> target:
             self.delete(root.left, target)
            
        elif root.val< target:
            self.delete(root.right, target)
            
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
    

    
bst = Solution()
root = TreeNode(5)
bstest1 = bst.insert(root, -5)
bstest1 = bst.insert(root, 3)
bstest1 = bst.insert(root, 3)
bstest1 = bst.insert(root, 8)
bstest1 = bst.insert(root, 7)
bstest1 = bst.insert(root, 10)
bstest1 = bst.insert(root, 6)

print(Solution().search(root,-5)==root.left)
print(Solution().search(root,3)==root.left.right)
print(Solution().search(root,7)==root.right.left)
print(Solution().search(root,6)==root.right.left.left)
print(Solution().search(root,10)==root.right.right)
a=Solution().preorder(bstest1)
print(a)
print("-----------------")
print("insert result")
print(Solution().insert(root,5)==root)
print(Solution().insert(root,7)==root)
print(Solution().insert(root,-5)==root)
a=Solution().preorder(bstest1)
print(a)
print("-----------------")
print("search result")
print(Solution().search(root,3)==root.left.right)
print(Solution().search(root,5)==root)
print(Solution().search(root,8)==root.right)
print(Solution().search(root,-5)==root.left)
print(Solution().search(root,10)==root.right.right)
print(Solution().search(root,6)==root.right.left.left)


e=Solution().preorder(bstest1)
print(e)
print("-----------------")
print("delete result")
bstest2 = bst.delete(root, 6)
bstest2 = bst.delete(root, -5)
b=Solution().preorder(bstest2)
print(Solution().delete(root,6)==root)
print(Solution().delete(root,-5)==root)
print(b)
print("-----------------")
print("modify result")
#print(Solution().modify(root,3,10)==root)
#print(Solution().modify(root,10,-2)==root)
#print(Solution().modify(root,8,9)==root)

bstest3 = bst.modify(root,8,11)
c1=Solution().preorder(bstest3)
print(c1)
bstest4 = bst.modify(root,10,-2)
c2=Solution().preorder(bstest4)
print(c2)
bstest5 = bst.modify(root,-2,9)
c3=Solution().preorder(bstest5)
print(c3)
print("-----------------")






```

    True
    True
    True
    True
    True
    [5, -5, 3, 3, 8, 7, 6, 10]
    -----------------
    insert result
    True
    True
    True
    [5, -5, -5, 3, 3, 5, 8, 7, 6, 7, 10]
    -----------------
    search result
    True
    True
    True
    True
    True
    True
    [5, -5, -5, 3, 3, 5, 8, 7, 6, 7, 10]
    -----------------
    delete result
    


    ---------------------------------------------------------------------------

    AttributeError                            Traceback (most recent call last)

    <ipython-input-95-4b864695ba05> in <module>
        127 bstest2 = bst.delete(root, 6)
        128 bstest2 = bst.delete(root, -5)
    --> 129 b=Solution().preorder(bstest2)
        130 print(Solution().delete(root,6)==root)
        131 print(Solution().delete(root,-5)==root)
    

    <ipython-input-95-4b864695ba05> in preorder(self, root)
         28         if root == None:
         29             return []
    ---> 30         return [root.val] + self.preorder(root.left) + self.preorder(root.right)
         31 
         32     def search(self, root, target):
    

    <ipython-input-95-4b864695ba05> in preorder(self, root)
         28         if root == None:
         29             return []
    ---> 30         return [root.val] + self.preorder(root.left) + self.preorder(root.right)
         31 
         32     def search(self, root, target):
    

    <ipython-input-95-4b864695ba05> in preorder(self, root)
         28         if root == None:
         29             return []
    ---> 30         return [root.val] + self.preorder(root.left) + self.preorder(root.right)
         31 
         32     def search(self, root, target):
    

    <ipython-input-95-4b864695ba05> in preorder(self, root)
         28         if root == None:
         29             return []
    ---> 30         return [root.val] + self.preorder(root.left) + self.preorder(root.right)
         31 
         32     def search(self, root, target):
    

    AttributeError: 'int' object has no attribute 'val'


中間跳過2萬字 加速中......

FInal code:
```python
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
    
```

## 參考資料

### 參考網站:
>* https://emn178.pixnet.net/blog/post/94574434
>* https://python-data-structures-and-algorithms.readthedocs.io/zh/latest/17_%E4%BA%8C%E5%8F%89%E6%9F%A5%E6%89%BE%E6%A0%91/binary_search_tree/
>* https://buptldy.github.io/2016/05/09/2016-05-09-Python%20BST/
>* https://thinkhard.tech/2017/05/29/python-data-structure-BST/
>* http://ddrv.cn/a/44089
>* https://www.cnblogs.com/linxiyue/p/3624597.html
>* https://blog.csdn.net/u010089444/article/details/70854510?utm_source=itdadao&utm_medium=referral
>* https://zhuanlan.zhihu.com/p/23334059
>* https://www.twblogs.net/a/5d4d09dcbd9eee541c30e5c9
>* https://www.cnblogs.com/lliuye/p/9118591.html


