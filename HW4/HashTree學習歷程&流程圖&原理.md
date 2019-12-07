# HW4 HASH TABLE
## 學習歷程：

### 哈希表
* Hash Table是根據關鍵碼值 (Key-Value) 而直接進行訪問的數據結構
* 通過把關鍵碼值映射到表中壹個位置來訪問記錄，以加快查找的速度
* 哈希表的實現主要需要解決兩個問題，哈希函數和沖突解決

### 哈希函數
* 哈希函數也叫散列函數
* 它對不同的輸出值得到壹個固定長度的消息摘要。
* 理想的哈希函數對于不同的輸入應該産生不同的結構，
* 同時散列結果應當具有同壹性

### 沖突解決
* 現實中的哈希函數不是完美的，當兩個不同的輸入值對應一個輸出值時，就會産生“碰撞”，這個時候便需要解決沖突。
* 常見的沖突解決方法有開放定址法，鏈地址法，建立公共溢出區等。實際的哈希表實現中，使用最多的是鏈地址法

###  Hash的應用

1. Hash主要用于信息安全領域中加密算法，它把壹些不同長度的信息轉化成雜亂的128位的編碼,這些編碼值叫做Hash值. 也可以說，Hash就是找到壹種數據內容和數據存放地址之間的映射關系。

2. 查找：哈希表，又稱爲散列，是壹種更加快捷的查找技術。當我知道key值以後，我就可以直接計算出這個元素在集合中的位置，根本不需要壹次又壹次的查找！

### 優缺點

