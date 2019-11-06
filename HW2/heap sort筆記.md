# HW2 HEAP SORT
## 學習歷程：

heap sort 是什麽？
選擇排序法的概念簡單，以降冪為例，每次從未排序部份選一最小值，插入已排序部份的後端，其時間主要花費於在整個未排序部份尋找最小值，如果能讓搜尋最小值的方式加 快，選擇排序法的速率也就可以加快，Heap排序法讓搜尋的路徑由樹根至最後一個樹葉，而不是整個未排序部份，因而稱之為改良的選擇排序法。

**解法**
* Heap排序法使用堆積樹（Heap tree），樹是一種資料結構，而堆積樹是一個二元樹，每個父節點最多只有兩個子節點，堆積樹的 父節點若小於子節點，則稱之為最小堆積（Min heap），父節點若大於子節點，則稱之為最大堆積（Max heap），而同一層的子節點則無需理會其大小關係，可以使用一維陣列來儲存堆積樹的所有元素與其順序，為了計算方便，使用的起始索引是1而不是0，索引1是樹根位置，如果左子節點儲存在陣列中的索引為s，則其父節點的索引為s/2，而右子節點為s+1。

* 首先必須知道如何建立堆積樹，以最小堆積為例，加至堆積樹的元素會先放置在最後一個樹葉節點位置，然後檢查父節點是否小於子節點，將小的元素不斷與父節點交換，直到滿足堆積樹的條件為止，建立好堆積樹之後，樹根一定是所有元素的最小值。
* 排序應用時：
1. 將最小值取出 
2. 調整樹為最小堆積樹


* 不斷重複以上的步驟，就可以達到排序的效果，最小值取出方式是將樹根與最後一個樹葉節點交換，然後切下樹葉節點，重新調整樹為堆積樹，調整過程中，找出父節點兩子節點中較小的一個進行交換，調整完畢後，樹根節點又是最小值了，於是可以重覆這個步驟，再取出最小值，並調整樹為堆積樹，如此重覆步驟之後，由於使用一維陣列來儲存堆積樹，每次將樹葉與樹根交換的動作就是將最小值放至後端的陣列，所以最後陣列就是變為已排序的狀態。

* 堆積樹在建立時，就樹葉到樹根的路徑來看，是氣泡排序。堆積排序若看每次選出最小值樹根與最後一個樹葉交換，是選擇排序，後續進行調整的過程中，就樹根到樹葉的路徑來看，實際上也在進行氣泡排序。如果以視覺化來看排序過程，已排序部份的出現可很明顯地看出像是選擇排序，調整過程則沒那麼明顯的視覺效果，因此Heap排序法被稱為改良的選擇排序法。

**總結**
* 是利用堆性質的一種選擇排序，在堆頂選出最大值或者最小值
* 堆排序的時間複雜度為O(nlogn)。
* 由於堆排序對原始記錄的排序狀態並不敏感，因此它無論是最好、最壞和平均時間複雜度均為O(nlogn)。
## 參考資料

### 參考網站:
>* https://github.com/pecu/DSA/blob/master/06_HeapSort/heapSort.py
>* https://openhome.cc/Gossip/AlgorithmGossip/HeapSort.htm#Python
>* http://www.pianshen.com/article/7788199455/
>* https://www.iteye.com/blog/2057-1897176
>* https://blog.csdn.net/weixin_37621790/article/details/86695537
>* https://blog.csdn.net/huang_yong_peng/article/details/81879990
>* https://www.cnblogs.com/yinzhengjie/p/10970889.html
>* https://www.runoob.com/python/att-dictionary-copy.html
>* https://towardsdatascience.com/data-structure-heap-23d4c78a6962
>* https://github.com/python/cpython/blob/master/Lib/heapq.py
>* https://docs.python.org/3/library/heapq.html
>* https://www.geeksforgeeks.org/iterative-heap-sort/

