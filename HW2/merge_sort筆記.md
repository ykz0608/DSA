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

x = np.random.randint(0,10,8)
#隨機生成數字
arr = x.tolist()
print("測試數值=",arr)
```

    測試數值= [1, 5, 9, 4, 2, 5, 9, 1]
    


```python
left = arr[:len(arr)/2]
right = arr[len(arr/2):]
left,right
```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    <ipython-input-12-0e26ca2894d6> in <module>
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

    <ipython-input-13-e1835a9f12b9> in <module>
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




    ([1, 5, 9, 4], [2, 5, 9, 1])




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

    <ipython-input-72-beeb403777db> in <module>
    ----> 1 split(arr)
    

    <ipython-input-71-75a8338c7e45> in split(data)
          3     left = data[:mid]
          4     right = data[mid:]
    ----> 5     split(left),split(right)
          6     print(left,right)
    

    ... last 1 frames repeated, from the frame below ...
    

    <ipython-input-71-75a8338c7e45> in split(data)
          3     left = data[:mid]
          4     right = data[mid:]
    ----> 5     split(left),split(right)
          6     print(left,right)
    

    RecursionError: maximum recursion depth exceeded while calling a Python object


需要結束條件


```python
def split(data):
    if len(data)//2 <= 0:
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




    [[[[1], [5]], [[9], [4]]], [[[2], [5]], [[9], [1]]]]



開始比較


```python
def split(data):
    if len(data)//2 <= 0:
        return data
    else:
        mid = len(data)//2
        left = data[:mid]
        right = data[mid:]
    left = split(left)
    right = split(right)
    return [left,right]
    
    p=0
    q=0
    if left[] < []
    p
```


```python
def merge(left, right):
    res = []
    while left and right:
        if left[0] < right[0]:
            res.append(left.pop(0))
        else:
            res.append(right.pop(0))
    res = res + left + right
    return res

def mergesort(lists):
    if len(lists) <= 1:
        return lists
    mid = len(lists)//2
    left = mergesort(lists[:mid])
    right = mergesort(lists[mid:])
    return merge(left,right)

```


```python
def print_lol(the_list,level):
    for each_item in the_list:
        if isinstance(each_item,list):
            print_lol(each_item,level+1)
        else:
            for tab_stop in range(level):
                print('\t',end='')
            print(each_item)
```


```python
mergesort(arr)
```




    [1, 1, 2, 4, 5, 5, 9, 9]


