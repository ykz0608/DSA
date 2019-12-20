# HW5 BFS Queue/DFS Stack
## 學習歷程：

### 原理:

#### BFS
* 寬度優先搜索(Breadth First Search,又稱廣度優先搜索)
* 是從根節點開始，遍歷完畢整張圖，不考慮結果所在的位置， 無論如何都要遍歷完畢整張地圖才終止。
* 按照就近原則進行， 距離原點相同的節點的訪問順序是相近的。
* 基本思路:
    1. 把根節點放到隊列的末尾。
    2. 每次從隊列的頭部取出一個元素，查看這個元素所有的下一級元素，把它們放到隊列的末尾。並把這個元素記爲它下一級元素的前驅。
    3. 找到所要找的元素時結束程序。
    4. 如果遍曆整個樹還沒有找到，結束程序。

#### DFS
* 深度優先搜索(Depth First Search)屬于算法的一種
* 是從根節點開始，逐個訪問每一條路徑，對於具有多子節點的節點而言，先搜尋到某一條子路的最深處，再逐個回溯前驅節點。
* 基本思路:
    1. 訪問頂點v
    2. 依次從v的未被訪問的鄰接點出發，對圖進行深度優先遍曆；直至圖中和v有路徑相通的頂點都被訪問。
    3. 若此時圖中尚有頂點未被訪問，則從一個未被訪問的頂點出發，重新進行深度優先遍曆，直到圖中所有頂點均被訪問過爲止。

### BFS和DFS的比較:

1. 數據結構上的運用
    * BFS
        * 用queue的形式
        * 先進先出
        * 需要與節點數成正比的記憶體空間

    * DFS
        * 用遞歸的形式，用到了stack
        * 先進後出
        * 較省記憶體空間

