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
    

Next:Delete


```python

```


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
        if target < root.val:
            return self.search(root.left,target)
        if target > root.val:
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
        if root:
            if root.val == target:
                root.val = new_val
            elif target < root.val:
                self.modify(root.left, target,new_val)
            elif target > root.val:
                self.modify(root.right, target,new_val)
        return root
    
    def modify2(self, root, target, new_val):
        if root:
            if root.val == target:
                root.val = new_val       
        if root.left:
            self.modify2(root.left, target, new_val)
        
        if root.right:
            self.modify2(root.right, target, new_val)
            
        return root
    
    def modify3(self, root, target, new_val):
        if root:
            if root.val == target:
                root.val = new_val
            if target < root.val:
                root.left = self.modify3(root.left, target, new_val)
            if target > root.val:
                root.right = self.modify3(root.right, target, new_val)
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
print(Solution().search(root,3)==root.left.right.left)
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
print(Solution().search(root,7)==root.right.left.left)
print(Solution().search(root,10)==root.right.right)
print(Solution().search(root,6)==root.right.left.left)
print(Solution().search(root,7)==root.right.left.left.right)


e=Solution().preorder2(bstest1)
print(e)
print("-----------------")
print("delete result")
bstest2 = bst.delete(root, 6)
bstest2 = bst.delete(root, -5)
b=Solution().preorder2(bstest2)
print(Solution().delete(root,6)==root)
print(Solution().delete(root,-5)==root)
print(b)
print("-----------------")
print("modify result")
print(Solution().modify(root,3,10)==root)
print(Solution().modify(root,10,-2)==root)
print(Solution().modify(root,8,9)==root)

bstest3 = bst.modify(root,3,10)
bstest3 = bst.modify(root,10,-2)
bstest3 = bst.modify(root,8,9)
c=Solution().preorder2(bstest3)
print(c)
print("-----------------")
print("modify2 result")
print(Solution().modify2(root,3,10)==root)
print(Solution().modify2(root,10,-2)==root)
print(Solution().modify2(root,8,9)==root)

bstest4 = bst.modify2(root,3,10)
bstest4 = bst.modify2(root,10,-2)
bstest4 = bst.modify2(root,8,9)
d=Solution().preorder2(bstest4)
print(d)
print("-----------------")
print("modify3 result")
print(Solution().modify3(root,3,10)==root)
print(Solution().modify3(root,10,-2)==root)
print(Solution().modify3(root,8,9)==root)

bstest5 = bst.modify3(root,3,10)
bstest5 = bst.modify3(root,10,-2)
bstest5 = bst.modify3(root,8,9)
f=Solution().preorder2(bstest5)
print(f)





```

    True
    True
    False
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
    False
    True
    True
    False
    [5, [-5, -5, 3, 3, 5], [8, 7, 6, 7, 10]]
    -----------------
    delete result
    True
    True
    [5, [3, -5, 5, 3], [8, 7, 7, 10]]
    -----------------
    modify result
    True
    True
    True
    [5, [10, 5, 3], [9, 7, 7, -2]]
    -----------------
    modify2 result
    True
    True
    True
    [5, [-2, 5, -2], [9, 7, 7, -2]]
    -----------------
    modify3 result
    True
    True
    True
    [5, [-2, 5, -2], [9, 7, 7, -2]]
    


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
    
   
    def preorder(self,root):
        if root is None:return []
        result=[root.val]
        resultl=self.preorder(root.left)
        resultr=self.preorder(root.right)
        return result+resultl+resultr
    
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
            return None
        elif target < root.val:
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
            else:
                return None
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
print(Solution().search(root,3)==root.left.right.left)
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
print(Solution().search(root,7)==root.right.left.left)
print(Solution().search(root,10)==root.right.right)
print(Solution().search(root,6)==root.right.left.left)
print(Solution().search(root,7)==root.right.left.left.right)


e=Solution().preorder2(bstest1)
print(e)
print("-----------------")
print("delete result")
bstest2 = bst.delete(root, 6)
bstest2 = bst.delete(root, -5)
b=Solution().preorder2(bstest2)
print(Solution().delete(root,6)==root)
print(Solution().delete(root,-5)==root)
print(b)
print("-----------------")
print("modify result")
#print(Solution().modify(root,3,10)==root)
#print(Solution().modify(root,10,-2)==root)
#print(Solution().modify(root,8,9)==root)

bstest3 = bst.modify(root,8,11)
c1=Solution().preorder2(bstest3)
print(c1)
print(Solution().search(root,11)==root.right)
print(Solution().search(root,10)==root.right.left.right)



bstest4 = bst.modify(root,10,-2)
c2=Solution().preorder2(bstest4)
print(c2)

bstest5 = bst.modify(root,8,9)


c3=Solution().preorder2(bstest5)
print(c3)
print("-----------------")






```

    True
    True
    False
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
    False
    True
    True
    False
    [5, [-5, -5, 3, 3, 5], [8, 7, 6, 7, 10]]
    -----------------
    delete result
    True
    True
    [5, [3, -5, 5, 3], [8, 7, 7, 10]]
    -----------------
    modify result
    [5, [3, 5, 3], [11, 7, 7, 10]]
    True
    False
    [5, [3, 5, 3], [11, 7, 7, -2]]
    [5, [3, 5, 3], [11, 7, 7, -2]]
    -----------------
    

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
>* https://emn178.pixnet.net/blog/post/94574434


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
    
   
    def preorder(self,root):
        if root is None:return []
        result=[root.val]
        resultl=self.preorder(root.left)
        resultr=self.preorder(root.right)
        return result+resultl+resultr
    
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
            return None
        elif target < root.val:
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
            else:
                return None
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
    

```


```python

```