* 優點：不論哈希表中有多少數據，查找、插入、刪除（有時包括刪除）只需要接近常量的時間即0(1）的時間級。速度比樹快，樹的操作通常需要O(N)的時間級。哈希表不僅速度快，編程實現也相對容易。

* 缺點：它是基于數組的，數組創建後難于擴展，某些哈希表被基本填滿時，性能下降得非常嚴重。


## 作業格式


```python
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
        """
        :type val: int
        :type next: ListNode
        :rtype: None        
        """
class MyHashSet:
    def __init__(self, capacity=5):
        self.capacity = capacity
        self.data = [None] * capacity
        """
        :type capacity: int
        :rtype: None
        """
    def add(self, key):
        """
        :type key: str
        :rtype: None
        """
    def remove(self, key):
        """
        :type key: str
        :rtype: None
        """
    def contains(self, key):
        """
        :type key: str
        :rtype: bool(True or False)
        """
```

## 流程圖
![](https://github.com/ykz0608/DSA/blob/master/image/hash%20table.svg)

## 嘗試寫code


```python
from Cryptodome.Hash import MD5
test=MD5.new()
test.update('word'.encode('utf-8'))
print(int(test.hexdigest(),16))
```

    261178219964662357386340107354023781930
    


```python
from Cryptodome.Hash import MD5
test=MD5.new()
test.update('word1'.encode('utf-8'))
print(int(test.hexdigest(),16))
```

    151698981254316234667945911935924933837
    


```python
from Cryptodome.Hash import MD5
test=MD5.new()
test.update('word'.encode('utf-8'))
print(int(test.hexdigest(),16))
```

    261178219964662357386340107354023781930
    


```python
from Cryptodome.Hash import MD5
test=MD5.new()
test.update('airplane'.encode('utf-8'))
print(int(test.hexdigest(),16))
```

    92932858071449192704270915748234345168
    

### contains part:
从contains開始個人認爲比較简单的


```python
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
        
class MyHashSet:
    from Cryptodome.Hash import MD5
    
    def __init__(self, capacity=5):
        self.capacity = capacity
        self.data = [None] * capacity
                        
    def contains(self, key):
        test = MD5.new()
        test.update(key.encode('utf-8'))
        num = int(test.hexdigest(),16)
        
        rem = num%self.capacity
        node = self.data[rem]
        
        if node == None:
            return False
        else:
            if node.val==num:
                return True
            elif node.val != num:
                node = node.next
            else :
                return False
        
                    
        
```

打算完成add再一起測試


```python
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
        
class MyHashSet:
    from Cryptodome.Hash import MD5
    
    def __init__(self, capacity=5):
        self.capacity = capacity
        self.data = [None] * capacity
        
    def add(self, key):
        test = MD5.new()
        test.update(key.encode('utf-8'))
        num = int(test.hexdigest(),16)
                        
    def contains(self, key):
        test = MD5.new()
        test.update(key.encode('utf-8'))
        num = int(test.hexdigest(),16)
        
        rem = num%self.capacity
        node = self.data[rem]
        
        if node == None:
            return False
        else:
            if node.val==num:
                return True
            elif node.val != num:
                node = node.next
            else :
                return False
        
                    
        
```

發現每次都要重複打
```python=
    h = MD5.new()
    h.update(key.encode('utf-8'))
    val = int(h.hexdigest(),16)
```
好麻煩 打算def個function


```python
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
        
class MyHashSet:
    from Cryptodome.Hash import MD5
    
    def __init__(self, capacity=5):
        self.capacity = capacity
        self.data = [None] * capacity
        
    def add(self, key):
        test = MD5.new()
        test.update(key.encode('utf-8'))
        num = int(h.hexdigest(),16)
        
    def hash_t(self, key):
        test = MD5.new()
        test.update(key.encode('utf-8'))
        num = int(test.hexdigest(),16)
        return num 
        
                        
    def contains(self, key):
        test = MD5.new()
        test.update(key.encode('utf-8'))
        num = int(test.hexdigest(),16)
        
        rem = num%self.capacity
        node = self.data[rem]
        
        if node == None:
            return False
        else:
            if node.val== num:
                return True
            elif node.val != num:
                node = node.next
            else :
                return False
        
                    
        
```

contains也改


```python
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
        
class MyHashSet:
    from Cryptodome.Hash import MD5
    
    def __init__(self, capacity=5):
        self.capacity = capacity
        self.data = [None] * capacity
        
    def add(self, key):
        input_num = MyHashSet.hash_t(self, key)
        
    def hash_t(self, key):
        test = MD5.new()
        test.update(key.encode('utf-8'))
        num = int(test.hexdigest(),16)
        return num 
        
                        
    def contains(self, key):
        input_num = MyHashSet.hash_t(self, key)
        rem = input_num%self.capacity
        node = self.data[rem]
        
        if node == None:
            return False
        else:
            if node.val==input_num:
                return True
            elif node.val != input_num:
                node = node.next
            else :
                return False
        
                    
        
```

寫add


```python
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
        
class MyHashSet:
    from Cryptodome.Hash import MD5
    
    def __init__(self, capacity=5):
        self.capacity = capacity
        self.data = [None] * capacity
        
    def add(self, key):
        input_num = MyHashSet.hash_t(self, key)
        rem = input_num%self.capacity
        node = self.data[rem]
        if node:
            
            if node.val !=input_num:
                node.next=ListNode(input_num)
                
            elif node.next:
                if node.val != input_num:
                    node = node.next
                else:
                    return
            else:
                return
        else:
            node = ListNode(input_num)
            self.data[rem] = node
        
        
        
    def hash_t(self, key):
        test = MD5.new()
        test.update(key.encode('utf-8'))
        num = int(test.hexdigest(),16)
        return num 
        
                        
    def contains(self, key):
        input_num = MyHashSet.hash_t(self, key)
        rem = input_num%self.capacity
        node = self.data[rem]
        
        if node == None:
            return False
        else:
            if node.val==input_num:
                return True
            elif node.val != input_num:
                node = node.next
            else :
                return False
        
                    
        
```

助教測值


```python
hashSet = MyHashSet()
hashSet.add('dog')
hashSet.add('pig')
rel = hashSet.contains('pig')
print(rel)
rel = hashSet.contains('dog')
print(rel)
rel = hashSet.contains('cat')
print(rel)
```

    True
    True
    None
    

contains有error
None 沒有顯示false

修改後:


```python
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
        
class MyHashSet:
    from Cryptodome.Hash import MD5
    
    def __init__(self, capacity=5):
        self.capacity = capacity
        self.data = [None] * capacity
        
    def add(self, key):
        input_num = MyHashSet.hash_t(self, key)
        rem = input_num%self.capacity
        node = self.data[rem]
        if node:
            
            if node.val !=input_num:
                node.next=ListNode(input_num)
                
            elif node.next:
                if node.val != input_num:
                    node = node.next
                else:
                    return
            else:
                return
        else:
            node = ListNode(input_num)
            self.data[rem] = node
        
        
        
    def hash_t(self, key):
        test = MD5.new()
        test.update(key.encode('utf-8'))
        num = int(test.hexdigest(),16)
        return num 
        
                        
    def contains(self, key):
        input_num = MyHashSet.hash_t(self, key)
        rem = input_num%self.capacity
        node = self.data[rem]
        
        if node == None:
            return False
        else:
            if node.val==input_num:
                return True
            else :
                return False
                    
        
```


```python
hashSet = MyHashSet()
hashSet.add('dog')
hashSet.add('pig')
rel = hashSet.contains('pig')
print(rel)
rel = hashSet.contains('dog')
print(rel)
rel = hashSet.contains('cat')
print(rel)
```

    True
    True
    False
    


```python
hashSet = MyHashSet()
hashSet.add('dog')
hashSet.add('pig')
rel = hashSet.contains('pig')
print(rel)
rel = hashSet.contains('dog')
print(rel)
rel = hashSet.contains('cat')
print(rel)
hashSet.add('bird')
rel = hashSet.contains('bird')
print(rel)

```

    True
    True
    False
    True
    

add and contains done! next remove


```python
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
        
class MyHashSet:
    from Cryptodome.Hash import MD5
    
    def __init__(self, capacity=5):
        self.capacity = capacity
        self.data = [None] * capacity
        
    def add(self, key):
        input_num = MyHashSet.hash_t(self, key)
        rem = input_num%self.capacity
        node = self.data[rem]
        if node:
            
            if node.val !=input_num:
                node.next=ListNode(input_num)
                
            elif node.next:
                if node.val != input_num:
                    node = node.next
                else:
                    return
            else:
                return
        else:
            node = ListNode(input_num)
            self.data[rem] = node
            
            
    def remove(self, key):
        input_num = MyHashSet.hash_t(self, key)
        rem = input_num%self.capacity
        node = self.data[rem]
         
        if node:
            if node.val == input_num:
                node = node.next
                self.data[rem] = node
            elif node.next:
                if node.next.val == input_num:
                    node.next = node.next.next
                else:
                    node = node.next
            else:
                return None
                       

        
        
        
        
    def hash_t(self, key):
        test = MD5.new()
        test.update(key.encode('utf-8'))
        num = int(test.hexdigest(),16)
        return num 
        
                        
    def contains(self, key):
        input_num = MyHashSet.hash_t(self, key)
        rem = input_num%self.capacity
        node = self.data[rem]
        
        if node == None:
            return False
        else:
            if node.val==input_num:
                return True
            else :
                return False
                    
        
```


```python
hashSet = MyHashSet()
hashSet.add('dog')
hashSet.add('pig')
rel = hashSet.contains('pig')
print(rel)
rel = hashSet.contains('dog')
print(rel)
rel = hashSet.contains('cat')
print(rel)
hashSet.add('bird')
rel = hashSet.contains('bird')
print(rel)
hashSet.remove('pig')
rel = hashSet.contains('pig')
print(rel)

```

    True
    True
    False
    True
    False
    


```python
hashSet = MyHashSet()
hashSet.add('dog')
hashSet.add('pig')
rel = hashSet.contains('pig')
print(rel)
rel = hashSet.contains('dog')
print(rel)
rel = hashSet.contains('cat')
print(rel)
hashSet.add('bird')
rel = hashSet.contains('bird')
print(rel)
hashSet.remove('pig')
rel = hashSet.contains('pig')
print(rel)
print("-----------------------------")
hashSet.add('dog')
hashSet.add('dog')
rel = hashSet.contains('dog')
print(rel)

```

    True
    True
    False
    True
    False
    -----------------------------
    True
    


```python
hashSet = MyHashSet()
hashSet.add('dog')
hashSet.add('pig')
rel = hashSet.contains('pig')
print(rel)
rel = hashSet.contains('dog')
print(rel)
rel = hashSet.contains('cat')
print(rel)
hashSet.add('bird')
rel = hashSet.contains('bird')
print(rel)
hashSet.remove('pig')
rel = hashSet.contains('pig')
print(rel)
print("-----------------------------")
hashSet.add('dog')
hashSet.add('dog')
rel = hashSet.contains('dog')
print(rel)
print("-----------------------------")
hashSet.remove('dog')
rel = hashSet.contains('dog')
print(rel)
```

    True
    True
    False
    True
    False
    -----------------------------
    True
    -----------------------------
    False
    


```python
hashSet = MyHashSet()
hashSet.add('dog')
hashSet.add('pig')
hashSet.add('pig')
hashSet.add('pig')
hashSet.add('dog')
hashSet.add('pig')
hashSet.add('dog')



rel = hashSet.contains('pig')
print(rel)
rel = hashSet.contains('dog')
print(rel)
rel = hashSet.contains('cat')
print(rel)
hashSet.add('bird')
rel = hashSet.contains('bird')
print(rel)
hashSet.remove('pig')
rel = hashSet.contains('pig')
print(rel)
print("-----------------------------")
hashSet.add('dog')
hashSet.add('dog')
rel = hashSet.contains('dog')
print(rel)
print("-----------------------------")
hashSet.remove('dog')
rel = hashSet.contains('dog')
print(rel)
```

    True
    True
    False
    True
    False
    -----------------------------
    True
    -----------------------------
    False
    

發現contains 少了抓重複值要改


```python
from Cryptodome.Hash import MD5

class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
        
class MyHashSet:
    from Cryptodome.Hash import MD5

    def __init__(self, capacity=5):
        self.capacity = capacity
        self.data = [None] * capacity
        
    def add(self, key):
        input_num = MyHashSet.hash_t(self, key)
        rem = input_num%self.capacity
        node = self.data[rem]
        if node:
            
            if node.val !=input_num:
                node.next=ListNode(input_num)
                
            elif node.next:
                if node.val != input_num:
                    node = node.next
                else:
                    return
            else:
                return
        else:
            node = ListNode(input_num)
            self.data[rem] = node
               
    def remove(self, key):
        input_num = MyHashSet.hash_t(self, key)
        rem = input_num%self.capacity
        node = self.data[rem]
         
        if node:
            if node.val == input_num:
                node = node.next
                self.data[rem] = node
            elif node.next:
                if node.next.val == input_num:
                    node.next = node.next.next
                else:
                    node = node.next
            else:
                return None
                       
    def hash_t(self, key):
        test = MD5.new()
        test.update(key.encode('utf-8'))
        num = int(test.hexdigest(),16)
        return num 
        
                        
    def contains(self, key):
        input_num = MyHashSet.hash_t(self, key)
        rem = input_num%self.capacity
        node = self.data[rem]

        
        if node == None:
            return False
        else:
            if node.val==input_num:
                return True
            elif node.val != input_num:
                node = node.next
                if node == None:
                    return False
                return True
            else :
                return False
            
        
        
```

test


```python
hashSet = MyHashSet()
hashSet.add('dog')
hashSet.add('pig')
hashSet.add('pig')
hashSet.add('pig')
hashSet.add('dog')
hashSet.add('pig')


rel = hashSet.contains('pig')
print(rel)
rel = hashSet.contains('dog')
print(rel)
rel = hashSet.contains('cat')
print(rel)
hashSet.add('bird')
rel = hashSet.contains('bird')
print(rel)
hashSet.remove('pig')
rel = hashSet.contains('pig')
print(rel)
print("-----------------------------")
hashSet.add('dog')
hashSet.add('dog')
rel = hashSet.contains('dog')
print(rel)
print("-----------------------------")
hashSet.remove('dog')
rel = hashSet.contains('dog')
print(rel)
```

    True
    True
    False
    True
    False
    -----------------------------
    True
    -----------------------------
    False
    

Final Code:


```python
from Cryptodome.Hash import MD5

class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
        
class MyHashSet:
    from Cryptodome.Hash import MD5

    def __init__(self, capacity=5):
        self.capacity = capacity
        self.data = [None] * capacity
        
    def add(self, key):
        input_num = MyHashSet.hash_t(self, key)
        rem = input_num%self.capacity
        node = self.data[rem]
        if node:
            if node.val !=input_num:
                node.next=ListNode(input_num)
                
            elif node.next:
                if node.val != input_num:
                    node = node.next
                else:
                    return
            else:
                return
        else:
            node = ListNode(input_num)
            self.data[rem] = node
               
    def remove(self, key):
        input_num = MyHashSet.hash_t(self, key)
        rem = input_num%self.capacity
        node = self.data[rem]
         
        if node:
            if node.val == input_num:
                node = node.next
                self.data[rem] = node
            elif node.next:
                if node.next.val == input_num:
                    node.next = node.next.next
                else:
                    node = node.next
            else:
                return None
                       
    def hash_t(self, key):
        test = MD5.new()
        test.update(key.encode('utf-8'))
        num = int(test.hexdigest(),16)
        return num 
        
                        
    def contains(self, key):
        input_num = MyHashSet.hash_t(self, key)
        rem = input_num%self.capacity
        node = self.data[rem]

        if node == None:
            return False
        else:
            if node.val==input_num:
                return True
            elif node.val != input_num:
                node = node.next
                if node == None:
                    return False
                return True
            else :
                return False
            
        
        
```

## 參考資料

### 參考網站:
>* https://docs.google.com/presentation/d/e/2PACX-1vT1HO9Nl475k2bR0l1x8_Tr4V5Wzx0BEqp9bpmHckvj8kTeJehhYVlOJUDVPhLQm6kjGCJ_sLMSBUw5/pub?start=false&loop=false&delayms=3000&slide=id.g790b8351ca_0_235
>* https://blog.csdn.net/duan19920101/article/details/51579136
>* https://www.jianshu.com/p/a4f8a6f9f541
>* https://blog.csdn.net/claroja/article/details/80007829
>* https://kknews.cc/code/r5mea4r.html
>* https://zhuanlan.zhihu.com/p/37165658
>* https://www.youtube.com/watch?v=oqzStHk36PI&feature=youtu.be