2. 複雜度
    * BFS:
        * 空間複雜度為O（v）
        * 時間復雜度為O(|V|+|E|) 
        * 適合大範圍的尋找
    * DFS:
        * 空問複雜度為O(V）
        * 時間複雜度為O(V+E)
        * 適合目標明確
    * 不同之處在于遍曆的方式與對于問題的解決出發點不同。

    
3. 思路
    * 廣度優先遍曆使用隊列(queue)來實現,整個過程也可以看作一個倒立的樹形:
        * 把根結點放到隊列的末尾
        * 每次從隊列的頭部取出一個元素,查看這個元素所有的下一級元素,把它們放在隊列的末尾。並且把這個元素記爲下一個元素的前驅
        * 找到所有要找的元素時結束程序
        * 如果遍曆整個樹還沒有找到,結束程序
    * 深度優先遍曆用棧(stack)實現,整個過程可以想象成一個倒立的樹形:
        * 把根結點壓入棧中
        * 每次從棧中彈出一個元素,搜索所有在它下一級的元素,把這些元素壓入棧中。並且把這個元素記爲它下一個元素的前驅。
        * 找到所有要找的元素時結束程序
        * 如果遍曆整個樹還沒有找到，結束程序

## BFS流程圖
![](https://github.com/ykz0608/DSA/blob/master/image/bfs.svg)

## DFS流程圖
![](https://github.com/ykz0608/DSA/blob/master/image/dfs.svg)

## 作業格式


```python
# Python3 Program to print BFS traversal 
# from a given source vertex. BFS(int s) 
# traverses vertices reachable from s. 
from collections import defaultdict 
  
# This class represents a directed graph 
# using adjacency list representation 
class Graph:
    # Constructor 
    def __init__(self): 
        # default dictionary to store graph 
        self.graph = defaultdict(list) 

    # function to add an edge to graph 
    def addEdge(self,u,v): 
        self.graph[u].append(v) 
  
    # Function to print a BFS of graph 
    def BFS(self, s): 
        """
        :type s: int
        :rtype: list
        """
    def DFS(self, s):
        """
        :type s: int
        :rtype: list
        """
  
        
  
```        

## 嘗試寫BFS code


```python
from collections import defaultdict 

class Graph:
    def __init__(self): 
        self.graph = defaultdict(list) 

    def addEdge(self,u,v): 
        self.graph[u].append(v) 
  
    def BFS(self, s): 
        queue = [] 
        output = []
        if len(output)==0:
            output.append(s)
            queue.append(self.graph[s])  
        
        while len(queue) != 0 :   
            output.append(queue[0])
            queue.pop(0)
            for i in self.graph[queue[0]]:
                if i not in queue and i not in output:
                    queue.append(i)
        return output
        
    #def DFS(self, s):

  
        
      
```

助教測值


```python
g = Graph()
g.addEdge(0,1)
g.addEdge(0,2)
g.addEdge(1,2)
g.addEdge(2,0)
g.addEdge(2,3)
g.addEdge(3,3)
g.graph
```




    defaultdict(list, {0: [1, 2], 1: [2], 2: [0, 3], 3: [3]})




```python
print(g.BFS(2))
```


    ---------------------------------------------------------------------------

    IndexError                                Traceback (most recent call last)

    <ipython-input-193-a38c2d0c02d3> in <module>
    ----> 1 print(g.BFS(2))
    

    <ipython-input-191-4b65ef507882> in BFS(self, s)
         18             output.append(queue[0])
         19             queue.pop(0)
    ---> 20             for i in self.graph[queue[0]]:
         21                 if i not in queue and i not in output:
         22                     queue.append(i)
    

    IndexError: list index out of range


超出范围了 要改


```python
from collections import defaultdict 

class Graph:
    def __init__(self): 
        self.graph = defaultdict(list) 

    def addEdge(self,u,v): 
        self.graph[u].append(v) 
  
    def BFS(self, s): 
        queue = [] 
        output = []
        if len(output)==0:
            output.append(s)
            queue.extend(self.graph[s])  
        
        while len(queue) != 0 :   
            output.append(queue[0])
            queue.pop(0)
            for i in self.graph[queue[0]]:
                if i not in queue and i not in output:
                    queue.append(i)
        return output
        
    #def DFS(self, s):

  
        
      
```


```python
g = Graph()
g.addEdge(0,1)
g.addEdge(0,2)
g.addEdge(1,2)
g.addEdge(2,0)
g.addEdge(2,3)
g.addEdge(3,3)

print(g.BFS(2))
#print(g.DFS(2))
```


    ---------------------------------------------------------------------------

    IndexError                                Traceback (most recent call last)

    <ipython-input-195-1219c43954fa> in <module>
          7 g.addEdge(3,3)
          8 
    ----> 9 print(g.BFS(2))
         10 #print(g.DFS(2))
    

    <ipython-input-194-daf5273b3007> in BFS(self, s)
         18             output.append(queue[0])
         19             queue.pop(0)
    ---> 20             for i in self.graph[queue[0]]:
         21                 if i not in queue and i not in output:
         22                     queue.append(i)
    

    IndexError: list index out of range


修改後:


```python
from collections import defaultdict 

class Graph:
    def __init__(self): 
        self.graph = defaultdict(list) 

    def addEdge(self,u,v): 
        self.graph[u].append(v) 
  
    def BFS(self, s): 
        queue = [] 
        output = []
        if len(output)==0:
            output.append(s)
            queue.extend(self.graph[s])  
        
        while len(queue) != 0 :   
            vertex = queue[0]
            output.append(vertex)
            queue.pop(0)
            for i in self.graph[vertex]:
                if i not in queue and i not in output:
                    queue.append(i)
        return output
        
    #def DFS(self, s):

  
        
      
```


```python
g = Graph()
g.addEdge(0,1)
g.addEdge(0,2)
g.addEdge(1,2)
g.addEdge(2,0)
g.addEdge(2,3)
g.addEdge(3,3)

print(g.BFS(2))
#print(g.DFS(2))
```

    [2, 0, 3, 1]
    

成功!再測試


```python
g = Graph()
g.addEdge(1,2)
g.addEdge(1,4)
g.addEdge(2,3)
g.addEdge(2,6)
g.addEdge(3,5)
g.addEdge(3,7)
g.addEdge(2,1)
g.addEdge(4,6)
g.addEdge(5,2)
g.addEdge(5,6)
g.addEdge(6,1)
g.addEdge(7,5)
g.BFS(3)
```




    [3, 5, 7, 2, 6, 1, 4]



Next DFS只是改變入排序的方式 


```python
from collections import defaultdict 

class Graph:
    def __init__(self): 
        self.graph = defaultdict(list) 

    def addEdge(self,u,v): 
        self.graph[u].append(v) 
  
    def BFS(self, s): 
        queue = [] 
        output = []
        if len(output)==0:
            output.append(s)
            queue.extend(self.graph[s])  
        
        while len(queue) != 0 :   
            vertex = queue[0]
            output.append(vertex)
            queue.pop(0)
            for i in self.graph[vertex]:
                if i not in queue and i not in output:
                    queue.append(i)
        return output
        
    def DFS(self, s): 
        queue = [] 
        output = []
        if len(output)==0:
            output.append(s)
            queue.extend(self.graph[s])  
        
        while len(queue) != 0 :   
            vertex = queue[-1]
            output.append(vertex)
            queue.pop(-1)
            for i in self.graph[vertex]:
                if i not in queue and i not in output:
                    queue.append(i)
        return output
      

```


```python
g = Graph()
g.addEdge(0,1)
g.addEdge(0,2)
g.addEdge(1,2)
g.addEdge(2,0)
g.addEdge(2,3)
g.addEdge(3,3)

print(g.BFS(2))
print(g.DFS(2))
```

    [2, 0, 3, 1]
    [2, 3, 0, 1]
    


```python
g = Graph()
g.addEdge(1,2)
g.addEdge(1,4)
g.addEdge(2,3)
g.addEdge(2,6)
g.addEdge(3,5)
g.addEdge(3,7)
g.addEdge(7,5)
g.addEdge(5,2)
g.addEdge(5,6)
g.addEdge(6,1)
g.addEdge(4,6)
print(g.BFS(7))
```

    [7, 5, 2, 6, 3, 1, 4]
    

## 參考資料

### 原理參考網站:
>* https://blog.csdn.net/saltriver/article/details/54429068
>* http://simonsays-tw.com/web/DFS-BFS/DepthFirstSearch.html
>* https://blog.csdn.net/raphealguo/article/details/7523411
>* https://blog.csdn.net/g11d111/article/details/76169861
>* https://blog.csdn.net/jnu_simba/article/details/8868235
>* https://www.jianshu.com/p/b086986969e6
>* https://www.jianshu.com/p/bff70b786bb6
>* https://codertw.com/%E7%A8%8B%E5%BC%8F%E8%AA%9E%E8%A8%80/102866/
>* https://magiclen.org/dfs-bfs/
>* https://zhuanlan.zhihu.com/p/24986203
>* https://www.itread01.com/content/1541297601.html

### 程式碼參考網站:
>* https://zhuanlan.zhihu.com/p/50187643
>* http://programmermagazine.github.io/201406/htm/focus1.html
>* https://www.jianshu.com/p/d2125448270b
>* https://medium.com/@yasufumy/algorithm-breadth-first-search-408297a075c9
>* https://pythoninwonderland.wordpress.com/2017/03/18/how-to-implement-breadth-first-search-in-python/
>* https://blog.csdn.net/qq_24056913/article/details/88671025
>* https://www.jianshu.com/p/255a349fd9c8
>* https://www.geeksforgeeks.org/breadth-first-search-or-bfs-for-a-graph/


```python

```
