# HW2 MERGE SORT
## 學習歷程：

merge sort是什麽？
* 合併排序是建立在歸併操作上的一種有效的排序算法。該算法是採用分治法（Divide and Conquer）的一個非常典型的應用。
* 歸併操作(Merge)，也叫歸併算法，指的是將兩個已經排序的序列合併成一個序列的操作。歸併排序算法依賴歸併操作。歸併排序有多路歸併排序、兩路歸併排序 , 可用於內排序，也可以用於外排序。這裡僅對內排序的兩路歸併方法進行討論。
* 算法思路：
    1. 把 n 個紀錄看成 n 個長度為 l 的有序子表
    2. 進行兩兩歸併使記錄關鍵字有序，得到 n/2 個長度為 2 的有序子表
    3. 重複第 2 步直到所有記錄歸併成一個長度為 n 的有序表為止。

## 流程圖
老師有講解過MergeSort的流程，所以廢話不多說,理解概念之後畫出的


![](https://github.com/ykz0608/DSA/blob/master/image/merge%20sort.svg)

# 程式碼
试寫


```python
import random
import pandas 
import numpy as np

x = np.random.randint(-100,100,10)
#隨機生成數字
arr = x.tolist()
print("測試數值=",arr)
```

    測試數值= [-42, -67, 57, 79, 90, 21, 59, -100, -29, -100]
    


```python
left = arr[:len(arr)/2]
right = arr[len(arr/2):]
left,right
```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    <ipython-input-384-0e26ca2894d6> in <module>
    ----> 1 left = arr[:len(arr)/2]
          2 right = arr[len(arr/2):]
          3 left,right
    

    TypeError: slice indices must be integers or None or have an __index__ method


必須是整數==


```python
left = arr[:len(arr)//2]
right = arr[len(arr//2):]
left,right
```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    <ipython-input-385-e1835a9f12b9> in <module>
          1 left = arr[:len(arr)//2]
    ----> 2 right = arr[len(arr//2):]
          3 left,right
    

    TypeError: unsupported operand type(s) for //: 'list' and 'int'


應該先建立中心點再分割


```python
mid = len(arr)//2
left = arr[:mid]
right = arr[mid:]
left,right
```




    ([-42, -67, 57, 79, 90], [21, 59, -100, -29, -100])




```python
def split(data):
    mid = len(data)//2
    left = data[:mid]
    right = data[mid:]
    split(left),split(right)
    print(left,right)
```


```python
split(arr)
```


    ---------------------------------------------------------------------------

    RecursionError                            Traceback (most recent call last)

    <ipython-input-407-beeb403777db> in <module>
    ----> 1 split(arr)
    

    <ipython-input-406-75a8338c7e45> in split(data)
          3     left = data[:mid]
          4     right = data[mid:]
    ----> 5     split(left),split(right)
          6     print(left,right)
    

    ... last 1 frames repeated, from the frame below ...
    

    <ipython-input-406-75a8338c7e45> in split(data)
          3     left = data[:mid]
          4     right = data[mid:]
    ----> 5     split(left),split(right)
          6     print(left,right)
    

    RecursionError: maximum recursion depth exceeded while calling a Python object


需要結束條件


```python
def split(data):
    if len(data)//2 == 0:
        return data
    else:
        mid = len(data)//2
        left = data[:mid]
        right = data[mid:]
    left = split(left)
    right = split(right)
    return [left,right]

```


```python
split(arr)
```




    [[[[-42], [-67]], [[57], [[79], [90]]]],
     [[[21], [59]], [[-100], [[-29], [-100]]]]]



開始比較


```python
def split(data):
    if len(data)//2 == 0:
        return data
    else:
        mid = len(data)//2
        left = data[:mid]
        right = data[mid:]
        left = split(left)
        right = split(right)
    return [left,right]
    
    i=0
    j=0
    y=0
    while i != 0 and j != 0:
        if left[i] <= right[j]:
            data[y] = left[i]
            i = i+1
        else:
            data[y] = right[j]
            j=j+1
        y=y+1
    while i != 0:
        data[y] = left[i]
        i = i+1
        k=k+1
    while j!=0:
        data[y] = right[j]
        j=j+1
        k=k+1
            
    return data
            
        
            
```

沒有變化！逻辑應該沒错？！


```python
split(arr)
```




    [[[[-42], [-67]], [[57], [[79], [90]]]],
     [[[21], [59]], [[-100], [[-29], [-100]]]]]



```python
發現這邊需要改 這裏不需要結束條件

if len(data)//2 == 0:
        return data
    else:
        mid = len(data)//2
        left = data[:mid]
        right = data[mid:]
        left = split(left)
        right = split(right)
    return [left,right]


```


```python
def split(data):
    if len(data)>1:
        mid = len(data)//2
        left = data[:mid]
        right = data[mid:]
        split(left)
        split(right)
        
        i = 0
        j = 0
        y = 0
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                data[y] = left[i]
                i += 1
            else:
                data[y] = right[j]
                j+=1
            y += 1
        
        while i < len(left):
            data[y] = left[i]
            i += 1
            y += 1
        
        while j < len(right):
            data[y] = right[j]
            j += 1
            y += 1
        
    return data
```


```python
split(arr)
```




    [-100, -100, -67, -42, -29, 21, 57, 59, 79, 90]




```python
z = [85, -66, -24, 91, -15, 36, 33, 24, 3, -53]
z1= [1, 0, 8, 18, 13, 17, 19, 42, 32]
print('test2',split(z))
```

    test2 [-66, -53, -24, -15, 3, 24, 33, 36, 85, 91]
    


```python
z1= [1, 0, 8, 18, 13, 17, 19, 42, 32]
print('test3',split(z1))
```

    test3 [0, 1, 8, 13, 17, 18, 19, 32, 42]
    

### renew.ver



```


```python
z4= [67, 0, 8, 90, 13, 17, 19, 42, 32]
merge_sort(z4)
```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    <ipython-input-532-84940d3ef3af> in <module>
          1 z4= [67, 0, 8, 90, 13, 17, 19, 42, 32]
    ----> 2 merge_sort(z4)
    

    <ipython-input-531-1d6e68902027> in merge_sort(data)
         29     else:
         30         mid = len(data)//2
    ---> 31         left = merge_sort(data[:mid])
         32         right = merge_sort(data[mid:])
         33         return merge(left,right)
    

    <ipython-input-531-1d6e68902027> in merge_sort(data)
         29     else:
         30         mid = len(data)//2
    ---> 31         left = merge_sort(data[:mid])
         32         right = merge_sort(data[mid:])
         33         return merge(left,right)
    

    <ipython-input-531-1d6e68902027> in merge_sort(data)
         31         left = merge_sort(data[:mid])
         32         right = merge_sort(data[mid:])
    ---> 33         return merge(left,right)
    

    <ipython-input-531-1d6e68902027> in merge(left, right)
         14             array.append(b[j])
         15             j += 1
    ---> 16         elif a[i] <= b[j]:
         17             array.append(a[i])
         18             i += 1
    

    TypeError: 'int' object is not subscriptable



```python
def merge(a,b):
    lena = len(a)
    lenb = len(b)
    i_a = 0
    i_b = 0
    c = []
    while True:
        if i_a == lena and i_b == lenb:
            break
        elif i_b == lenb:
            c.append(a[i_a])
            i_a += 1
        elif i_a == lena:
            c.append(b[i_b])
            i_b += 1
        elif a[i_a] <= b[i_b]:
            c.append(a[i_a])
            i_a += 1
        else:
            c.append(b[i_b])
            i_b += 1

    return c

# Code for merge sort

def mergesort(x):
    if len(x) == 0 or len(x) == 1:
        return x
    else:
        middle = len(x)//2
        a = mergesort(x[:middle])
        b = mergesort(x[middle:])
        return merge(a,b)
```

# 純程式碼+文字說明


```python
def merge_sort(data):
    if len(data)>1:#結束條件
        mid = len(data)//2
        left = data[:mid]#左半部
        right = data[mid:]#右半部
        merge_sort(left)
        merge_sort(right)
        
        i = 0
        j = 0
        y = 0
        while i < len(left) and j < len(right):
            if left[i] <= right[j]: # if left<right i
                data[y] = left[i]
                i += 1
            else:
                data[y] = right[j]
                j+=1
            y += 1
        
        while i < len(left):
            data[y] = left[i]
            i += 1
            y += 1
        
        while j < len(right):
            data[y] = right[j]
            j += 1
            y += 1
        
    return data
```

# 作業格式版本


```python
class Solution(object):    
    def merge_sort(self,data):
        if len(data)>1:
            mid = len(data)//2
            left = data[:mid]
            right = data[mid:]
            self.merge_sort(left)
            self.merge_sort(right)
            
            i = 0
            j = 0
            y = 0
            while i < len(left) and j < len(right):
                if left[i] <= right[j]:
                    data[y] = left[i]
                    i += 1
                else:
                    data[y] = right[j]
                    j+=1
                y += 1
            
            while i < len(left):
                data[y] = left[i]
                i += 1
                y += 1
            
            while j < len(right):
                data[y] = right[j]
                j += 1
                y += 1
            
        return data
```


```python
output=Solution().merge_sort([72,2,-4,54,87,0,19])
output
```




    [-4, 0, 2, 19, 54, 72, 87]



# 參考資料

參考網站:

>* https://www.geeksforgeeks.org/merge-sort/
>* https://www.cnblogs.com/xxtalhr/p/10800699.html
>* https://www.geeksforgeeks.org/python-program-for-merge-sort/
>* https://runestone.academy/runestone/books/published/pythonds/SortSearch/TheMergeSort.html


```python

```