可以用的package **heapq**
```python=
from heapq import heappush,heappop  
  
def heap_sort(iterable):  
    h = []  
    for value in iterable:  
        heappush(h, value)  
    return [heappop(h) for i in range(len(h))]  
  
def main():  
    L = [1, 3, 5, 7, 9, 2, 4, 6, 8, 0]  
    print( heap_sort(L)  )
  
if __name__ == "__main__":  
    main()  
```
老師的例子
```python=
# Python program for implementation of heap Sort 

# To heapify subtree rooted at index i. 
# n is size of heap 
def heapify(arr, n, i): 
    largest = i # Initialize largest as root 
    l = 2 * i + 1    # left = 2*i + 1 
    r = 2 * i + 2    # right = 2*i + 2 

    # See if left child of root exists and is 
    # greater than root 
    if l < n and arr[i] < arr[l]: 
        largest = l 

    # See if right child of root exists and is 
    # greater than root 
    if r < n and arr[largest] < arr[r]: 
        largest = r 

    # Change root, if needed 
    if largest != i: 
        arr[i],arr[largest] = arr[largest],arr[i] # swap 

        # Heapify the root. 
        heapify(arr, n, largest) 

# The main function to sort an array of given size 
def heapSort(arr): 
    n = len(arr) 

    # Build a maxheap. 
    for i in range(n, -1, -1): 
        heapify(arr, n, i) 

    # One by one extract elements 
    for i in range(n-1, 0, -1): 
        arr[i], arr[0] = arr[0], arr[i] # swap 
        heapify(arr, i, 0) 

# Driver code to test above 
arr = [ 12, 11, 13, 5, 6, 7] 
heapSort(arr) 
n = len(arr) 
print ("Sorted array is") 
for i in range(n): 
    print ("%d" %arr[i]), 
# This code is contributed by Mohit Kumra 
```
**理解概念之後畫出的**
# 流程圖
![](https://github.com/ykz0608/DSA/blob/master/image/hear%20sort.svg)

# 程式碼

自己尝试寫一次:
```python=
import random
import pandas 
import numpy as np

x = np.random.randint(-100,100,10)
#隨機生成數字
arr = x.tolist()
print("測試數值=",arr)

def heapify(data, root, n):
    largest = root #建立root
    left = 2 * root + 1 
    #proof
    # if root=0,left1=2*0+1=1
    # if root=1,left2=2*1+1=3
    
    right = 2 * root + 2
    #proof
    # if root=0,left1=2*0+2=2,
    # if root=1,left2=2*1+2=4,
    
    if left < n and data[left] > data[root]:
        largest = left
        #if left的index大於root 交换位置
        
    if right < n and data[right] > data[root]:
        largest = right
        #if right的index大於root 交换位置
        
    if largest != root:#改變root
        data[largest], data[root] = data[root], data[largest]
        #兩個交換
        heapify(data, largest , n)
        
    def heap_sort(data):
    n = len(data)
    for i in range(n // 2 - 1, -1, -1):
        heapify(data, i, n)
        #建立Max-Heap
    for i in range(n - 1, 0, -1):
        data[0], data[i] = data[i],data[0]
        heapify(data, 0, i)
    return data
    
    heap_sort(arr)
```
output = [-74, -4, 31, 21, -23, -21, 30, 77, 67, 87]
* 第一次嘗試不成功。。。
* 修復錯誤ing
* A FEW MOMENT LATER

```python=
def heapify(data, root, n):
    largest = root #建立root
    left = 2 * root + 1 
    #proof
    # if root=0,left1=2*0+1=1
    # if root=1,left2=2*1+1=3
    
    right = 2 * root + 2
    #proof
    # if root=0,left1=2*0+2=2,
    # if root=1,left2=2*1+2=4,
    
    if left < n and data[left] > data[largest]:
        largest = left
        #if left的index大於root 交换位置
        
    if right < n and data[right] > data[largest]:
        largest = right
        #if right的index大於root 交换位置
        
    if largest != root:#改變root
        data[largest], data[root] = data[root], data[largest]
        #兩個交換
        heapify(data, largest , n)

def heap_sort(data):
    n = len(data)
    for i in range(n , -1, -1):
        heapify(data, i, n)
        #建立Max-Heap
    for i in range(n - 1, 0, -1):
        data[0], data[i] = data[i],data[0]
        heapify(data, 0, i)
    return data


```
output=[-74, -23, -21, -4, 21, 30, 31, 67, 77, 87]
* 經過嘗試后。。。finally!!!root的位置很重要 要定義好

# 接下來開始作業
## 過程分為

1. 建立heap
2. 提取最小值
3. 放在序列最後
4. 然後交換到新序列裡
5. 重複指導排序完成

# 直接賦值和 copy 的區別
dict1 =  {'user':'runoob','num':[1,2,3]}
 
dict2 = dict1          # 淺拷貝: 引用對象
dict3 = dict1.copy()   # 淺拷貝：深拷貝父對象（一級目錄），子對象（二級目錄）不拷貝，還是引用
 
# 修改 data 數據
dict1['user']='root'
dict1['num'].remove(1)
 
# 輸出結果
print(dict1)
print(dict2)
print(dict3)

{'num': [2, 3], 'user': 'root'}
{'num': [2, 3], 'user': 'root'}
{'num': [2, 3], 'user': 'runoob'}
